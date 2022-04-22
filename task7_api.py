import os
import subprocess

from submodule.textToSpeech import textToSpeech

### work only for linux or macOs, if you se windows change it before to start
nodePath = '/usr/local/bin/node'

def getTranslation(data):

    # if we have file and text key in data dic, we use file in priority
    if("file" in data):
        # check extension png/jpg or text
        if(os.path.exists(data["file"]) and data["file"].split(".")[-1].lower() in ["jpg", "png", "jpeg"]):
            # get the image text in to text
            p = subprocess.Popen(
                [nodePath, 'submodule/imageToText.js', data["file"]], stdout=subprocess.PIPE)
            textToTranslate = p.stdout.read().decode('UTF8')
        else:
            return None, "Unreachable file sorry"
    elif("text" in data):
        textToTranslate = data["text"]
    else:
        return None, "Miss 'text or 'file' attribut in the body"

    # ## get feeling 
    # p = subprocess.Popen(
    #             [nodePath, 'submodule/imageToText.js', textToTranslate], stdout=subprocess.PIPE)
    # sentimentScore =  p.stdout.read().decode('UTF8')

    if("language" not in data):
        return None, "Miss 'language' or 'voice' attribut in the body"

    # translate the text
    p = subprocess.Popen([nodePath, 'submodule/translate.js',
                         textToTranslate, data['language']], stdout=subprocess.PIPE)
    textTranslated = p.stdout.read().decode('UTF8')

    ## get the text in to speech if needed
    if("outputFileName" in data and "voice" in data):
        path, err = textToSpeech(
            textTranslated, data['outputFileName'],  data['voice'], data['language'])    
        if (err != None):
            ## errors occured in text to Speech
            return None, err
    else:
        path = None
        outText = textTranslated

    ## return a resp for flask app
    if(path == None):
        return {
            "Orignal Text": textToTranslate,
            "Translation": outText
        }, None
    else:
        return {
            "Orignal Text": textToTranslate,
            "File path to the audio translation": path
        }, None
