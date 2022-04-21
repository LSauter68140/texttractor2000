
from asyncio.windows_events import NULL
import os
import subprocess


def show_result():

    return {
        "the translation is cxfghjh ": 12
    }


def getTranslation(data):
  
    if(data["file"] != NULL):
        # check extension png/jpg or text
        if(os.path.exists(data["file"])):
            p = subprocess.Popen(['/usr/local/bin/node', 'submodule/imageToText.js', data["file"]], stdout=subprocess.PIPE)
            text = p.stdout.read().decode('UTF8')
        else:
            raise Exception("Unreachable file sorry")    
    if(data["text"] != NULL):
        text = data["text"]

    p = subprocess.Popen(['/usr/local/bin/node', 'submodule/translate.js', data["file"]], stdout=subprocess.PIPE)
    textTranslated = p.stdout.read().decode('UTF8')
    # translate
    # avec data['langue]

    # get text transate
    # output
    # data['outputPath']
    if(data["out"] == "text"):
        ##
        print()
    elif(data["out"] == "text"):
        print()
    else:
        raise Exception("Out format no supported or not informed")



    return show_result()


# input

# language
## output in text or audio
## text or image
# femal or mal if audio
