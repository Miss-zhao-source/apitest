import logging
import requests
import pytest

user_list=[
    ["",1,20,"获取管理员列表成功"],
    ["","",20, "pagenum 参数错误"],
    ["",1,"","pagesize 参数错误"]
]
class Test_1_3_1_user_list:
    def setup_class(self):
        self.url='http://127.0.0.1:8888/api/private/v1/users'
        logging.info("self.url==============={}".format(self.url))
        self.flag = 0

    def teardown_class(self):
        print('Print CLASS END')

    def setup(self):
        print('test user list start!')
        self.headers = {
            "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NTQ4MzE0NzAsImV4cCI6MTY1NDkxNzg3MH0.9If1HZ_jR6htnsIG2ftt9WnuVgmbYVXQl3biwO3NEZg"
        }

    def teardown(self):
        print('test user list end')


    @pytest.mark.parametrize('query,pagenum,pagesize,msg',user_list)
    def test_user_list(self,query,pagenum,pagesize,msg):
        url_str='?query={}&pagenum={}&pagesize={}'.format(query,pagenum,pagesize)
        r = requests.get(url=self.url+url_str, headers=self.headers)
        logging.info(r.json())
        logging.info(r.status_code)
        assert r.json()['meta']['msg']==msg




