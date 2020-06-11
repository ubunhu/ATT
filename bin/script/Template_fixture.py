# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 2:20 PM
# @Project  : ATT
# @File     : Template_fixture.py
# @explain  : 文件说明



import setupMain
from bin.unit.initializeCase import ini_case
from bin.unit import checkResult, apiSend
from bin.unit.readParameter import read_param

PATH = setupMain.PATH + "/aff/page/commonData/offer"

case_dict = ini_case(PATH, "Template")

param = read_param(case_dict["test_case"]["test_name"],case_dict["test_case"]["parameter"],PATH,None)

def test_template(param,PATH):
    """
	测试预置条件说明
    :test_case: Template

    """
    # 发送测试请求
    #apiSend(case_dict["test_case"], case_dict, self.init_relevance, param, PATH)
    code, data = apiSend.send_request(case, project_dict["test_info"].get("host"),
	                                  project_dict["test_info"].get("address"), param, PATH, relevance)
    print(code,data)