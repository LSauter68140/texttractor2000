const vision = require('@google-cloud/vision');
// Creates a client
const client = new vision.ImageAnnotatorClient();

//const fileName = '../data/image.png';


(async (fileName) => {
    // Performs text detection on the local file
    const [result] = await client.textDetection(fileName);
    const detections = result.textAnnotations;
    ///console.log('Text:');
    //detections.forEach(text => console.log(text));
    console.log(detections[0].description)
})(process.argv[2])



/// or just 
// gcloud ml vision detect-text ../data/image2.png