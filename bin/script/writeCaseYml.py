# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:50 PM
# @Project  : ATT
# @File     : writeCaseYml.py
# @explain  : 文件说明

import json
import logging
import os
import re
import urllib.parse

from ruamel import yaml

from bin.script.mkDir import mk_dir
from bin.script.readCsv import getTestCase

def write_open_path(i, har_path):
	with open(har_path + '/' + str(i), 'r', encoding='utf-8') as f:
		logging.debug("从%s目录下，读取文件%s" % (har_path, i))
		har_cts = json.loads(f.read())
		har_ct = har_cts[0]
		case_list = dict()
		scheme = har_ct["scheme"]
		method = har_ct["method"]
		path = har_ct["path"]
		host = har_ct["host"]
		# title = path.split("/")[-1]
		# if path[-1] == "/":
		# 	title = path.split("/")[-2]
		# else:
		# 	title = path.split("/")[-1]
		title = re.findall('(.*?).chlsj', i)
		# if "_" in title[0]:
		# 	title = title[0].split("_")
		# if len(title) > 1:
		# 	case_no = title[-1]
		# 	info_id = "test_" + title[0] + '_' + title[-1]
		# else:
		title = title[0].split("_")
		case_no = title[-1]
		info_id = "test_" + title[0] + "_" + case_no
		parameter_type = har_ct["request"]["mimeType"]
		parameter = dict()
		try:
			if method == 'POST':
				parameter_list = urllib.parse.unquote(har_ct["request"]["body"]["text"])
			else:
				parameter_list = har_ct["query"]
			# if '&' in parameter_list:
			for key in parameter_list.split("&"):
				val = key.split("=")
				parameter[val[0]] = val[1]
			# else:
			#
			#     pass
		except Exception as e:
			print(e)

		project_path = str(os.path.abspath('.').split('bin')[0])
		if "commonData" in har_path:
			case_path = project_path + '/testcase/source/commonData/' + title[0]
		else:
			case_path = project_path + '/testcase/source/' + title[0]
		mk_dir(case_path)
		request_header = har_ct["request"]["header"]["headers"]
		request_headers = {}
		for i in request_header:
			request_headers[i["name"]] = i["value"]
		response_code = har_ct["response"]["status"]
		response_boby = har_ct["response"]["body"]["text"]
		test_info = dict()
		# test_info = {'id': info_id, 'address': path, 'host': '${host}$', 'title': path.split("/")[-2]}
		test_info["id"] = info_id
		# if case_no != None:
		test_info["title"] = title[0]
		# else:
		# 	test_info["title"] = title[0]
		test_info["host"] = host
		test_info["address"] = path

		# 定义checkout
		check = dict()
		# check = {'check_type': 'json', 'expected_code': response_code}

		#检查类型
		check["check_type"] = 'json'
		check["expected_code"] = response_code
		expected_request = json.loads(response_boby)
		test_case = dict()
		test_case["test_name"] = test_info["title"]
		test_case["info"] = info_id
		test_case["http_type"] = scheme
		test_case["request_type"] = method
		test_case["parameter_type"] = parameter_type
		test_case["address"] = path
		# test_case["headers"] = {"X-Requested-With": "XMLHttpRequest"}
		test_case["headers"] = request_headers
		test_case["cookies"] = True
		test_case["timeout"] = 20
		test_case["parameter"] = title[0] + '.json'
		test_case["file"] = False
		test_case["check"] = check
		test_case["relevance"] = None
		case_list["test_info"] = test_info
		case_list["premise"] = None
		case_list["test_case"] = test_case
	return case_path, title, case_list, expected_request, check, parameter, case_no

def writting_json(title, case_path, expected_request, check, parameter, case_no):

	result_file = 'result_' + title[0] + "_" + case_no + '.json'
	# result参数大于4时，写入result.json中
	# if len(expected_request) >= 4:
	if result_file in os.listdir(case_path):
		pass
	else:
		result_list = []
		result_dicts = dict()
		with open(case_path + '/' + result_file, "w") as ff:
			# expected_request = "'result_'+ title + '.json'"
			result_dicts["test_name"] = title
			result_dicts["json"] = expected_request
			result_list.append(result_dicts)

			json.dump(result_list, ff, ensure_ascii=False, indent=4)
	if check is str == False:
		check["expected_request"] = result_file
	# if case_no != None:
	# 	param_file = case_path + '/' +  title[0] + '_' + title[-1] + '.json'
	# else:
	param_file = case_path + '/' + title[0] + "_" + case_no + '.json'
	# para参数大于等于4时，参数文件单独写入json中
	# if len(parameter) >= 4:
	if param_file in os.listdir(case_path):
		pass
	else:
		new_dicts = dict()
		new_list = []
		with open(param_file, "w") as fs:
			new_dicts["test_name"] = title
			new_dicts["parameter"] = parameter
			new_list.append(new_dicts)
			json.dump(new_list, fs, ensure_ascii=False, indent=4)


def writting_yml(case_file_list, case_path, title, case_list, case_no):
	# if case_no != None:
	# 	case_file = case_path + '/' +  title[0] + '_' + title[-1] + '.yml'
	# else:
	case_file = case_path + '/' + title[0] + "_" + case_no + '.yml'
	if case_file in os.listdir(case_path):
		pass
	else:
		with open(case_file, 'w+', encoding='utf-8') as ff:
			logging.debug("从%s目录下，写入测试文件%s" % (case_path, case_file))
			yaml.dump(case_list, ff, Dumper=yaml.RoundTripDumper)
			if title[0] in case_file_list:
				pass
			else:
				if "commonData" in case_file:
					case_file_list[title[0]] = 1
				else:
					case_file_list[title[0]] = 0
	return case_file_list


def write_case_yml(har_path):
	"""
	循环读取导出文件
	:param har_path: Charles导出文件路径
	:return:
	"""
	# har_list = os.listdir(har_path)
	har_list = [f for f in os.listdir(har_path) if not f.startswith('.')]
	case_file_list = {}
	for i in har_list:
		if 'chlsj' in i:
			case_path, title, case_list, expected_request, check, parameter, case_no = write_open_path(i, har_path)
			writting_json(title, case_path, expected_request, check, parameter, case_no)
			case_file_list = writting_yml(case_file_list, case_path, title, case_list, case_no)
		else:
			har_fixture_path = har_path + "/" + i
			har_lists = getTestCase(har_fixture_path)
			project_path = str(os.path.abspath('.').split('bin')[0])
			for case in har_lists:
				case_path = project_path + '/testcase/source/' + case["name"]
				title = list(case["name"].split(" "))
				mk_dir(case_path)
				writting_json(title, case_path, case["expect"], case["check"], case["params"], case["num"])
				case_file_list = writting_yml(case_file_list, case_path, title, case, case["num"])
	return case_file_list