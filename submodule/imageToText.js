const vision = require('@google-cloud/vision');
// Creates a client
const client = new vision.ImageAnnotatorClient();

(async (fileName) => {
    // Performs text detection on the local file
    const [result] = await client.textDetection(fileName);
    console.log(result.textAnnotations[0].description)
})(process.argv[2])

/// or just 
// gcloud ml vision detect-text ../data/image2.png