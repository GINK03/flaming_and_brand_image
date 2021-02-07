from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import pandas as pd
from tqdm import tqdm

def scoring(x):
    try:
        ret = classifier(x)[0]
    except Exception as exc:
        print(exc)
        return None
    if ret.get("label") == "ネガティブ":
        return -ret["score"] + 0.5
    elif ret.get("label") == "ポジティブ":
        return ret["score"] - 0.5
    else:
        None


tokenizer = AutoTokenizer.from_pretrained('daigo/bert-base-japanese-sentiment', use_fast=False)

import torch

if torch.cuda.is_available():
    classifier = pipeline('sentiment-analysis', model="daigo/bert-base-japanese-sentiment", tokenizer=tokenizer, device=0)
else:
    classifier = pipeline('sentiment-analysis', model="daigo/bert-base-japanese-sentiment", tokenizer=tokenizer)


def infer_sentiment(df: pd.DataFrame, filename, frac=0.3) -> pd.DataFrame:
    tqdm.pandas()
    tmp = df.sample(frac=frac)
    tmp["score"] = tmp.tweet.progress_apply(scoring)
    tmp.to_csv(f"../var/{filename}.csv", index=None)

    return tmp
