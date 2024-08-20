import pandas as pd
from datetime import datetime, timedelta

def isin(df, text):
    loc = -1

    for i in range(df.shape[0]):
        if df['prompt'].values[i] == text:
            loc = i
            break

    return loc


def append(df, text):
    sub = {'prompt': text, 'count': 1}
    sub = pd.DataFrame([sub])
    df = pd.concat([df, sub], ignore_index=True)

    return df


def count(df):
    df['time'] = pd.to_datetime(df['time'])
    cutoff = datetime.now() - timedelta(hours=24)
    sub = df[df['time'] >= cutoff]
    return sub.shape[0]


def log(df, text):
    now = str(datetime.now())
    sub = {'output': text, 'time': now}
    sub = pd.DataFrame([sub])
    df = pd.concat([df, sub], ignore_index=True)

    return df, '{},{}'.format(text, now)