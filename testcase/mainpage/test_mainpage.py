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



PATH = setupMain.PATH + "/testcase/source/mainpage"


@allure.feature('首页')
class Testmainpage:


    @allure.story("正确数据")
    @pytest.mark.parametrize("case_param", [{}], ids=['参数{}'])
    def test_mainpage_1(self, case_param):
        """
        测试用例说明
        :test_case: Template

        """
        # 发送测试请求
        api_send_check({'id': '3', 'name': 'mainpage', 'num': '1', 'title': '首页', 'case': '首页数据正常', 'description': '正确数据', 'before': '', 'params': [{}], 'url': 'http://test.doctorpanda.com/panda-user-web/mainpage/getMP?bizType=1', 'file': '', 'method': 'get', 'header': {'Host': 'test.doctorpanda.com'}, 'check': 'status_msg', 'expect': {'code': '200', 'msg': '请求成功'}, 'results': '', 'testResult': '', 'version': '', 'date': '', 'ids_data': ['参数{}']}, PATH)