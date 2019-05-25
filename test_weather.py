import requests
import json


def test_weadther():
    url = "http://t.weather.itboy.net/api/weather/city/"
    city_code = "101010100"   # 北京
    r = requests.get(url=url + city_code)
    result = json.dumps(r.json(), ensure_ascii=False, sort_keys=True, indent=2)
    print(result)


if __name__ == "__main__":
    t = test_weadther()




