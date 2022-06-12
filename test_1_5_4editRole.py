import logging
import requests
import pytest
import pymysql

#[108,'','','更新角色信息失败']
role=[
    [108,'aaa','','获取成功'],
    [108,'','','角色名称不能为空'],


]
class Test_1_5_4editRole:
    def setup_class(self):
        self.url = "http://127.0.0.1:8888/api/private/v1/roles/{}:id"
        self.headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NTUwMDI4MjUsImV4cCI6MTY1NTA4OTIyNX0.vtqQN-Dtu4VTkmr4qeJPTYVckW2zMJLYbhdCmWgX3mM"
        }
        print('CLASS START!!!')

    def teardown_class(self):
        print('CLASS END!!!')

    def setup(self):
        print('FUNCTION Start:')
        # 打开数据库连接
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='zrq0104',
                                  database='mydb')

        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()
        # type()
        sql = "SELECT * FROM sp_role WHERE role_name={}".format(role[0][1])
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            print(results)
        except:
            print("Error: unable to fetch data")

    def teardown(self):
        print('FUNCTION ends:')
        sql = "SELECT * FROM sp_role WHERE role_name='{}'".format(role[0][1])
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取所有记录列表
            results = self.cursor.fetchall()
            print(results)
        except:
            print("Error: unable to fetch data")

        self.db.close()

    @pytest.mark.parametrize('id,roleName,roleDesc,msg',role)
    def test_edit_role(self,id,roleName,roleDesc,msg):
        data={
            "roleName":roleName,
            "roleDesc":roleDesc,
        }
        self.url = self.url.format(id)
        r=requests.put(url=self.url,data=data,headers=self.headers)
        logging.info(self.url.format(id))
        logging.info(r.json())
        assert r.json()['meta']['msg']==msg



