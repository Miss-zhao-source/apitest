import pytest
import pymysql
import requests
import logging

class Test_1_5_5_delete_role:
    def setup_class(self):
        self.url="http://127.0.0.1:8888/api/private/v1/roles/{}:id"
        self.headers={
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjUwMCwicmlkIjowLCJpYXQiOjE2NTUwOTkzNjUsImV4cCI6MTY1NTE4NTc2NX0.tlKvhMKXT_sqZeI5iiapPr4MOEZdH40hop5cTARKuiA"
        }
        print('CLASS STARTS!')

    def teardwon_class(self):
        logging.info('CLASS ENDS!')

    def setup(self):
        print('FUNCTION STARTS:')

    def teardown(self):
        print('---------------------------->FUNCTION ENDS')

    def test_delete_role(self):
        id=108
        url=self.url.format(id)
        r=requests.delete(url=url,headers=self.headers)
        logging.info(url)
        logging.info(r.json())


