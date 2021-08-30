from Train.MovesPredictor import MovesPredictor
from flask import request
from flask import jsonify
mp=MovesPredictor()

from flask import Flask
app = Flask(__name__)

@app.route('/LengthPredict', methods=['GET'])
def length_predict():
    white = request.args.get('white', default = 2000, type = int)
    black = request.args.get('black', default = 2000, type = int)
    year = request.args.get('year', default = 2000, type = int)
    prediction = mp.predict(white,black,year)
    data = {'AverageMoveCount': prediction[0]}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30006, debug=True)
    