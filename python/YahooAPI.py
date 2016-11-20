
# -*- coding: utf-8 -*-

import sys
import json
import urllib
import urllib.request # opener
import urllib.parse # urlencode
import http
import http.cookiejar
import sys
import io

class YahooAPI():

    def __init__(self):
        '''
        constructor
        '''
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    def getYahooAPIRequest(self):
        # create request info for http request
        # appid should be hidden when this program code is open to the public
        url = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/json/queryRanking?'
        appid = 'dj0zaiZpPURzM2R1Skk4RTN1YSZzPWNvbnN1bWVyc2VjcmV0Jng9NzA-'
        params = urllib.parse.urlencode({
            'appid':appid,
            'hits': 50,})

        try:
            # get request to the URL, and get fili-like object
            response = urllib.request.urlopen(url + params)

            # # meta data of the response
            # print(response.info())

            # read the contents of response object which is byte string with decoding
            return response.read().decode('utf8')

        except urllib.request.URLError as e:
            print (e.reason)

    def parseJSON(self, responseData):
        # jsonオブジェクトを辞書型で読み込み
        data = json.loads(responseData)
        # print(json.dumps(data, sort_keys=True, indent=4))

        # テストデータ
        tmp_data = {"temp group":{"group2":{"Eric":44, "ken":33, "John":44, "Mike":99},"group1":{"Adam":40, "David":71, "Chris":60, "Bob":74}}}
        list_tmp_data = tmp_data["temp group"]
        print(json.dumps(list_tmp_data, sort_keys=True, indent=4))

        item_list = data['ResultSet']['0']['Result']
        # print (json.dumps(item_list, sort_keys=True, indent=4))

        ranking = {}
        for k, v in item_list.items():
            try:
                rank = int(v['_attributes']['rank'])
                vector = v['_attributes']['vector']
                query = v['Query']
                ranking[rank] = [vector, query]

            except:
                if k == 'RankingInfo':
                    StartDate = v['StartDate']
                    EndDate = v['EndDate']

        print ('Start date of aggrigation : ' + StartDate)
        print ('End date of aggrigation : ' + EndDate)
        print ('-' * 40)
        ranking_keys = list(ranking.keys())
        ranking_keys.sort()
        # ranking_keys.reverse()
        for i in ranking_keys:
            print (i, ranking[i][0], ranking[i][1])

if __name__ == '__main__':
    # create instance
    obj = YahooAPI()

    responseData = obj.getYahooAPIRequest()
    obj.parseJSON(responseData)
