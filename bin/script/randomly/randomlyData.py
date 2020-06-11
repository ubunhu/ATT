# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:41 PM
# @Project  : ATT
# @File     : randomlyData.py
# @explain  : 文件说明

import random


def choice_data(data):
	"""
	获取随机整型数据
	:param data: 数组
	:return:
	"""
	_list = data.split(",")
	num = random.choice(_list)
	return num


if __name__ == "__main__":
	print(choice_data("400,100,2"))