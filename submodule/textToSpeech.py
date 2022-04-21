import base64
import requests
from requests.structures import CaseInsensitiveDict

token = "ya29.c.b0AXv0zTMeYg3HmSVr2k_PJgF8Xohx6goZKyUjkZiPYXNV4VML0rI6VD8TttvGCjTclNtdHDC7zoehPmmYxgcrPPGgO-oiMvosG3pJZ0LefVG9VyS1roSR5Qzk0s4dPRvoty_zAyQVN6MlfQpe02I-RpDIY8OnVEovWhE5Gb0uXstg96FOGmDgAwh6RgdbAOTl3IN6QT9DjcKUg0NDAl1R-BJJ6KuT5uM........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................"

params = {
  "input":{
    "text":"Android is a mobile operating system developed by Google, based on the Linux kernel and designed primarily for touchscreen mobile devices such as smartphones and tablets."
  },
  "voice":{
    "languageCode":"en-gb",
    "name":"en-GB-Standard-A",
    "ssmlGender":"FEMALE"
  },
  "audioConfig":{
    "audioEncoding":"MP3"
  }
}

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer {}".format(token)
headers["Content-Type"] = "application/json; charset=utf-8;"
url = "https://texttospeech.googleapis.com/v1/text:synthesize"

response = requests.post(url, json=params, headers=headers)
print(response.status_code)


audioBase64 = response.json()["audioContent"]
audioDecoded = base64.b64decode(audioBase64)
f = open("../data/audioFile.mp3", "wb")
f.write(audioDecoded)
f.close()
print("en theorie ca marche")

