import time
import init
import logger
import pandas as pd

post_limit = 50
repeat = 300

df = pd.read_csv('assets/records.csv')
log = pd.read_csv('assets/log.csv')

sp = init.get_spotify()
client = init.get_twitter()
count = logger.count(log)

print('used: {}'.format(count))

while count < post_limit:
    track = sp.current_user_playing_track()

    if track:
        name = track['item']['name'].lower().replace(',', '')
        artist = track['item']['artists'][0]['name'].lower().replace(',', '')
        text = '{} {} dinliyoruö.'.format(artist, name)

        count = 1
        loc = logger.isin(df, text)
        if loc == -1:
            df = logger.append(df, text)
        else:
            df['count'].values[loc] += 1
            count = df['count'].values[loc]

        text += ' (dinleme sayısı: {})'.format(count)

        #client.create_tweet(text=text)
        log, printed = logger.log(log, text)
        print(printed)

        count += 1
        time.sleep(repeat)


df.to_csv('assets/records.csv', index=False)
log.to_csv('assets/log.csv', index=False)