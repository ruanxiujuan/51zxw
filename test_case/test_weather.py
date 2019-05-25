import unittest
import time
import requests
import json
from time import sleep


'''
将接口测试集成到unittest，对接口进行不同参数场景的测试，设置断言，生成测试报告！

用例设计：
正常参数  传入正常参数进行测试                        返回success提示信息，city传参一致。
异常参数  传入异常参数，如参数错误，参数类型不一致等   返回Request resource not found提示信息，状态码400。
缺省参数  不参cityId                                 返回Request resource not found提示信息，状态码400。
'''

class TestWeather(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = "http://t.weather.itboy.net/api/weather/city/"
        cls.proxies = {"https": "119.254.94.93:46323"}

    def test_weather_beijing(self):
        url = self.url
        cityId = "101010100"

        r = requests.get(url=url+cityId, proxies=self.proxies, verify=False)
        result = r.json()
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))

        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "Success !")
        self.assertEqual(result['cityInfo']['city'], "北京市")

        sleep(3)

    def test_weather_param_error(self):
        url = self.url
        cityId = "8888"

        r = requests.get(url=url + cityId, proxies=self.proxies, verify=False)
        result = r.json()
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))

        self.assertEqual(result['status'], 404)
        self.assertEqual(result['message'], "Request resource not found.")

        sleep(3)

    def test_weather_no_param(self):
        url = self.url

        r = requests.get(url=url, proxies=self.proxies, verify=False)
        result = r.json()
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))

        self.assertEqual(result['status'], 404)
        self.assertEqual(result['message'], "Request resource not found.")

        sleep(3)


if __name__ == "__main__":
    unittest.main()





