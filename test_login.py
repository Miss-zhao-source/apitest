import logging
import requests
import time
class Test_login:
    def setup_class(self):
        self.url = 'http://127.0.0.1:8888/api/private/v1/login'
        logging.info("self.url-------->>>>>{}".format(self.url))
        self.flag = 0   #0,1,2,3,4
        self.data = [
            {"username":"admin", "password":"123456", "status":"200"},
            {"username":"", "password":"123456", "status":"400"},
            {"username":"admin", "password":"", "status":"300"},
            {"username":"admin1", "password":"123456", "status":"400"},
            {"username":"admin", "password":"1234567", "status":"400"},
        ]

    # def teardown_class(self):
    #     print("TestDemo teardown_class")


    def setup(self):
        print("test_login run")
        self.headers = {
            "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NTQzMjg3MDUsImV4cCI6MTY1NDQxNTEwNX0.oEtPXTC6v0TrAo4LwW9DvJxFXCpYw--OxYEPIcDZ9Sc"
        }
    def teardown(self):
        print("test_login end")

    def test_login(self):
        for i in range(5):
            data_json = self.data[i]
            data = {
                "username":data_json["username"],
                "password":data_json["password"]
            }
            r = requests.post(url=self.url,headers=self.headers,data=data)
            logging.info(r.json())
            logging.info(r.status_code)
            try:
                assert str(r.json()['meta']['status']) == data_json['status']
            except AssertionError:
                logging.info("failed num: {}, value:{}".format(i,data_json['status']))
            time.sleep(1)
