#!/usr/bin/env python


import os
import sys
import random
import django
from datetime import date


# 在当前项目中运行该python脚本
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Django_ORM.settings'
django.setup() 

from orm.models import Aritcle


def import_data():
 
    for i in [1,2,3,4,5,6,7,8,9,10]:
         Aritcle.objects.create(title = '这个是标题%s'%(i),brief_content='这个是简介',content='这个是内容我们都有一个家名字叫中国')
    return True

if __name__ == "__main__":
    if import_data():
        print('插入数据成功')