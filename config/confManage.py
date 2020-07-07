# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:40 PM
# @Project  : ATT
# @File     : confManage.py
# @explain  : 文件说明


import re
from config.confRead import Config

def header_manage(args):
	"""
	host关联配置
	:param hos:
	:return:
	"""
	try:
		# relevance_list = re.findall("\${(.*?)}\$", hos)
		# for n in relevance_list:
		# 	pattern = re.compile('\${' + n + '}\$')
		# 	host_cf = Config()
		# 	config_headers = host_cf.read_headers()
		# 	hos = re.sub(pattern, host_relevance[n], hos, count=1)
		host_cf = Config()
		config_headers = host_cf.read_headers()
		config_args=config_headers[args]
	except TypeError:
		pass
	return config_args