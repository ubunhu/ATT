# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:42 PM
# @Project  : ATT
# @File     : randomlyFloat.py
# @explain  : 文件说明

import random


def random_float(data):
	"""
	获取随机整型数据
	:param data: 数组
	:return:
	"""
	try:
		start_num, end_num, accuracy = data.split(",")
		start_num = int(start_num)
		end_num = int(end_num)
		accuracy = int(accuracy)
	except ValueError:
		raise Exception("调用随机整数失败，范围参数或精度有误！\n小数范围精度 %s" % data)

	if start_num <= end_num:
		num = random.uniform(start_num, end_num)
	else:
		num = random.uniform(end_num, start_num)
	num = round(num, accuracy)
	return num


if __name__ == '__main__':
	print(random_float("200,100,5"))