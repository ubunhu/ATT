# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:49 PM
# @Project  : ATT
# @File     : writeCase.py
# @explain  : 文件说明



import os,re
import shutil

from bin.script.mkDir import mk_dir
from bin.script.writeCaseYml import write_case_yml

from bin.unit.initializeCase import ini_case
from bin.unit.readParameter import check_param
#from bin.script.customParam import customparam

#自动定义并生成普通case
def write_case(case,case_list,src,new_case,case_num,source_path):
    shutil.copyfile(src, new_case)
    case_list= ini_case(source_path, case, case_list)
    #使用自定义的参数
    #param = customparam()
    for case_dict in case_list:
        #排列组合所有参数
        #case_dict["params"] = check_param(case_dict["params"])
        #直接使用默认参数
        param_list =[]
        param_list.append(case_dict["params"])
        case_dict["params"] = param_list
        if len(case_dict["params"]) == 0:
            ids_data = []
        else:
            ids_data = [
                "参数{}".
                    format(id_data) for id_data in case_dict["params"]
            ]
        case_dict['ids_data'] = ids_data
    with open(new_case, 'r', encoding='UTF-8') as fw:
        source = fw.readlines()
    n = 0
    content = '''
    @allure.story("%s")
    @pytest.mark.parametrize("case_param", %s, ids=%s)
    def test_%s_%s(self, case_param):
        """
        测试用例说明
        :test_case: Template

        """
        # 发送测试请求
        api_send_check(%s, PATH)'''
    with open(new_case, 'w') as f:
        for line in source:
            if 'PATH = setupMain.PATH' in line:
                line = line.replace("/testcase/source", "/testcase/source/%s" % case)
                f.write(line)
                n = n + 1
            elif '@allure.feature' in line:
                line = line.replace("@allure.feature", "@allure.feature('%s')" % case_dict['title'])
                f.write(line)
                n = n + 1
            elif 'class TestTemplate' in line:
                line = line.replace("TestTemplate", "Test%s" % case)
                f.write(line)
                n = n + 1
            elif '@pytest.mark.parametrize' in line:
                for case_dict in case_list:
                    #line = line.replace("@pytest.mark.parametrize", content % (case_dict['description'],case_dict['params'],case_dict['ids_data'],case_dict,case_dict,case_dict['params']))
                    f.write(content % (case_dict['description'],case_dict['params'],case_dict['ids_data'],case_dict['name'],case_dict['num'],case_dict))
                    n += 1
                break
            else:
                f.write(line)
        # for i in range(n, len(source)):
        #   	 f.write(source[i])

def write_define(_path):
    case_list = write_case_yml(_path)
    project_path = str(os.path.abspath('.').split('/bin')[0])
    test_path = project_path + '/testcase/'
    src = project_path + '/bin/script/Template_case.py'
    src_fixture = project_path + '/bin/script/Template_fixture.py'

    for case in case_list:
        case_num = case_list[case]

        case_name = 'test_' + case + '.py'
        source_path = test_path + 'source' + '/' + case
        new_case = test_path + case + '/' + case_name
        mk_dir(test_path + case)
        if case_list[case] > 1:
            if case_name in os.listdir(test_path + case):
                pass
            else:
                write_case(case,case_list,src,new_case,case_num,source_path)
        else:
            if case_name in os.listdir(test_path + case):
                pass
            else:
                write_case(case,case_list,src,new_case,case_num,source_path)