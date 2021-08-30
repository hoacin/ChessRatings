import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

class MovesCountPredictor:
    def __init__(self):
        pass
    def getResults(self):
        X = pd.read_csv('Moves.csv', usecols=[0,1,2], header=None)
        y = pd.read_csv('Moves.csv', usecols=[3], header=None)
        reg = LinearRegression().fit(X,y)
        return reg
def main():
    sample_data = [[2750,2550,2015]]
    reg = (MovesCountPredictor().getResults())
    coef = reg.coef_[0]
    prediction = sum([sample_data[0][i]*coef[i] for i in range(3)])+reg.intercept_
    print(f'Manual prediction: {prediction}')
    
if __name__=='__main__':
    main()