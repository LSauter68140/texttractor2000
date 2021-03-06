(async (text) => {
    // Imports the Google Cloud client library
    const language = require('@google-cloud/language');

    // Instantiates a client
    const client = new language.LanguageServiceClient();

    // The text to analyze
    //const text = 'I hate muffin';

    const document = {
        content: text,
        type: 'PLAIN_TEXT',
    };

    // Detects the sentiment of the text
    const [result] = await client.analyzeSentiment({ document: document });
    const sentiment = result.documentSentiment;
    console.log(sentiment.score);
    //console.log(`Sentiment magnitude: ${sentiment.magnitude}`);
})(process.argv[2])