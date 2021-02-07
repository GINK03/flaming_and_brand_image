import pandas as pd
import glob

def load_data(target_path_to_glob):
    tmps =[]
    for file in glob.glob(target_path_to_glob):
        tmp = pd.read_csv(file, sep="\t", error_bad_lines=False, usecols=["date", "time", "username", "tweet", "likes_count", "mentions"])
        tmp = tmp[tmp.mentions == "[]"]
        tmp = tmp[~tmp.tweet.str.contains("@") ]
        tmp = tmp[~tmp.tweet.str.contains("http") ]
        tmp.drop_duplicates(subset=["username"], inplace=True, keep="last") # １id 一票とする
        tmp.drop_duplicates(subset=["tweet"], inplace=True, keep="last") # 何度も同じ投稿するものを禁止　
        tmps.append(tmp)
        
    df = pd.concat(tmps)
    return df
