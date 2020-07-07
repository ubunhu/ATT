# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 2:19 PM
# @Project  : ATT
# @File     : Template_case.py
# @explain  : 文件说明


import allure
import pytest
import setupMain


from bin.unit.initializePremise import ini_request
from bin.unit.apiSendCheck import api_send_check



PATH = setupMain.PATH + "/testcase/source/login"


@allure.feature('登录模块')
class Testlogin:


    @allure.story("正确用户名和密码")
    @pytest.mark.parametrize("case_param", [{'usr': '1', 'psw': '1'}], ids=["参数{'usr': '1', 'psw': '1'}"])
    def test_login_1(self, case_param):
        """
        测试用例说明
        :test_case: Template

        """
        # 发送测试请求
        api_send_check({'id': '1', 'name': 'login', 'num': '1', 'title': '登录模块', 'case': '登录成功', 'description': '正确用户名和密码', 'before': '', 'params': [{'usr': '1', 'psw': '1'}], 'url': 'https://ms.shijiebang.com/assem/search/', 'file': '', 'method': 'post', 'header': {'Host': 'ms.shijiebang.com', 'Authorization': ' bearer MC4uLi4uLi0xNTkxOTMxNzYzNzQzLTE1OTQ1MjM3NjM3NDMtMDA4LTQtM2U1NDA3YWNmYjY0ODFlZWEzZmZkZmUwZDE0ZmJjNDk5OWMwNTIxMA', 'Cookie': 'nsid=wKgGFl54MSVkyk8SAw9kAg==;SERVER_ID=cebfcf3a-6b8d8f77'}, 'check': 'status_msg', 'expect': {'code': '200', 'msg': 'success'}, 'results': '', 'testResult': '', 'version': '', 'date': '', 'ids_data': ["参数{'usr': '1', 'psw': '1'}"]}, PATH)
    @allure.story("错误用户名")
    @pytest.mark.parametrize("case_param", [{'usr': '0', 'psw': '1'}], ids=["参数{'usr': '0', 'psw': '1'}"])
    def test_login_2(self, case_param):
        """
        测试用例说明
        :test_case: Template

        """
        # 发送测试请求
        api_send_check({'id': '2', 'name': 'login', 'num': '2', 'title': '登录模块', 'case': '登录失败', 'description': '错误用户名', 'before': '', 'params': [{'usr': '0', 'psw': '1'}], 'url': 'https://ms.shijiebang.com/assem/search/', 'file': '', 'method': 'post', 'header': {'Host': 'ms.shijiebang.com', 'Authorization': ' bearer MC4uLi4uLi0xNTkxOTMxNzYzNzQzLTE1OTQ1MjM3NjM3NDMtMDA4LTQtM2U1NDA3YWNmYjY0ODFlZWEzZmZkZmUwZDE0ZmJjNDk5OWMwNTIxMA', 'Cookie': 'nsid=wKgGFl54MSVkyk8SAw9kAg==;SERVER_ID=cebfcf3a-6b8d8f77'}, 'check': 'status_msg', 'expect': {'code': '200', 'msg': 'success'}, 'results': '', 'testResult': '', 'version': '', 'date': '', 'ids_data': ["参数{'usr': '0', 'psw': '1'}"]}, PATH)
    @allure.story("错误密码")
    @pytest.mark.parametrize("case_param", [{'usr': '1', 'psw': '0'}], ids=["参数{'usr': '1', 'psw': '0'}"])
    def test_login_3(self, case_param):
        """
        测试用例说明
        :test_case: Template

        """
        # 发送测试请求
        api_send_check({'id': '4', 'name': 'login', 'num': '3', 'title': '登录模块', 'case': '登录失败', 'description': '错误密码', 'before': '', 'params': [{'usr': '1', 'psw': '0'}], 'url': 'https://ms.shijiebang.com/assem/search/', 'file': '', 'method': 'post', 'header': {'Host': 'ms.shijiebang.com', 'Authorization': ' bearer MC4uLi4uLi0xNTkxOTMxNzYzNzQzLTE1OTQ1MjM3NjM3NDMtMDA4LTQtM2U1NDA3YWNmYjY0ODFlZWEzZmZkZmUwZDE0ZmJjNDk5OWMwNTIxMA', 'Cookie': 'nsid=wKgGFl54MSVkyk8SAw9kAg==;SERVER_ID=cebfcf3a-6b8d8f77'}, 'check': 'status_msg', 'expect': {'code': '200', 'msg': 'success'}, 'results': '', 'testResult': '', 'version': '', 'date': '', 'ids_data': ["参数{'usr': '1', 'psw': '0'}"]}, PATH)