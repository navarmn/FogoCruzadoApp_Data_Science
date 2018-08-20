from sklearn.base import BaseEstimator, TransformerMixin

class RemoveOutliers_lat_long(BaseEstimator, TransformerMixin):
    def __init__(self, coordinates=(-44.93, -40.81, -23.43, -20.72)):

        # State of Rio de Janeiro on map:
        # lat_min, lat_max, long_min, long_max = -44.93, -40.81, -23.43, -20.72
        self.coordinates = coordinates
        # Default size of string containing latitude and longitude
        self.str_len = 12
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        
        drop_idx = []

        for x in range(0,len(X['LATITUDE'])):
            
            # assert type(len(X['LATITUDE'].loc[x]) == str, "Data is not string"
            
            if len(X['LATITUDE'].loc[x]) > self.str_len:
                drop_idx.append(x)
        if len(drop_idx) != 0:
            dataOut = X.drop(labels=drop_idx, axis=0, inplace=False)
        return dataOut

class String2Float_lat_long(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X):
        return self

    def transform(self, X):
        X['LATITUDE'] = list(map(float, X['LATITUDE']))
        X['LONGITUDE'] = list(map(float, X['LONGITUDE']))
        return X

class GetData_lat_long(BaseEstimator, TransformerMixin):
    def __init__(self, coordinates=(-43.906927, -42.987857, -23.081902, -22.736000)):
        # The default value is a region around Rocinha
        self.coordinates = coordinates
    def fit(self, X):
        return self
    def transform(self, X):
        idx_long = (X['LONGITUDE'] >= self.coordinates[0]) & (X['LONGITUDE'] <= self.coordinates[1])
        idx_lat = (X['LATITUDE'] >= self.coordinates[2]) & (X['LATITUDE'] <= self.coordinates[3])
        idx = idx_long & idx_lat
        return X.loc[idx]