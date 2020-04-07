import requests,json

def postlogin():
    url = 'http://sso.pt.gomedc.com/app/login/'
    data = {
        "userName": "chenyingjie",
        "password": "gome.1234",
        "redirectUrl": "http://falcon.pt.gomedc.com/",
        "appKey": ""
    }
    headers = {'content-type': "application/json"}
    json_data = json.dumps(data)
    r = requests.post(url, json_data, headers=headers)

    print(r.text)
    print(type(r.text))


def deleteip(snmpname):
    url = "http://falcon.pt.gomedc.com/api/endpoints"
    try:
        headers = {
            'Accept':'*/*',
            'Origin':'http://falcon.pt.gomedc.com',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Cookie': 'session=eyJvcGVuLWZhbGNvbi1jayI6ImNoZW55aW5namllOjIzZWU4YmNmMjY0MTExZWE4NGJjMjQ2ZTk2MjczNTQ0In0.EOOSyg.wu7kw9wn76v1X0H8bBKHkg63Zgo',
            # 'Content-Type' : 'multipart/form-data; boundary=--------------------------736854445577785697768593',
            'Referer':'http://falcon.pt.gomedc.com/?sign=8A2F7E58F8BAEA92E42D4F27F385225C612357673EB6DD090F785836182EBD2A75EA61F9A00627C7&_t=1577187582880'
        }
        data = {
            'endpoints[]': snmpname,
            '_r':'0.31668142293235535'
        }
        session = requests.session()
        # print(str(headers))
        resp = session.delete(url, data=data, headers=headers, verify=False)
        # print(resp.text)
        # print(resp.text.split(" "))
        # print(resp.text.split(" ")[6])
        if (int(resp.text.split(" ")[6])>0):
            # print("delete success")
            # return resp.text
            return "delete success"
        else:
            return ('Fail.' + resp.text)
    except Exception as e:
        print('Test error.', format(e))
        return ("delete_snmp fail:" + format(e))

result = deleteip('0.0.0.26;33436')
print(result)