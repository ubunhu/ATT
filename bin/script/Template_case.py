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



PATH = setupMain.PATH + "/testcase/source"


@allure.feature
class TestTemplate:

    @pytest.mark.parametrize
    @allure.story("Template")
    @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_template(self, case_data):
        """

        :param case_data: 测试用例
        :return:
        """
        #self.init_relevance = ini_request(case_dict, PATH)
        # 发送测试请求
        api_send_check(case_data, case_dict, self.init_relevance, PATH)