# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:43 PM
# @Project  : ATT
# @File     : randomlyInt.py
# @explain  : 文件说明

import random


def random_int(scope):
	"""
	获取随机整型数据
	:param scope: 数据范围
	:return:
	"""
	try:
		start_num, end_num = scope.split(",")
		start_num = int(start_num)
		end_num = int(end_num)
	except ValueError:
		raise Exception("调用随机整数失败，范围参数有误！\n %s" % str(scope))
	if start_num <= end_num:
		num = random.randint(start_num, end_num)
	else:
		num = random.randint(end_num, start_num)

	return num


if __name__ == '__main__':
	print(random_int("100,200"))