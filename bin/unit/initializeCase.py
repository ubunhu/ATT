# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:54 PM
# @Project  : ATT
# @File     : initializeCase.py
# @explain  : 文件说明

import yaml


def ini_case(_path, case_file, case_list):
	"""
	case初始化.yml测试用例
	:param _path: case路径
	:param case_file: case名称
	:return:
	"""
	# try:
	project_list = []
	if case_list[case_file] > 1:
		for i in range(1,case_list[case_file]+1):
			with open(_path + '/' + case_file +  '_' + str(i) + '.yml', 'r', encoding="utf-8") as f:
				project_dict = yaml.load(f, Loader=yaml.FullLoader)
				project_list.append(project_dict)
	else:
		with open(_path + '/' + case_file + '_1' +'.yml', 'r', encoding="utf-8") as f:
			project_dict = yaml.load(f, Loader=yaml.FullLoader)
			project_list.append(project_dict)
	# except FileNotFoundError:
	# 		project_dict = "file dose not exsit"

	return project_list