# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 2:00 PM
# @Project  : ATT
# @File     : readParameter.py
# @explain  : 文件说明



import json
from json import JSONDecodeError
from bin.unit.replaceRelevance import replace
from itertools import combinations

def combine(temp_list, n):
    '''根据n获得列表中的所有可能组合（n个元素为一组）'''
    temp_list2 = []
    for c in combinations(temp_list, n+1):
        temp_list2.append(c)
    return temp_list2
def check_param(data_param):
    end_list = []
    param_list = []
    for i in range(len(data_param)):
        end_list.extend(combine(data_param, i))
    for param in end_list:
        pd={}
        for p in param:
            pd[p]=data_param[p]
            #print(param_list)
            if pd not in param_list:
                param_list.append(pd)
    return param_list

def read_param(test_name, param, _path, relevance=None):
	"""
	读取用例中参数parameter
	:param test_name: 用例名称
	:param param: parameter
	:param relevance: 关联对象
	:param _path: case路径
	:param result: 全局结果
	:return:
	"""
	if isinstance(param, dict):
		param = replace(param, relevance)
	elif isinstance(param, list):
		param = replace(param, relevance)
	elif param is None:
		pass
	else:
		try:
			with open(_path + "/" + param, "r", encoding="utf-8") as f:
				data = json.load(f)
				for i in data:
					if i["test_name"][0] == test_name:
						param = i["parameter"]
						break
				if not isinstance(param, dict):
					raise Exception("未能找到用例关联的参数\n文件路径：%s\n索引：%s" % (param, _path))
				else:
					param = replace(param, relevance)
		except FileNotFoundError:
			raise Exception("用例关联文件不存在\n文件路径： %s" % param)
		except JSONDecodeError:
			raise Exception("用例关联的参数文件有误\n文件路径： %s" % param)
	#把param重新排列组合,生成所有param组合


	return param