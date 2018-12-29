import urllib.request
import json

url = 'http://t.weather.sojson.com/api/weather/city/101180101'
resp = urllib.request.urlopen(url)
if resp.code == 200:
    weather_json = resp.read().decode('utf-8')
    print(type(weather_json), weather_json)
    weather_data = json.loads(weather_json)
    data = weather_data['data']
    print('\n\n', data)

    today_humidity = data['shidu']
    today_pm25 = data['pm25']
    today_temperature = data['wendu']
    print(f'今日温度:{today_temperature},湿度:{today_humidity}')
