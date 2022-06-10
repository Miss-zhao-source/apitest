import logging
import requests
import time
class Test_add:
    def setup_class(self):
        self.url = 'http://127.0.0.1:8888/api/private/v1/users'
        logging.info("self.url-------->>>>>{}".format(self.url))
        self.flag = 0   #0,1,2,3,4
        self.data = [
            {"username":"zrq1", "password":"123456", "email":"8841", "mobile":"1303588", "status":"201"},
            {"username":"zrq2", "password":"123456", "email":"", "mobile":"1303588", "status":"201"},
            {"username": "zrq3", "password": "123456", "email": "1", "mobile": "", "status": "201"},
            {"username": "zrq3", "password": "123456", "email": "1", "mobile": "", "status": "400"},
            {"username": "zrq4", "password": "", "email": "1", "mobile": "", "status": "400"},
        ]

    # def teardown_class(self):
    #     print("TestDemo teardown_class")


    def setup(self):
        print("test_login run")
        self.headers = {
            "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NTQ4MjkyMTIsImV4cCI6MTY1NDkxNTYxMn0.bGMyQedl1YmDuGQKfvRYyr3R8O3JcBiXoT4r4m8YhtM"
        }
    def teardown(self):
        print("test_add end")

    def test_login(self):
        for i in range(5):
            data_json = self.data[i]
            data = {
                "username":data_json["username"],
                "password":data_json["password"],
                "email":data_json["email"],
                "mobile":data_json["mobile"],
            }
            r = requests.post(url=self.url,headers=self.headers,data=data)
            logging.info(r.json())
            logging.info(r.status_code)
            assert str(r.json()['meta']['status']) == data_json['status']
            time.sleep(1)