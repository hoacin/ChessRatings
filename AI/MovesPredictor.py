import pandas as pd
from sklearn.linear_model import LinearRegression

class MovesPredictor:
    reg = None
    def __init__(self):
        X = pd.read_csv('Moves.csv', usecols=[0,1,2], header=None)
        y = pd.read_csv('Moves.csv', usecols=[3], header=None)
        self.reg = LinearRegression().fit(X,y)
    def predict(self, white, black, year):
        coef = self.reg.coef_[0]
        prediction = white*coef[0]+black*coef[1]+year*coef[2]+self.reg.intercept_
        return prediction
    def getCoef(self):
        return self.reg.coef_[0]
    def getIntercept(self):
        return self.reg.intercept_