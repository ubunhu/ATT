# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/12 11:55 AM
# @Project  : ATT
# @File     : readCsv.py
# @explain  : 文件说明

import csv
def getTestCase(filename):
	#filename = "testcase.csv"
	testCase = []
	key = None
	with open(filename) as f:
		reader = csv.reader(f)

		for row in reader:
			if row[0] == "id":
				key = row
			else:
				testCase.append(dict(zip(key,row)))
	for case in testCase:
		case_header = case["header"].split(",")
		case_params = case["params"].split(",")
		case_expect = case["expect"].split(",")
		header = {}
		params = {}
		expect = {}
		for iterm_h in case_header:
			iterm_h = iterm_h.split(":")
			header[iterm_h[0]] = iterm_h[1]
		for iterm_p in case_params:
			iterm_p = iterm_p.split(":")
			params[iterm_p[0]] = iterm_p[1]
		for iterm_e in case_expect:
			iterm_e = iterm_e.split(":")
			expect[iterm_e[0]] = iterm_e[1]
		case["header"] = header
		case["params"] = params
		case["expect"] = expect

	#testModel = {}
	#for model in testCase:
		# if case["name"] in testCase:
		# 	case["num"] += 1
		# else:
		# 	case["num"] = 1
	return testCase