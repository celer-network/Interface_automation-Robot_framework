# This repo is shared between mobile and backend teams. Read below carefully before making changes!
1. follow protobuf [style guide](https://developers.google.com/protocol-buffers/docs/style). File name should be snake_case.proto (sdk-data and sdk-api are only exception)
2. read our own [x-proto style guide](https://docs.google.com/document/d/1hCm4YKdrnaJqzOimokRIF3hLt6OUZ_bQAc43JgvuBW8/edit#)
3. write lots of comments about message and rpc, especially error/corner cases. so whoever using the msg/rpc has fewer surprises
4. editing existing messages must be [backward compatible](https://developers.google.com/protocol-buffers/docs/proto3#updating_a_message_type), unless the message is never used in our prod system. If the message is used in staging, then we need to decide whether changing the message can justify the cost of re-write in message consumers
5. multiple proto files can share same package, this will simplify use definitions defined in other proto files. Note: each proto file can define their own java/go package so generated code is still organized

## SDK proto files (used by both mobile, sdk and backend teams)
- sdk-data.proto: data model definition for SDK layer
- sdk-api.proto: API definition using grpc syntax, will generate client stub using our own gen-api tool

We're phasing out this in favor of mobile native grpc and shared data mobel between mobile and backend directly.

Notes:
1. changes to sdk-api.proto and sdk-data.proto requires mobile TL review
2. data across SDK API layer is serialized bytes of protobuf message or scalar type like int, bool.
3. sdk-data.proto should only include messages that cross SDK API layer (ie. used by both mobile app and sdk golang code)
4. for better readability, use service to group related APIs in sdk-api.proto, eg. service FiatAPIs. Note service name/hierarchy is not included in generated API code stub (this could change in the future)
5. for callbacks, define a service that ends w/ `Callback`, eg. MyCallback, then includes all callback functions as rpc in the service, returns should be google.protobuf.Empty as no callback return value is supported for now.
6. root level APIs (not belong to celerxclient) can be set via rootapi option, see sdk-api.proto for example

## GRPC Files:
- user_event.proto: shared definition of user events like deposit, game result etc.
- error.proto: shared definition of error code enum and error message definition. each module has its own errcode range
- campaign.proto: shared definition of campaign service like create campaign, check campaign and send RC etc.
- user_tagging.proto: user tagging query.
- common_backend.proto: shared definition of common celerx backend messages.
- finance.proto: fiat deposit etc and bank
- invitation.proto: refer code, check bonus etc
- loyalty.proto: win and redeem gems
- social.proto: social feeds and challenge
- account.proto: user account login and management

Notes:
1. **GRPC server handlers MUST NOT return grpc error**. Errors should be sent back to requester as BackendError message. this also requires rpc response definition should always include an BackendError message field and error code enum is defined in error.proto
2. all internal rpcs between backend systems should be via grpc/protobuf
3. if there is a need for http access, use `option(google.api.http)`. for transcoding http/json to grpc, use envoy proxy or grpc-gateway. Internal only http (eg. for admin web) URL must begin w/ `/internal` so we can block at ingress. [more details](https://svblockchain.slack.com/archives/CLLHEP5L4/p1579567960052800)

## Workflow
The goal is to have all data definitions and rpc interfaces of new celerx modules defined in one place. So cross-team collaboration is more efficient, with minimal confusion/misunderstanding.

For languages that support using .proto files directly (like java), we recommend using git submodule(or subtree) to include proto files in source code repo.

For golang, after a PR is created, CI will run protoc generating pb.go files and push to x-proto-go repo. If x-proto PR number is 123, topic branch is addmsg, the x-proto-go branch will be `xproto-123-addmsg`. So during local developing, just do `go get github.com/celer-network/x-proto-go@xproto-123-addmsg`. NO NEED to create a PR in x-proto-go repo! After x-proto PR is merged, CI will run again on master and sync automatically to x-proto-go master. Only need to run `go get github.com/celer-network/x-proto-go@master`. x-proto release tags will also be synced to x-proto-go repo, with same name.

If PR has API changes in sdk-api.proto, CI will generate celerxclient/sdk-api.go and push a branch to https://github.com/celer-network/celerx-client repo. Because sdk-api.go is only a stub (missing actual function implementation), eng who work on SDK APIs should follow instructions in celerx-client repo to add implementation.

## Resolve conflicts
1. Use short-live topic branch. Always pull master before creating a branch. And delete the branch from github and local after PR merged
2. If github shows PR has conflict file so can't merge, run below locally:
```bash
# at topic branch, make sure to have latest commit of PR
git pull
# fetch latest remote master
git fetch origin master:master
# merge origin/master to topic branch, and prefer their changes
git merge -s recursive -Xtheirs --no-edit origin/master
# push again to PR, it should be ok to merge
git push
```
If merge failed due to conflict in .proto files, need to manually resolve the conflict. Contact junda for any question/help.
