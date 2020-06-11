# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 2:19 PM
# @Project  : ATT
# @File     : Template_case.py
# @explain  : 文件说明


import allure
import pytest
import setupMain

from bin.unit.initializeCase import ini_case
from bin.unit.initializePremise import ini_request
from bin.unit.apiSendCheck import api_send_check
from bin.unit.readParameter import read_param,check_param
from bin.script.customParam import customparam


PATH = setupMain.PATH + "/testcase/source/blogpost"

case_dict = ini_case(PATH, "blogpost")
#使用自定义的参数
param = customparam()
#使用chls请求时参数
param = read_param(case_dict["test_case"]["test_name"],case_dict["test_case"]["parameter"],PATH,None)
#排列组合所有参数
test_param = check_param(param)
if len(test_param) == 0:
	ids_data = []
else:
	ids_data = [
	    "参数{}".
	        format(id_data) for id_data in test_param
	]

@pytest.fixture()
def blogpost_before():
	"""
	from resoure.fixture import xxx
	xxx(xxx)
	"""
	print("if need add other fixture")
@pytest.mark.usefixtures("blogpost_before")
@allure.feature(case_dict["test_info"]["title"])
class TestBlogpost(object):


    @allure.story("blogpost")
    #@pytest.mark.flaky(reruns=3, reruns_delay=3)
    @pytest.mark.parametrize("case_param", test_param, ids=ids_data)
    def test_blogpost(self, case_param):
        """
		测试用例说明
        :test_case: blogpost

        """
        self.init_relevance = ini_request(case_dict, PATH)
        # 发送测试请求
        api_send_check(case_dict["test_case"], case_dict, self.init_relevance, case_param, PATH)


