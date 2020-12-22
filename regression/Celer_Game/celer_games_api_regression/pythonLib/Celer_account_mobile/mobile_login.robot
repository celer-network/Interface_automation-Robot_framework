*** Settings ***
#Library  account_mobile_pb2.py
#Library  account_mobile_pb2_grpc.py
#Library  account_mobile_client.py
#Library  account_mobile_run.py

Library     robot_login_run.py
Library     Collections
Library    RequestsKeywords.py
#Library   RequestsLibrary


*** Variables ***


*** Keywords ***
ACCOUNT MOBILE API
    [Arguments]     # ${login_email}  ${password}
    [Documentation]    登录获取token
    ${headers}   Create Dictionary
    ${login}    test_run_01    pknafg52837@chacuo.net    yandong01
#    create session    alias=celer    url=celerx-test.celer.app
#    ${Ret}   post request    celer    ${login}    ""
    ${result}    To Json    ${login}
#    Should Contain    ${result}    statusCode
    ${str}      Get From Dictionary     ${result}    statuscode
#    Should Be Equal As Integers    ${str}
    log    ${str}
    should be equal as strings    ${str}    200
    [Return]     ${result}


#*** Test Cases ***
#mobile login
#    [Tags]  HTTP API
#    ${ret}      ACCOUNT MOBILE API    # login_email=pknafg52837@chacuo.net     password=yandong001
#    log    登录成功
##    ${result}    Get From Dictionary    ${ret}    result
##    ${message}    get from dictionary   ${result}    message
##    # 输出消息格式
##     log    ${message}

