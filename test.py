# -*- coding: utf-8 -*-
# @Author   : Hyman<ubunhu@gmail.com>
# @Time     : 2020/6/12 4:43 PM
# @Project  : ATT
# @File     : test.py
# @explain  : 文件说明
import  os,requests
case_path = os.path.split(os.path.realpath(__file__))[0]
# print([f for f in os.listdir(case_path) if not f.startswith('.')])
import hashlib
pwd = "Aa123456"
num = "16601166167"
token = "ed63e7b6b3cf45c2a4beac136b0f7bc6"
#加密后：AA98F2DDA4C09738D2815759A12215B4

def md5(data):
	hash = hashlib.md5(data.encode("utf-8"))
	pwd_md5 = hash.hexdigest()
	return pwd_md5.upper()

#md5加密转大写
pwd_md5 = md5(pwd)
#拼接手机号
pwd_md5 = pwd_md5+num
#md5加密转大写
pwd_md5 = md5(pwd_md5)
#拼接toekn
pwd_md5 =  token + pwd_md5
#md5加密大写
pwd_md5 = md5(pwd_md5)

print('MD5加密前为 ：' + pwd)
print('MD5加密后为 ：' + pwd_md5)
