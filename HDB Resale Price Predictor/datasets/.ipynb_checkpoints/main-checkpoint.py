from collections import OrderedDict
import pandas as pd
import misc_func
from hdb_data_cleaner import DataCleaner
from lin_reg_brain import LinRegBrain
import json

FEATURES = ["town", "floor_area_sqm", "mid_storey", "hdb_age", "market_hawker", "commercial", "multistorey_carpark",
            "precinct_pavilion", "Mall_Nearest_Distance", "Hawker_Nearest_Distance", "hawker_food_stalls",
            "hawker_market_stalls", "mrt_nearest_distance", "pri_sch_nearest_distance",
            "pri_sch_name", "sec_sch_nearest_dist", "sec_sch_name", "cutoff_point"]

pd.options.mode.chained_assignment = None

best_score = 0
best_features = ""
counter = 0
score_dict = {}

combinations = misc_func.combos(FEATURES)

df = pd.read_csv("datasets/train.csv", low_memory=False)

for combination in combinations:

    features_to_use = list(combination)

    X = df[features_to_use]

    y = df["resale_price"]

    cleaned = DataCleaner(X)

    cleaned.clean()

    print(counter)

    try:
        brain = LinRegBrain(cleaned.df, y)
    except ValueError:
        pass

    if brain.score > best_score:
        best_score = brain.score
        score_dict[counter] = {"best_score": best_score, "best_features": features_to_use}
        print(brain.score)
        print(features_to_use)
    else:
        pass

    counter += 1


results = OrderedDict(sorted(score_dict.items(), key=lambda x: x[1]['best_score'], reverse=True))

with open("scores.json", "w") as file:
    json.dump(results, file)
