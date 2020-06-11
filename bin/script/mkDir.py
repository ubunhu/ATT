# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:49 PM
# @Project  : ATT
# @File     : mkDir.py
# @explain  : 文件说明



import logging
import os


def mk_dir(path):
	# 去除首位空格
	path = path.strip()
	path = path.rstrip("\\")
	path = path.rstrip("/")

	# 判断路径是否存在
	is_exists = os.path.exists(path)

	if not is_exists:
		try:
			os.makedirs(path)
		except Exception as e:
			logging.error("logs目录创建失败：%s" % e)
	else:
		# 如果目录存在则不创建，并提示目录已存在
		logging.debug("logs目录已存在：%s" % str(path))
		pass
