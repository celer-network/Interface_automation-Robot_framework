#!/usr/bin/env bash
# Script to setup tools and env
# Push sdk-api.go to celerx-client repo
# Push all pb.go/pb.gw-.go files to x-proto-go repo

# $1 should be pr id number. if not a pr build, empty string for circle, false for travis
if [ "$1" != "false" ]; then
  PRID="$1" # PRID is a number or empty
fi
BRANCH="$2" # topic branch or master
TO_BRANCH="xproto-$PRID-$BRANCH"
XP_HEAD_COMMIT=`git rev-parse --short HEAD` # HEAD commit of x-proto change, used when push to other repos

PROTOC_VER="3.11.2" # github.com/protocolbuffers/protobuf/releases
GEN_GO_VER="v1.4.2" # github.com/golang/protobuf/releases
GEN_GRPCGW_VER="v1.14.4" # github.com/grpc-ecosystem/grpc-gateway/releases. note affected go repo go.mod must match this to ensure compatibility
GEN_API_VER="v1.10"  # our own protoc-gen-api
GENAPI="api.github.com/repos/celer-network/protoc-gen-api/releases"

# repos to push to
CXCLIENT="github.com/celer-network/celerx-client"
XPROTOGO="github.com/celer-network/x-proto-go"

# get protoc and gen-lint
dld_protoc() {
  # setup protoc and import google proto files
  curl -L https://github.com/protocolbuffers/protobuf/releases/download/v$PROTOC_VER/protoc-$PROTOC_VER-linux-x86_64.zip -o protoc.zip
  unzip protoc.zip -d protoc && rm protoc.zip
  # below proto needed for grpc gateway, uncomment when need to use grpc gateway
  curl -L --create-dirs 'https://raw.githubusercontent.com/googleapis/googleapis/master/google/api/{annotations,http}.proto' -o 'protoc/include/google/api/#1.proto'
  sudo mv protoc/bin/* /usr/local/bin/
  sudo mv protoc/include/* /usr/local/include/
  curl -LO https://github.com/ckaznocha/protoc-gen-lint/releases/download/v0.2.1/protoc-gen-lint_linux_amd64.zip && unzip protoc-gen-lint_linux_amd64.zip && chmod +x protoc-gen-lint
  sudo mv protoc-gen-lint /usr/local/bin
}

run_lint() {
  protoc -I. -I/usr/local/include --lint_out=. *.proto
}

# download/install tools needed for generating files, also setup_git
# grpc-gateway, gen-api are under /usr/local/bin
# protoc-gen-go is /go/bin via go install
prepare_tools() {
  # grpc-gateway for http api
  curl -L https://github.com/grpc-ecosystem/grpc-gateway/releases/download/$GEN_GRPCGW_VER/protoc-gen-grpc-gateway-$GEN_GRPCGW_VER-linux-x86_64 -o protoc-gen-grpc-gateway && chmod +x protoc-gen-grpc-gateway
  # gen-go for pb.go and grpc
  go get -d github.com/golang/protobuf/protoc-gen-go
  git -C "$GOPATH"/src/github.com/golang/protobuf checkout $GEN_GO_VER
  go install github.com/golang/protobuf/protoc-gen-go
  # celer protoc-gen-api, a bit more complicated due to private repo
  ASSET_ID=$(curl -s "https://$GH_TOKEN@$GENAPI/tags/$GEN_API_VER" | jq '.assets[] | select(.name == "protoc-gen-api").id')
  curl -JLO -H 'Accept: application/octet-stream' https://$GH_TOKEN@$GENAPI/assets/$ASSET_ID && chmod +x protoc-gen-api
  sudo mv protoc-gen* /usr/local/bin
  setup_git
}

# clone cxc repo, generate new sdk-api.go, push if needed
# TODO: check if sdk-* is in latest change, if not, skip
do_sdkapi() {
  clone_repo $CXCLIENT
  # generate sdk api code to celerx client repo, note sdk-api.proto file has no go_package option by design
  protoc -I. -I/usr/local/include --api_out=gopkg=celerxclient,owner=Client:$GOPATH/src/$CXCLIENT/celerxclient sdk-api.proto
  push2repo $GOPATH/src/$CXCLIENT
}

do_xprotogo() {
  clone_repo $XPROTOGO
  gen_xprotogo
  push2repo $GOPATH/src/$XPROTOGO
}

# clone repos and checkout to $TO_BRANCH if $PRID isn't empty, or stay on default branch if PRID is empty
# $1 is the repo url, eg. $CXCLIENT
clone_repo() {
  git clone https://$GH_TOKEN@$1 $GOPATH/src/$1
  # if a PR build, checkout a new branch from PRID and proto branch name
  # if same branch already exists in remote, meaning we're not first commit in this PR,
  # git checkout $TO_BRANCH creates and track remote automatically
  if [ -n "$PRID" ]; then
    pushd $GOPATH/src/$1
    co_branch $TO_BRANCH
    popd
  fi
}

# first backup our own err.go files in $XPROTOGO, then back to x-proto to generate go files using protoc
# generated files at $GOPATH/src/$XPROTOGO, b/c all proto should have correct go_package option
gen_xprotogo() {
  pushd $GOPATH/src/$XPROTOGO
  # backup our own err.go
  mv errcode/err.go errcode_err.go
  mv sdkdata/err.go sdkdata_err.go
  # delete folders under x-proto-go
  rm -r */
  # put back err.go
  mkdir -p errcode sdkdata
  mv errcode_err.go errcode/err.go
  mv sdkdata_err.go sdkdata/err.go
  popd

  # back to x-proto root

  # all proto files below has option go_package
  ###### data only 
  # generate sdk data pb.go, gopkg: x-proto-go/sdkdata
  protoc -I. -I/usr/local/include --go_out=$GOPATH/src sdk-data.proto
  # err
  protoc -I. -I/usr/local/include --go_out=$GOPATH/src error.proto
  # generate common pb.go, gopkg: x-proto-go/common
  protoc -I. -I/usr/local/include --go_out=$GOPATH/src common_*.proto
  # generate user event pb.go, gopkg: x-proto-go/ue
  protoc -I. -I/usr/local/include --go_out=$GOPATH/src user_event.proto
  # generate system event pb.go, gopkg: x-proto-go/se
  protoc -I. -I/usr/local/include --go_out=$GOPATH/src system_event.proto
  # generate match ticket pb.go, gopkg: x-proto-go/matchticket
  protoc -I. -I/usr/local/include --go_out=$GOPATH/src match_ticket_internal.proto
  # generate campaign mobile pb.go, gopkg: x-proto-go/campaign
  protoc -I. -I/usr/local/include --go_out=$GOPATH/src campaign_mobile.proto
  # generate sale mobile pb.go, gopkg: x-proto-go/sale
  protoc -I. -I/usr/local/include --go_out=$GOPATH/src sale_mobile.proto

  ###### data and grpc, misc biz modules, gen-go doesn't support mixed proto pkg
  # KEEP list in order!
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src account_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src bank_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src match_engine_internal.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src campaign.proto user_tagging.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src finance_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src invitation_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src loyalty_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src notification_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src social_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src auth_mgr_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src league_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src history_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src tournament_*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src match_mobile*.proto
  protoc -I. -I/usr/local/include --go_out=plugins=grpc:$GOPATH/src --grpc-gateway_out=$GOPATH/src sale_internal.proto
}

setup_git() {
  git config --global user.email "build@celer.network"
  git config --global user.name "Build Bot"
  git config --global push.default "current" # so git push doesn't require branch name
}

# checkout or create a local branch
co_branch() {
  git fetch
  git checkout $1 || git checkout -b $1
}

update_proto_commit_file() {
  echo -e "commit: $XP_HEAD_COMMIT\nbranch: $BRANCH\nPR: $PRID" > .proto.commit
}

# $1 local repo folder
push2repo() {
  pushd $1
  if [[ `git status --porcelain` ]]; then
    update_proto_commit_file
    git add .
    if [ -n "$PRID" ]; then
      git commit -m "Sync bindings for x-proto/pull/$PRID" -m "x-proto branch: $BRANCH commit: $XP_HEAD_COMMIT"
    else
      # master branch sync mode, use a msg w/o PRID
      git commit -m "Sync from x-proto $BRANCH commit: $XP_HEAD_COMMIT"
    fi
    git push
  else
    echo "skip push due to no diff"
  fi
  popd
}

sync_tag() {
  echo "tag: $1"
  # clone if no x-proto-go folder
  [ ! -d "$GOPATH/src/$XPROTOGO" ] && clone_repo $XPROTOGO
  pushd $GOPATH/src/$XPROTOGO
  git tag "$1" && git push origin "$1"
  popd
}

########## DONOT USE BELOW ##########
# if x-proto/go folder has changes, add commit and push to current pr branch
# this is deprecated as we now push to x-proto-go repo. keep here for reference only
push_add2pr() {
  if [[ `git status --porcelain go` ]]; then
    git add go/
    git commit -m "[skip ci] Update x-proto-go pb.go files by build bot, based on $XP_HEAD_COMMIT"
    git push https://${GH_TOKEN}@github.com/celer-network/x-proto $BRANCH
  fi
}
