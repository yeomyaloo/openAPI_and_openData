import requests, xmltodict,json


url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'

params = {
    'serviceKey' :'서비스키',
    'pageNo' : '1',
    'numOfRows' : '10',
    'startCreateDt' : '20220801',
    'endCreateDt' : '20220809' }

response = requests.get(url, params = params)
content = response.content
dic = xmltodict.parse(content)
jsonString = json.dumps(dic['response']['body']['items'])
json_object = json.loads(jsonString)


for i in json_object['item']:
    print(f"날짜: {i['createDt']}")
    print(f"감염자 수: {i['decideCnt']}")
