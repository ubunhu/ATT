# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/11 2:04 PM
# @Project  : ATT
# @File     : setupMain.py
# @explain  : 文件说明

import os
import subprocess
import pytest
import  os.path
from bin.script.logs import LogConfig
from bin.script.writeCase import write_define

PATH = os.path.split(os.path.realpath(__file__))[0]
xml_report_path = PATH + "/report/xml/"
html_report_path = PATH + "/report/html/"
har_path = PATH + "/data"



def invoke(md):
	output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	o = output.decode("utf-8")
	return o
if __name__ == '__main__':
	LogConfig(PATH)
	write_define(har_path)
	args = ['-s', '--alluredir', xml_report_path]
	pytest.main(args)
	#os.system(r"allure generate  /report/xml -o ./report/html")
	cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
	invoke(cmd)