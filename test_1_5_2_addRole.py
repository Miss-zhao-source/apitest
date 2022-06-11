import logging
import requests
import pytest
import pymysql

roleList=[
    ["admin2","admin2Desc","创建成功"],
    ["","admin2Desc","角色名称不能为空"],
    ["admin2","","创建成功"],
    ["admin2","admin2Desc","创建成功"]
]

class Test_1_5_2_addRole:
    def setup_class(self):
        self.url="http://127.0.0.1:8888/api/private/v1/roles"
        self.headers={
            "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NTQ5MzY2MTYsImV4cCI6MTY1NTAyMzAxNn0.zPUGKVG-60h7iSQzEzaLDVFBvg8kJkEEAi7Qu6kbbQE"
        }
        logging.info("self.url==============={}".format(self.url))
        print('CLASS START!')

    def teardown_class(self):
        print('CLASS END!')

    def setup(self):
        # 打开数据库连接
        self.db = pymysql.connect(host='localhost',
                             user='root',
                             password='zrq0104',
                             database='mydb')

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    def teardown(self):
        # SQL 删除语句
        sql = "DELETE FROM sp_role WHERE role_name='{}'".format(roleList[0][0])
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

        # 关闭连接
        self.db.close()


    @pytest.mark.parametrize('roleName,roleDesc,msg',roleList)
    def test_addRole(self,roleName,roleDesc,msg):
        data={
            'roleName':roleName,
            'roleDesc':roleDesc
        }
        r=requests.post(url=self.url,headers=self.headers,data=data)
        logging.info(r.json())
        print('r.json():',r.json()['meta']['msg'])
        assert r.json()['meta']['msg']==msg


