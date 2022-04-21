import base64
import subprocess
import requests
from requests.structures import CaseInsensitiveDict

### put here your output folder in absolute
dataPath = ""

def language_code(language, voice):
    if(voice == 'FEMALE'):
        if(language == 'Arabic'):
            return ['ar-XA', 'ar-XA-Standard-A', 'FEMALE']
        elif(language == 'Chinese'):
            return ['yue-HK', 'yue-HK-Standard-A', 'FEMALE']
        elif(language == 'English'):
            return ['en-GB', 'en-GB-Standard-A', 'FEMALE']
        elif(language == 'French'):
            return ['fr-FR', 'fr-FR-Standard-A', 'FEMALE']
        elif(language == 'Finnish'):
            return ['fi-FI', 'fi-FI-Standard-A', 'FEMALE']
    elif (voice == 'MALE'):
        if(language == 'Arabic'):
            return ['ar-XA', 'ar-XA-Standard-B', 'MALE']
        elif(language == 'Chinese'):
            return ['yue-HK', 'yue-HK-Standard-B', 'MALE']
        elif(language == 'English'):
            return ['en-GB', 'en-GB-Standard-B', 'MALE']
        elif(language == 'French'):
            return ['fr-FR', 'fr-FR-Standard-B', 'MALE']
        elif(language == 'Finnish'):
            return ['fi-FI', 'fi-FI-Standard-B', 'MALE']
    else:
        # default return english
        return ['en-GB', 'en-GB-Standard-B', 'MALE']


def textToSpeech(text, fileName,  voice, languages):

    token = subprocess.check_output(
        ["gcloud auth application-default print-access-token"], shell=True)
    token = token.decode().rstrip("\n")
    languageCode, name, ssmlGender = language_code(languages, voice)

    params = {
        "input": {
            "text": text
        },
        "voice": {
            "languageCode": languageCode,
            "name": name,
            "ssmlGender": ssmlGender
        },
        "audioConfig": {
            "audioEncoding": "mp3"
        }
    }
    
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer {}".format(token)
    headers["Content-Type"] = "application/json; charset=utf-8;"
    url = "https://texttospeech.googleapis.com/v1/text:synthesize"

    response = requests.post(url, json=params, headers=headers)
    print(response.status_code)
    audioBase64 = response.json()

    if("audioContent" not in audioBase64 or response.status_code != 200 ):
        # error occured
        return None, audioBase64

    try:
        audioDecoded = base64.b64decode(audioBase64["audioContent"])
        realPath = '/{}.mp3'.format(
            fileName)
        f = open(realPath, "wb")
        f.write(audioDecoded)
        f.close()
    except Exception as E:
        return None, E

    return realPath, None
