import requests
import time
import json
key = 'AQVNxs1dX-rXeDrGDLonmysiJTzn3zBoY5DqTM7u'
filelink = input("paste a link to the audio file in Yandex.Cloud here --> ")
POST = "https://transcribe.api.cloud.yandex.net/speech/stt/v2/longRunningRecognize"
body ={
    "config": {
        "specification": {
            "languageCode": "en-US"
        }
    },
    "audio": {
        "uri": filelink
    }
}
header = {'Authorization': 'Api-Key {}'.format(key)}
req = requests.post(POST, headers=header, json=body)
data = req.json()
print(data)
id = data['id']
while True:
    time.sleep(1)
    GET = "https://operation.api.cloud.yandex.net/operations/{id}"
    req = requests.get(GET.format(id=id), headers=header)
    req = req.json()
    if req['done']: break
    print("Not done yet...")
print("Your text:")
for chunk in req['response']['chunks']:
    print(chunk['alternatives'][0]['text'])
