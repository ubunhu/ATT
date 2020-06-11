# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:42 PM
# @Project  : ATT
# @File     : randomlyHash.py
# @explain  : 文件说明


import hashlib


def md5(data):
	"""
	md5加密
	:param data:想要加密的字符
	:return:
	"""
	m1 = hashlib.md5()
	m1.update(data.encode("utf-8"))
	data = m1.hexdigest()
	return data


if __name__ == '__main__':
	print(md5("ssss"))