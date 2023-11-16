from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


class LinRegBrain:

    def __init__(self, features, target): # Take in the X and y, instantiate sk-lean lr model and fit and save as attr
        self.features = features
        self.target = target
        self.lr = LinearRegression()
        self.model = self.lr.fit(features, target)
        self.intercept = self.get_intercept()
        self.coefs = self.get_coefs()
        self.score = self.get_score()

    def get_intercept(self):
        return self.model.intercept_ # returns the intercept

    def get_coefs(self):
        coefs = {}
        cols = self.features.columns
        for n in range(len(self.model.coef_)):
            coefs[cols[n]] = self.model.coef_[n]
        return coefs # returns dictionary of coefficients, so we know which column is having what effect

    def get_score(self):
        return self.model.score(self.features, self.target) # returns r2 score
