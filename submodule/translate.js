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
    default :
    // default language
      return "English"
  }
}

(async (textToTranslate, targetLanguage) => {
  // Translates some text into the targetLanguage
  const [translation] = await translate.translate(textToTranslate, langageToCode(targetLanguage));
  console.log(translation);
})(process.argv[2], process.argv[3])


