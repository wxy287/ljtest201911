import pymysql

def query(sql):
    '''
    这是数据库的查询方法
    '''
    db = pymysql.connect(host="122.51.207.203",user="root",password="123456",db="db_morning")
    cursor = db.cursor()  # 获取游标
    try:
        cursor.execute(sql)  # 执行SQL
        res = cursor.fetchall()  # 获取所有结果
        db.close()  # 关闭数据库连接
        return(res)
    except:
        print("辣鸡！sql语句写错了！")


def gaibian(sql):
    '''
    数据库的修改，新增，删除的方法
    '''
    db = pymysql.connect(host="49.233.151.159",user="root",password="123456",db="ceshi")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()  # 应用/提交
    db.close()