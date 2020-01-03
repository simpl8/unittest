#coding=utf-8
import xlrd
import xdrlib,sys
'''data=xlrd.open_workbook('d:/test.xls')
table=data.sheet_by_name("Sheet1")
print(table.row_values(0))
print(table.col_values(0))'''

class ExcelUtil:
    def __init__(self,excel_path,sheet_name):
        self.data=xlrd.open_workbook(excel_path)
        self.table=self.data.sheet_by_name(sheet_name)
        #获取第一行的值作为keys
        self.keys=self.table.row_values(0)
        #获取表中数据总行数
        self.rowNum = self.table.nrows
        #获取表中数据总列数
        self.colNum = self.table.ncols
    def dict_data(self):
        if self.rowNum<=1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s={}
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
'''if __name__=="__main__":
    excel_path=''
    sheet_name=''
    data=ExcelUtil(excel_path,sheet_name)
    #print(data.dict_data()[0])'''
    

