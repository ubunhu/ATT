# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 1:41 PM
# @Project  : ATT
# @File     : confRead.py
# @explain  : 文件说明



import os
from configparser import ConfigParser


class Config:
	def __init__(self):
		"""
		初始化
		"""
		self.config = ConfigParser()
		self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

		if not os.path.exists(self.conf_path):
			raise FileNotFoundError("请确保配置文件存在！")

	def set_conf(self, title, value, text):
		"""
		配置文件修改
		:param title:
		:param value:
		:param text:
		:return:
		"""
		self.config.set(title, value, text)
		with open(self.conf_path, "w+") as f:
			return self.config.write(f)

	def add_conf(self, title):
		"""
		配置文件添加
		:param title:
		:return:
		"""
		self.config.add_section(title)
		with open(self.conf_path, "w+") as f:
			return self.config.write(f)

	def read_headers(self):
		"""
		读取配置文件中host相关信息
		:return:
		"""
		self.config.read(self.conf_path, encoding='utf-8')
		headers = self.config['headers']
		return headers

	def read_email(self):
		"""
		读取配置文件中email相关信息
		:return:
		"""
		self.config.read(self.conf_path, encoding='utf-8')
		email = self.config['mail']
		return email


if __name__ == '__main__':
	cf = Config()
	print(cf.read_host())