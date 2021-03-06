const fs = require('fs');

// Imports the CLoud Media Translation client library
const {
    SpeechTranslationServiceClient,
} = require('@google-cloud/media-translation');

// Creates a client
const client = new SpeechTranslationServiceClient();

async function translate_from_file() {
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    const filename = 'data/audio.mp4';
    const encoding = 'linear16';
    const sourceLanguage = 'en-US';
    const targetLanguage = 'fr-FR';
    const config = {
        audioConfig: {
            audioEncoding: encoding,
            sourceLanguageCode: sourceLanguage,
            targetLanguageCode: targetLanguage,
        },
        single_utterance: true,
    };

    // First request needs to have only a streaming config, no data.
    const initialRequest = {
        streamingConfig: config,
        audioContent: null,
    };

    const readStream = fs.createReadStream(filename, {
        highWaterMark: 4096,
        encoding: 'base64',
    });

    const chunks = [];
    readStream
        .on('data', chunk => {
            const request = {
                streamingConfig: config,
                audioContent: chunk.toString(),
            };
            chunks.push(request);
        })
        .on('close', () => {
            // Config-only request should be first in stream of requests
            stream.write(initialRequest);
            for (let i = 0; i < chunks.length; i++) {
                stream.write(chunks[i]);
            }
            stream.end();
        });
    console.log("bonjour")
    const stream = client.streamingTranslateSpeech().on('data', (response) => {
        const { result, error } = response;
        console.log(error)
        if (result.textTranslationResult.isFinal) {
            console.log(
                `\nFinal translation: ${result.textTranslationResult.translation}`
            );
            console.log(`Final recognition result: ${result.recognitionResult}`);
        } else {
            console.log(
                `\nPartial translation: ${result.textTranslationResult.translation}`
            );
            console.log(`Partial recognition result: ${result.recognitionResult}`);
        }
    }).on('end', ()=>console.log('cest la fin '));
    console.log(stream)
}

translate_from_file()
