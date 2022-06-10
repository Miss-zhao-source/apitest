import logging
import requests

class Test_1_3_1_user_list:
    def setup_class(self):
        self.url='http://127.0.0.1:8888/api/private/v1/users'
        logging.info("self.url==============={}".format(self.url))
        self.flag = 0
        self.data = [
            {"query":"","pagenum":1,"pagesize":20,"msg":"获取管理员列表成功"},
            {"query": "", "pagenum": '', "pagesize": 20, "msg": "pagenum 参数错误"},
            {"query": "", "pagenum": '1', "pagesize": '', "msg": "pagesize 参数错误"}
        ]

    def teardown_class(self):
        print('Print CLASS END')

    def setup(self):
        print('test user list start!')
        self.headers = {
            "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NTQ4MzE0NzAsImV4cCI6MTY1NDkxNzg3MH0.9If1HZ_jR6htnsIG2ftt9WnuVgmbYVXQl3biwO3NEZg"
        }

    def teardown(self):
        print('test user list end')

    def test_user_list(self):
        for i in range(len(self.data)):
            data_test = self.data[i]
            data = {
                "query":data_test["query"],
                "pagenum":data_test["pagenum"],
                "pagesize":data_test["pagesize"],
            }

            url_str='?query={}&pagenum={}&pagesize={}'.format(data['query'],data['pagenum'],data['pagesize'])
            r = requests.get(url=self.url+url_str, headers=self.headers, data=data)
            logging.info(r.json())
            logging.info(r.status_code)
            assert r.json()['meta']['msg']==data_test['msg']




