import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class LinearRegression:
    def __init__(self):
        self.a = 0
        self.b = 0

    def fit(self, x, y):
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        self.b = sum((x - x_mean) * (y - y_mean)) / sum(np.square(x))
        self.a = y_mean - (self.b * x_mean)
        return self

    def predict(self,x):
        y_pred = self.a + (self.b * x)
        return y_pred

    def plot(self,x,y):
        sns.scatterplot(x,y)
        sns.lineplot(x=x,y = self.a+self.b*x)
        plt.show()


