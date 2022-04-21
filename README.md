# Courses Project JYU FINLAND
### Use cognitive service and create a use case

We use here mainly google cloud vision api to get text from image, to translate and then to convert or not the translated text into audio file.

We use python with flask to create a 'api' useable with postamn, and node to use google cloud vision api (not working in python on my laptop)


# Quick start


Need python 3, [CLI gcloud](https://cloud.google.com/sdk/docs/install), and node.js to start

```console

pip install Flask

git clone ttps://github.com/LSauter68140/texttractor2000/

cd texttractor2000/submodule
npm install

cd ..
python task7_flask.py 

```

Be carefull you have to change *nodePath* from **task7_api** and *dataPath* from **textToSpeech** before to start the serveur



Open postamn and create a new post query

```
http://127.0.0.1:5000/translate

```

## Example

The json for the post query

Voice can accept *FEMALE* or *MALE* only, we are working on *Non-binary*


#### Simple one : 
```json
{
    "text" : "Hello word",
    "voice" : "FEMALE",
    "language" : "Finnish"
}
```
#### With file
Can use jpg or png image

```json
{
    "file" : "path/to/image.png",
    "outputFileName" : "nameAudioOuput",
    "voice" : "FEMALE",
    "language" : "Finnish"
}

```
The api will return the path of your audio.mp3 with the translation





