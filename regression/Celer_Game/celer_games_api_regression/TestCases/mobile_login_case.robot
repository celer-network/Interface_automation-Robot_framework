# Copyright 2020 juqitech (Shanghai) Ltd.
# Authors: yandong

*** Settings ***
Documentation    Suite description
Resource    ../pythonLib/Celer_account_mobile/mobile_login.robot


*** Variables ***

*** Test Cases ***
mobile login
    [Tags]  HTTP API
    ${ret}      ACCOUNT MOBILE API    # login_email=pknafg52837@chacuo.net     password=yandong001
    log    登录成功
#    ${result}    Get From Dictionary    ${ret}    result
#    ${message}    get from dictionary   ${result}    message
#    # 输出消息格式
#     log    ${message}
*** Keywords ***