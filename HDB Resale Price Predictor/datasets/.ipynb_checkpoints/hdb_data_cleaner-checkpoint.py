import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataCleaner:

    def __init__(self, dataframe):
        self.df = dataframe

    def clean(self):
        self.clean_town()
        self.clean_floor_area()
        self.clean_storey()
        self.clean_age()
        self.clean_market_hawker()
        self.clean_commercial()
        self.clean_multistorey_carpark()
        self.clean_precinct_pavilion()
        self.clean_mall_nearest()
        self.clean_hawker_nearest()
        self.clean_food_stalls()
        self.clean_market_stalls()
        self.clean_nearest_mrt()
        self.clean_nearest_pri()
        self.clean_pri_name()
        self.clean_nearest_sec()
        self.clean_sec_name()
        self.df = self.df.dropna(axis=1)

    def clean_town(self):
        try:
            self.df = pd.get_dummies(self.df, columns=["town"], dtype=int, prefix="town", drop_first=True)
        except KeyError:
            pass

    def clean_floor_area(self):
        try:
            sc = StandardScaler()
            self.df["floor_area_sqm"] = sc.fit_transform(self.df[["floor_area_sqm"]])
        except KeyError:
            pass

    def clean_storey(self):
        try:
            sc = StandardScaler()
            self.df["mid_storey"] = sc.fit_transform(self.df[["mid_storey"]])
        except KeyError:
            pass

    def clean_age(self):
        try:
            sc = StandardScaler()
            self.df["hdb_age"] = sc.fit_transform(self.df[["hdb_age"]])
        except KeyError:
            pass

    def clean_market_hawker(self):
        try:
            self.df["market_hawker"] = self.df["market_hawker"].apply(lambda x: 1 if x == "Y" else 0)
        except KeyError:
            pass

    def clean_commercial(self):
        try:
            self.df["commercial"] = self.df["commercial"].apply(lambda x: 1 if x == "Y" else 0)
        except KeyError:
            pass

    def clean_multistorey_carpark(self):
        try:
            self.df["multistorey_carpark"] = self.df["multistorey_carpark"].apply(lambda x: 1 if x == "Y" else 0)
        except KeyError:
            pass

    def clean_precinct_pavilion(self):
        try:
            self.df["precinct_pavilion"] = self.df["precinct_pavilion"].apply(lambda x: 1 if x == "Y" else 0)
        except KeyError:
            pass

    def clean_mall_nearest(self):
        try:
            sc = StandardScaler()
            self.df["Mall_Nearest_Distance"] = sc.fit_transform(self.df[["Mall_Nearest_Distance"]])
        except KeyError:
            pass

    def clean_hawker_nearest(self):
        try:
            sc = StandardScaler()
            self.df["Hawker_Nearest_Distance"] = sc.fit_transform(self.df[["Hawker_Nearest_Distance"]])
        except KeyError:
            pass

    def clean_food_stalls(self):
        try:
            sc = StandardScaler()
            self.df["hawker_food_stalls"] = sc.fit_transform(self.df[["hawker_food_stalls"]])
        except KeyError:
            pass

    def clean_market_stalls(self):
        try:
            sc = StandardScaler()
            self.df["hawker_market_stalls"] = sc.fit_transform(self.df[["hawker_market_stalls"]])
        except KeyError:
            pass

    def clean_nearest_mrt(self):
        try:
            sc = StandardScaler()
            self.df["mrt_nearest_distance"] = sc.fit_transform(self.df[["mrt_nearest_distance"]])
        except KeyError:
            pass

    def clean_nearest_pri(self):
        try:
            sc = StandardScaler()
            self.df["pri_sch_nearest_distance"] = sc.fit_transform(self.df[["pri_sch_nearest_distance"]])
        except KeyError:
            pass

    def clean_pri_name(self):
        try:
            self.df = pd.get_dummies(self.df, columns=["pri_sch_name"], dtype=int, prefix="pri", drop_first=True)
        except KeyError:
            pass

    def clean_nearest_sec(self):
        try:
            sc = StandardScaler()
            self.df["sec_sch_nearest_dist"] = sc.fit_transform(self.df[["sec_sch_nearest_dist"]])
        except KeyError:
            pass

    def clean_sec_name(self):
        try:
            self.df = pd.get_dummies(self.df, columns=["sec_sch_name"], dtype=int, prefix="sec", drop_first=True)
        except KeyError:
            pass

    def clean_cutoff(self):
        try:
            sc = StandardScaler()
            self.df["cutoff_point"] = sc.fit_transform(self.df[["cutoff_point"]])
        except KeyError:
            pass
