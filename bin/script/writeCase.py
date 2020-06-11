# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:49 PM
# @Project  : ATT
# @File     : writeCase.py
# @explain  : 文件说明



import os
import shutil
from bin.script.mkDir import mk_dir
from bin.script.writeCaseYml import write_case_yml

#自动定义并生成预置case
def write_fixture(case,src,new_case):
	shutil.copyfile(src, new_case)
	with open(new_case, 'r') as fw:
		source = fw.readlines()
	n = 0
	with open(new_case, 'w') as f:
		for line in source:
			if 'PATH = setupMain.PATH' in line:
				line = line.replace("/aff/page/commonData/offer", "/aff/page/commonData/%s" % case)
				f.write(line)
				n = n + 1
			elif 'case_dict = ini_case' in line:
				line = line.replace("Template", case)
				f.write(line)
				n = n + 1
			elif 'class TestTemplate' in line:
				line = line.replace("TestTemplate", "Test%s" % case.title().replace("_", ""))
				f.write(line)
				n = n + 1
			elif '@allure.story' in line:
				line = line.replace("Template", case)
				f.write(line)
				n = n + 1
			elif 'def test_template' in line:
				line = line.replace("template", case.lower())
				f.write(line)
				n = n + 1
			elif 'test_case: Template' in line:
				line = line.replace("Template", case)
				f.write(line)
				n = n + 1
			else:
				f.write(line)
				n += 1
		for i in range(n, len(source)):
			f.write(source[i])
#自动定义并生成普通case
def write_case(case,src,new_case):
	shutil.copyfile(src, new_case)
	with open(new_case, 'r') as fw:
		source = fw.readlines()
	n = 0
	with open(new_case, 'w') as f:
		for line in source:
			if 'PATH = setupMain.PATH' in line:
				line = line.replace("/testcase/source", "/testcase/source/%s" % case)
				f.write(line)
				n = n + 1
			elif 'case_dict = ini_case' in line:
				line = line.replace("Template", case)
				f.write(line)
				n = n + 1
			elif 'def test_before' in line:
				line = line.replace("test_before", "%s_before" % case)
				f.write(line)
				n = n + 1
			elif '@pytest.mark.usefixtures("test_before")' in line:
				line = line.replace("test_before", "%s_before" % case)
				f.write(line)
				n = n + 1

			elif 'class TestTemplate' in line:
				line = line.replace("TestTemplate", "Test%s" % case.title().replace("_", ""))
				f.write(line)
				n = n + 1
			elif '@allure.story' in line:
				line = line.replace("Template", case)
				f.write(line)
				n = n + 1
			elif 'def test_template' in line:
				line = line.replace("template", case.lower())
				f.write(line)
				n = n + 1
			elif 'test_case: Template' in line:
				line = line.replace("Template", case)
				f.write(line)
				n = n + 1
			else:
				f.write(line)
				n += 1
		for i in range(n, len(source)):
			f.write(source[i])

def write_define(_path):
	yml_list = write_case_yml(_path)
	project_path = str(os.path.abspath('.').split('/bin')[0])
	test_path = project_path + '/testcase/'
	src = project_path + '/bin/script/Template_case.py'
	src_fixture = project_path + '/bin/script/Template_fixture.py'

	for case in yml_list:

		if yml_list[case] == 1:
			case_name = 'fixture_' + case + '.py'
			new_case = test_path + 'commonCase/' + case + "/"+ case_name
			mk_dir(test_path + 'commonCase/' + case)
			shutil.copyfile(test_path+"__init__.py", test_path+"commonCase/__init__.py")
			shutil.copyfile(test_path+"__init__.py", test_path+"commonCase/"+case+"/__init__.py")
			if case_name in os.listdir(test_path + "commonCase/" + case):
				pass
			else:
				write_fixture(case,src_fixture,new_case)
		else:
			case_name = 'test_' + case + '.py'
			new_case = test_path + case + '/' + case_name
			mk_dir(test_path + case)
			if case_name in os.listdir(test_path + case):
				pass
			else:
				write_case(case,src,new_case)