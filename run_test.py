#coding=utf-8
import time, sys
sys.path.append('./testcase')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

test_dir= "F:/AutoTestting/testcase"
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

def ReportBulid():
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename='F:/AutoTestting/report/'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title="通财学院测试报告",description='通财学院')
    runner.run(discover)
    fp.close()


if __name__=="__main__":
    ReportBulid()
