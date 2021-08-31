from operator import indexOf
import pandas as pd
from sklearn.linear_model import LogisticRegression

class ResultPredictor:
    reg = None
    def __init__(self):
        X = pd.read_csv('Moves.csv', usecols=[0,1,2], header=None)
        y = pd.read_csv('Moves.csv', usecols=[4], header=None)
        self.reg = LogisticRegression().fit(X,y)
    def predict(self, white, black, year):
        probabilities = self.reg.predict_proba([[white,black,year]])
        classes = self.reg.classes_
        winIndex = myIndexOf(classes,'win')
        drawIndex = myIndexOf(classes,'draw')
        lossIndex = myIndexOf(classes,'lose')  
        return {'win' : probabilities[0][winIndex],'draw': probabilities[0][drawIndex],'loss': probabilities[0][lossIndex]}

def myIndexOf(classes, value):
    index = 0
    for x in classes:
        if x==value:
            return index
        index=index+1
    return -1