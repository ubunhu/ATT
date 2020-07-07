# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:53 PM
# @Project  : ATT
# @File     : apiSend.py
# @explain  : 文件说明



import logging

import allure

#from bin.config import confManage
from bin.unit import apiMethod, replaceRelevance
#from bin.unit import initializeCookie
#from bin.unit import readParameter
from config.confManage import header_manage

def send_request(case_data, _path):
	"""
	封装请求
	:param data: 测试用例
	:param host: 测试host
	:param address: 接口地址
	:param relevance: 关联对象
	:param _path: case路径
	:return:
	"""
	logging.info("=" * 100)
	# request_header = data["headers"]
	# request_headers = {}
	# for i in request_header:
	#     request_headers[i["name"]]=i["value"]
	# headers = request_headers
	#header = readParameter.read_param(data["test_name"], data["headers"], _path, relevance)
	header = case_data["header"]
	# if header["cookies"] is True and header["Authorization"] is not None:
	# 	#header["Cookie"] = initializeCookie.ini_cookie()
	# 	header["Authorization"] = header_manage(relevance)
	logging.debug("请求头处理结果：%s" % header)
	parameter = case_data['params'][0]
	logging.debug("请求参数处理结果：%s" % parameter)
	try:
		host = header["Host"]
	except KeyError:
		pass
	try:
		address = case_data["url"]
	except KeyError:
		pass
	#host = confManage.host_manage(host)
	# address = replaceRelevance.replace(address, relevance)
	logging.debug("host处理结果： %s" % host)
	if not host:
		raise Exception("接口请求地址为空 %s" % data["headers"])
	logging.info("请求接口：%s" % case_data['name'])
	logging.info("请求地址：%s" % address)
	logging.info("请求头: %s" % str(header))
	logging.info("请求参数: %s" % str(parameter))
	if case_data["name"] == 'password正确':
		with allure.step("保存cookie信息"):
			allure.attach("请求接口：", address)
			allure.attach("请求地址", data["http_type"] + "://" + host + address)
			allure.attach("请求头", str(header))
			allure.attach("请求参数", str(parameter))
			apiMethod.save_cookie(header=header, address=data["http_type"] + "://" + host + address, data=parameter)

	if case_data["method"].lower() == 'post':
		logging.info("请求方法: POST")
		if 'file' in case_data.keys():
			if case_data["file"] != "":
				with allure.step("POST上传文件"):
					allure.attach(case_data['name'], "请求接口")
					allure.attach("请求地址", address)
					allure.attach("请求头", str(header))
					allure.attach("请求参数", str(parameter))

				result = apiMethod.post(header=header,
				                        address=data["http_type"] + "://" + host + address,
				                        request_parameter_type=data["parameter_type"],
				                        files=parameter,
				                        timeout=data["timeout"])
		else:
			with allure.step("POST请求接口"):
				allure.attach(case_data['name'], "请求接口：")
				allure.attach(address, "请求地址")
				allure.attach(str(header), "请求头")
				allure.attach(str(parameter), "请求参数")
			result = apiMethod.post(header=header,
			                        address=address,
			                        request_parameter_type=data["parameter_type"],
			                        data=parameter)
	elif case_data["method"].lower() == 'get':
		with allure.step("GET请求接口"):
			allure.attach(case_data['name'], "请求接口")
			allure.attach(address, "请求地址")
			allure.attach(str(header), "请求头")
			allure.attach(str(parameter), "请求参数")
			logging.info("请求方法: GET")
		result = apiMethod.get(header=header,
		                       address=address,
		                       data=parameter,)
	elif case_data["method"].lower() == 'put':
		logging.info("请求方法: PUT")
		if data["file"]:
			with allure.step("PUT上传文件"):
				allure.attach("请求接口：", str(data["test_name"]))
				allure.attach("请求地址", data["http_type"] + "://" + host + address)
				allure.attach("请求头", str(header))
				allure.attach("请求参数", str(parameter))
			result = apiMethod.post(header=header,
			                        address=data["http_type"] + "://" + host + address,
			                        request_parameter_type=data["parameter_type"],
			                        files=parameter,
			                        timeout=data["timeout"])
		else:
			with allure.step("PUT请求接口"):
				allure.attach("请求接口：", str(data["test_name"]))
				allure.attach("请求地址", data["http_type"] + "://" + host + address)
				allure.attach("请求头", str(header))
				allure.attach("请求参数", str(parameter))
			result = apiMethod.post(header=header,
			                        address=data["http_type"] + "://" + host + address,
			                        request_parameter_type=data["parameter_type"],
			                        data=parameter,
			                        timeout=data["timeout"])
	elif case_data["method"].lower() == 'delete':
		with allure.step("DELETE请求接口"):
			allure.attach("请求接口：", str(data["test_name"]))
			allure.attach("请求地址", data["http_type"] + "://" + host + address)
			allure.attach("请求头", str(header))
			allure.attach("请求参数", str(parameter))
		logging.info("请求方法: DELETE")
		result = apiMethod.get(header=header,
		                       address=data["http_type"] + "://" + host + address,
		                       data=parameter,
		                       timeout=data["timeout"])
	else:
		result = {"code": False, "data": False}
	logging.info("请求接口结果：\n %s" % str(result))
	return result