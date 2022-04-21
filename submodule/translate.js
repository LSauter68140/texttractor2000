const {Translate} = require('@google-cloud/translate').v2;

// Instantiates a client
const translate = new Translate();

(async (textToTranslate, targetLanguage)=> {
  // The text to translate
  //const text = 'Hello, Maria !';

  // The target language
  //const target = 'ru';

  // Translates some text into Russian
  const [translation] = await translate.translate(textToTranslate, targetLanguage);
  //console.log(`Text: ${text}`);
  console.log(translation);
})(process.argv[2], process.argv[3])