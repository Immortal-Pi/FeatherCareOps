import os
from  flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from FeatherCareOps.utils.common import decodeImage
from FeatherCareOps.pipeline.predict import PredictionPipeline

os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app=Flask(__name__)
CORS(app) # allows app to handle requests from different domains


class ClientApp:
    def __init__(self):
        self.filename='inputImage.png'
        self.classifier=PredictionPipeline(self.filename)


@app.route('/',methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train',methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system('python main.py')
    return 'Training done successfully!'

@app.route('/predict',methods=['POST'])
@cross_origin()
def predictRoute():
    image=request.json['image']
    decodeImage(image,clApp.filename)
    results=clApp.classifier.predict()
    return jsonify(results)


if __name__=='__main__':
    clApp=ClientApp()
    # app.run(host='0.0.0.0',port=8080,debug=True) # local host
    # app.run(host='0.0.0.0',port=8080,debug=True) # for AWS
    app.run(host='0.0.0.0',port=80,debug=True) # for Azure