# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:49 PM
# @Project  : ATT
# @File     : logs.py
# @explain  : 文件说明


import logging
import sys
import time

from bin.script.mkDir import mk_dir


class LogConfig:
	def __init__(self, path):
		"""
		日志配置
		:param path: 路径
		"""

		runtime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
		mk_dir(path + "/log")
		logfile = path + "/log/" + runtime + '.log'
		logfile_err = path + "/log/" + runtime + '_error.log'

		logger = logging.getLogger()
		logger.setLevel(logging.DEBUG)
		logger.handlers = []

		# 第二步，创建一个handler，用于写入全部info日志文件

		fh = logging.FileHandler(logfile, mode='a+')
		fh.setLevel(logging.DEBUG)

		# 第三步，创建一个handler，用于写入错误日志文件

		fh_err = logging.FileHandler(logfile_err, mode='a+')
		fh_err.setLevel(logging.ERROR)

		# 第四步，再创建一个handler，用于输出到控制台
		ch = logging.StreamHandler(sys.stdout)
		ch.setLevel(logging.INFO)

		# 第五步，定义handler的输出格式
		formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
		fh.setFormatter(formatter)
		fh_err.setFormatter(formatter)
		ch.setFormatter(formatter)

		# 第六步，将logger添加到handler里面
		logger.addHandler(fh)
		logger.addHandler(fh_err)
		logger.addHandler(ch)
