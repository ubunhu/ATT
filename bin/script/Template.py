# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 2:18 PM
# @Project  : ATT
# @File     : Template.py
# @explain  : 文件说明

import allure
import pytest
import setupMain

from bin.unit.initializeCase import ini_case
from bin.unit.initializePremise import ini_request
from bin.unit.apiSendCheck import api_send_check
from bin.unit.readParameter import read_param,check_param


PATH = setupMain.PATH + "/testcase/source"

case_dict = ini_case(PATH, "Template")

param = read_param(case_dict["test_case"]["test_name"],case_dict["test_case"]["parameter"],PATH,None)
#排列组合所有参数
test_param = check_param(param)

@allure.feature(case_dict["test_info"]["title"])
class TestTemplate:

    @pytest.mark.parametrize("case_data", case_dict["test_case"], ids=[])
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
