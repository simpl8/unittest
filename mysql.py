import pymysql

# sql 语句

#创建student表
Student = '''
    create table Student(
        StdID int primary key not null,
        StdName varchar(100) not null,
        Gender enum('M','F') not null,
        Age int 
    )
'''

# 创建 Course 表
Course = '''
    create table Course(
        CouID int primary key not null,
        CName varchar(100) not null,
        TID int not null
    )
'''

# 创建 Score 表
Score= '''
    create table Score(
        SID int primary key not null,
        StdID int not null,
        CouID int not null,
        Grade int not null
    )
'''

# 创建Teacher 表
Teacher='''
    create table Teacher(
        TID int primary key not null,
        TName varchar(100) not null
    )
'''

def connect_mysql():
    db_config = dict(host="172.190.105.64", port=3306, db="testdata_report", charset="utf8", user="testdata_report", passwd="ahKIy8PCrbsC4wQ")
    try:
        cnx = pymysql.connect(**db_config)
    except Exception as err:
        raise err
    return cnx

if __name__ == "__main__":
    sql = "create table test(id int not null);"
    cnx = connect_mysql()  # 连接mysql
    cus = cnx.cursor()     # 创建一个游标对象    try:
    try:
        cus.execute(Student)
        cus.execute(Course)
        cus.execute(Score)
        cus.execute(Teacher)
        cus.close()
        cnx.commit()
    except Exception as err:
        cnx.rollback()
        raise err
    finally:
        cnx.close()