const { Translate } = require('@google-cloud/translate').v2;

// Instantiates a client
const translate = new Translate();

const langageToCode = (language) => {
  switch (language) {
    case "Arabic":
      return "ar"
    case "Chinese":
      return "yue"
    case "English":
      return "en"
    case "French":
      return "fr"
    case "Finnish":
      return "fi"
  }
}

(async (textToTranslate, targetLanguage) => {
  // The text to translate
  //const text = 'Hello, Maria !';

  // The target language
  //const target = 'ru';

  // Translates some text into Russian
  const [translation] = await translate.translate(textToTranslate, langageToCode(targetLanguage));
  //console.log(`Text: ${text}`);
  console.log(translation);
})(process.argv[2], process.argv[3])


