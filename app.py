from AI.ResultPredictor import ResultPredictor
from AI.MovesPredictor import MovesPredictor
from flask import request
from flask import jsonify
mp=MovesPredictor()
rp=ResultPredictor()

from flask import Flask
app = Flask(__name__)

@app.route('/LengthPredict', methods=['GET'])
def length_predict():
    white = request.args.get('white', default = 2000, type = int)
    black = request.args.get('black', default = 2000, type = int)
    year = request.args.get('year', default = 2000, type = int)
    prediction = mp.predict(white,black,year)
    data = {'ExpectedHalfmoveCount': prediction[0]}
    return jsonify(data)

@app.route('/ResultPredict', methods=['GET'])
def result_predict():
    white = request.args.get('white', default = 2000, type = int)
    black = request.args.get('black', default = 2000, type = int)
    year = request.args.get('year', default = 2020, type = int)
    prediction = rp.predict(white,black,year)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30006, debug=True)
    