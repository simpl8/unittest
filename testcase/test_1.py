#coding=utf-8
import time
import requests
import unittest
from excel_optest import ExcelUtil
import json
import os, sys
from HTMLTestRunner import HTMLTestRunner


class Generalist(unittest.TestCase):
    def setUp(self):
        self.base_url_1="http://10.10.13.211:19188/api/addCouseSub"
        self.base_url_2="http://10.10.13.211:19188/api/addRead"
        self.base_url_3="http://10.10.13.211:19188/api/allCouses"
        self.base_url_4="http://10.10.13.211:19188/api/generalistEnter"
        self.base_url_5="http://10.10.13.211:19188/api/getCouseInfoDetail"
        self.base_url_6="http://10.10.13.211:19188/api/getGeneralistFrontPage"
        self.base_url_7="http://10.10.13.211:19188/api/getSubCouseList"
        self.base_url_8="http://10.10.13.211:19188/api/mineCouses"
        self.base_url_9="http://10.10.13.211:19188/api/moreRecommList"
        self.base_url_10="http://10.10.13.211:19188/api/searchCouseList"
        self.base_url_11="http://10.10.13.211:19188/api/subCouseInfo"
#addCouseSub
    #入参都为空
    def test_addCouseSub_0(self):
        
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程订阅').dict_data()[0]
        r=requests.post(self.base_url_1,params=data)
        result=r.json()          
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'订阅传入参数异常,更新失败')
    #couseId为空
    def test_addCouseSub_1(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程订阅').dict_data()[1]
        r=requests.post(self.base_url_1,params=data)
        result=r.json()    
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'订阅传入参数异常,更新失败')
    #commAccount为空
    def test_addCouseSub_2(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程订阅').dict_data()[2]
        r=requests.post(self.base_url_1,params=data)
        result=r.json() 
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'订阅传入参数异常,更新失败')
    #参数正确已订阅
    def test_addCouseSub_3(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程订阅').dict_data()[3]
        r=requests.post(self.base_url_1,params=data)
        result=r.json()
        self.assertEqual(result['code'], '1')
        self.assertEqual(result['msg'],'已经订阅该课程')
    #参数正确订阅成功
    def test_addCouseSub_4(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程订阅').dict_data()[4]
        r=requests.post(self.base_url_1,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'订阅成功')
#addRead
    #入参都为空
    def test_addRead_0(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程阅读更新').dict_data()[0]
        r=requests.post(self.base_url_2,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'阅读量更新传入参数异常,更新失败')
    #couseId有入参
    def test_addRead_1(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程阅读更新').dict_data()[1]
        r=requests.post(self.base_url_2,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'阅读量更新传入参数异常,更新失败')
    #commAccount有入参
    def test_addRead_2(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程阅读更新').dict_data()[2]
        r=requests.post(self.base_url_2,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'阅读量更新传入参数异常,更新失败')
    #subCouseId有入参
    def test_addRead_3(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程阅读更新').dict_data()[3]
        r=requests.post(self.base_url_2,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'阅读量更新传入参数异常,更新失败')
    #couseId为空
    def test_addRead_4(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程阅读更新').dict_data()[4]
        r=requests.post(self.base_url_2,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'阅读量更新传入参数异常,更新失败')
    #commAccount为空
    def test_addRead_5(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程阅读更新').dict_data()[5]
        r=requests.post(self.base_url_2,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'阅读量更新传入参数异常,更新失败')
    #subCouseId为空
    def test_addRead_6(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程阅读更新').dict_data()[6]
        r=requests.post(self.base_url_2,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'阅读量更新传入参数异常,更新失败')
    #参数正常
    def test_addRead_7(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程阅读更新').dict_data()[7]
        r=requests.post(self.base_url_2,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'阅读量更新成功')
#allCouse
    #无入参
    def test_allCouse_0(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','所有课程').dict_data()[0]
        r=requests.get(self.base_url_3,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #couseType有参
    def test_allCouse_1(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','所有课程').dict_data()[1]
        r=requests.get(self.base_url_3,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #couseTitle有参
    def test_allCouse_2(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','所有课程').dict_data()[2]
        r=requests.get(self.base_url_3,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #都有入参
    def test_allCouse_3(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','所有课程').dict_data()[3]
        r=requests.get(self.base_url_3,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
#generalistEnter
    #commAccount为空
    def test_generalistEnter_0(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','客户端入口').dict_data()[0]
        r=requests.get(self.base_url_4,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #commAccount正常
    def test_generalistEnter_1(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','客户端入口').dict_data()[1]
        r=requests.get(self.base_url_4,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
#getCouseInfoDetail
    #couseId为空
    def test_getCouseInfoDetail_0(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','大课程详情').dict_data()[0]
        r=requests.get(self.base_url_5,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #commAccount为空
    def test_getCouseInfoDetail_1(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','大课程详情').dict_data()[1]
        r=requests.get(self.base_url_5,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #入参都有，但是不正确
    def test_getCouseInfoDetail_2(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','大课程详情').dict_data()[2]
        r=requests.get(self.base_url_5,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
#getGeneralistFrontPage
    #入参为空
    def test_getGeneralistFrontPage_0(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[0]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #theme有入参
    def test_getGeneralistFrontPage_1(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[1]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #commAccount有入参
    def test_getGeneralistFrontPage_2(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[2]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #version有入参
    def test_getGeneralistFrontPage_3(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[3]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #platform有入参
    def test_getGeneralistFrontPage_4(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[4]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #theme&commAccount有入参
    def test_getGeneralistFrontPage_5(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[5]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #commAccount&version有入参
    def test_getGeneralistFrontPage_6(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[6]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #version&platform有入参
    def test_getGeneralistFrontPage_7(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[7]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #platform无入参       
    def test_getGeneralistFrontPage_8(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[8]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #version无入参
    def test_getGeneralistFrontPage_9(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[9]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #commAccount无入参
    def test_getGeneralistFrontPage_10(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[10]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #theme无入参
    def test_getGeneralistFrontPage_11(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[11]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #都有入参
    def test_getGeneralistFrontPage_12(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[12]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    def test_getGeneralistFrontPage_13(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[13]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    def test_getGeneralistFrontPage_14(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[14]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    def test_getGeneralistFrontPage_15(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[15]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    def test_getGeneralistFrontPage_16(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[16]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    def test_getGeneralistFrontPage_17(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[17]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    def test_getGeneralistFrontPage_18(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','首页').dict_data()[18]
        r=requests.get(self.base_url_6,params=data)
        result=r.json()
        #print(r.url)
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
#getSubCouseList
    #没有入参
    def test_getSubCouseList_0(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','小课程').dict_data()[0]
        r=requests.get(self.base_url_7,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #stepCode有入参
    def test_getSubCouseList_1(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','小课程').dict_data()[1]
        r=requests.get(self.base_url_7,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #couseId有入参
    def test_getSubCouseList_2(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','小课程').dict_data()[2]
        r=requests.get(self.base_url_7,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #commAccount有入参
    def test_getSubCouseList_3(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','小课程').dict_data()[3]
        r=requests.get(self.base_url_7,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #都有入参
    def test_getSubCouseList_4(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','小课程').dict_data()[4]
        r=requests.get(self.base_url_7,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #stepCode无入参
    def test_getSubCouseList_5(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','小课程').dict_data()[5]
        r=requests.get(self.base_url_7,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #couseId无入参
    def test_getSubCouseList_6(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','小课程').dict_data()[6]
        r=requests.get(self.base_url_7,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #commAccount无入参
    def test_getSubCouseList_7(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','小课程').dict_data()[7]
        r=requests.get(self.base_url_7,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
#mineCouse
    #commAccount入参为空
    def test_mineCouse_0(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','我的课程').dict_data()[0]
        r=requests.get(self.base_url_8,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #commAccount入参正确
    def test_mineCouse_1(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','我的课程').dict_data()[1]
        r=requests.get(self.base_url_8,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
#moreRecommList
    #无需入参
    def test_moreRecommList_0(self):
        #data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','更多推荐课程').dict_data()[0]
        r=requests.get(self.base_url_9)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
#searchCouseList
    #searchTitle入参为空
    def test_searchCouseList_0(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程搜索').dict_data()[0]
        r=requests.get(self.base_url_10,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
    #searchTitle入参正确
    def test_searchCouseList_1(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','课程搜索').dict_data()[1]
        r=requests.get(self.base_url_10,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')
#subCouseInfo
    #入参为空
    def test_subCouseInfo_0(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','子课程详情').dict_data()[0]
        r=requests.get(self.base_url_11,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'传入参数异常')
    #subCouseId为空
    def test_subCouseInfo_1(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','子课程详情').dict_data()[1]
        r=requests.get(self.base_url_11,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'传入参数异常')
    #commAccount为空
    def test_subCouseInfo_2(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','子课程详情').dict_data()[2]
        r=requests.get(self.base_url_11,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'查询失败')
    #couseId为空
    def test_subCouseInfo_3(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','子课程详情').dict_data()[3]
        r=requests.get(self.base_url_11,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'传入参数异常')
    #souCouseId有入参
    def test_subCouseInfo_4(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','子课程详情').dict_data()[4]
        r=requests.get(self.base_url_11,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'传入参数异常')
    #commAccount有入参
    def test_subCouseInfo_5(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','子课程详情').dict_data()[5]
        r=requests.get(self.base_url_11,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'传入参数异常')
    #couseId有入参
    def test_subCouseInfo_6(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','子课程详情').dict_data()[6]
        r=requests.get(self.base_url_11,params=data)
        result=r.json()
        self.assertEqual(result['code'], '-1')
        self.assertEqual(result['msg'],'传入参数异常')
    #入参正确
    def test_subCouseInfo_7(self):
        data=ExcelUtil('F:/AutoTestting/TestData/TCcollege.xls','子课程详情').dict_data()[7]
        r=requests.get(self.base_url_11,params=data)
        result=r.json()
        self.assertEqual(result['code'], '0')
        self.assertEqual(result['msg'],'查询成功')

if __name__=='__main__':
    #test_data.init_data()
    unittest.main()
    
  