

from fileinput import filename
import os
import subprocess
from submodule.textToSpeech import textToSpeech


def getTranslation(data):

    if("file" in data):
        # check extension png/jpg or text
        if(os.path.exists(data["file"])):
            p = subprocess.Popen(
                ['/usr/local/bin/node', 'submodule/imageToText.js', data["file"]], stdout=subprocess.PIPE)
            textToTranslate = p.stdout.read().decode('UTF8')
        else:
            raise Exception("Unreachable file sorry")
    if("text" in data):
        textToTranslate = data["text"]

    p = subprocess.Popen(['/usr/local/bin/node', 'submodule/translate.js',
                         textToTranslate, data['language']], stdout=subprocess.PIPE)
    textTranslated = p.stdout.read().decode('UTF8')
    print("test ::")
    print(textTranslated)
    if("outputFileName" in data ):
        path = textToSpeech(textTranslated, data['outputFileName'],  data['voice'], data['language'])
    else:
        path = None
        outText = textTranslated

    if(path == None):
        return {
            "Orignal Text": textToTranslate,
            "Translation": outText
        }
    else:
        return {
            "Orignal Text": textToTranslate,
            "File path to the audio translation": path
        }


# input

# language
## output in text or audio
## text or image
# femal or mal if audio
