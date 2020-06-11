# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:55 PM
# @Project  : ATT
# @File     : initalizeCookie.py
# @explain  : 文件说明


import setupMain


def ini_cookie():
	"""
	读取cookie文件
	:return:
	"""
	file = setupMain.PATH + '/aff/data/cookie.txt'
	with open(file, 'rb') as f:
		cookie = f.read().decode()

	return cookie.strip("\n")