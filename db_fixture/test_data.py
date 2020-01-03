'''from excel_optest import ExcelUtil
import sys
sys.path.append('../db_fixture')
from mysql_db import DB

#create data
datas={'addCouseSub':ExcelUtil('D:/TestData/TCcollege.xls','课程订阅').dict_data()}

def init_data():
    DB().init_data(datas)

if __name__=='__main__':
    init_data()'''