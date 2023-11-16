from joblib import Parallel, delayed
from tqdm import tqdm
from operator import itemgetter
import multiprocessing
import time

# def get_scores_features(combination):
#
#     global score_list
#
#     features_to_use = list(combination)
#
#     df = pd.read_csv("datasets/train.csv", low_memory=False)
#
#     X = df[features_to_use]
#
#     y = df["resale_price"]
#
#     cleaned = DataCleaner(X)
#
#     cleaned.clean()
#
#     try:
#         brain = LinRegBrain(cleaned.df, y)
#     except ValueError:
#         pass
#
#     score = brain.score
#     score_list.append({"score": score, "features": features_to_use})
#
#     return score_list
#
#
# num_cores = multiprocessing.cpu_count()
# inputs = tqdm(combinations)
#
# results = Parallel(n_jobs=num_cores)(delayed(get_scores_features)(combination) for combination in inputs)
#
# results = sorted(results, key=lambda x: x[0]['score'], reverse=True)[:100]