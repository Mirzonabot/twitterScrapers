#pip install snscrape
import snscrape.modules.twitter as snstwitter
import os
import pandas as pd
from datetime import datetime

all_terms = []

all_terms = list(set(all_terms))


all_tweets = []

isExist = os.path.exists("csvs/")
if not isExist:
    os.makedirs("csvs/")


def scratch_for_keyword(kw,):
    global all_tweets

    ### depending on the time zone add an extra day to both since and until

    query = "("+kw+") until:2023-02-01 since:2022-12-31 -filter:retweets"
    print("starting for >>>>>>" +  kw)
    for tweet in snstwitter.TwitterSearchScraper(query).get_items():
        ## to check what each tweet has
        # print(vars(tweet))
        # print(tweet.retweetedTweet)

        all_tweets.append([tweet.date, tweet.user.id,tweet.id,tweet.lang,tweet.rawContent,tweet.retweetCount])
    ## to back up the data save it every 20000 tweets
    if len(all_tweets) > 20000:
        df = pd.DataFrame(all_tweets, columns = ['created_at', 'author', 'id', 'lang', 'tweet', 'retweet'])
        df.to_csv("csvs/till_"+kw[1:]+".csv")
        all_tweets = []
    print("finished for >>>>>>" +  kw)

for keyword in all_terms:
    scratch_for_keyword(keyword)

    

df = pd.DataFrame(all_tweets, columns = ['created_at', 'author', 'id', 'lang', 'tweet', 'retweet'])


### to create a folder called csvs on the same level as this file

df.to_csv("csvs/till_lastt"+all_terms[-1]+".csv")

onlyfiles = [f for f in os.listdir("csvs")]
print(onlyfiles)

columns = ["data.created_at","data.author_id","data.id","data.lang","data.text","data.retweet_number"]
new_df = []
print(columns)
for i in range(len(onlyfiles)):
    onlyfiles[i] = "csvs/" + onlyfiles[i]
    df = pd.read_csv(onlyfiles[i],index_col=0)
    df.author = df.author.apply(str)
    df.id = df.id.apply(str)

    print(df.id)
    print(df.author)
    print("____________________________")
    new_df.extend(df.values.tolist())

df = pd.DataFrame(new_df,columns=columns).reindex()

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df.to_csv("scrapedat_" + str(datetime.now()) + ".csv")
        
for i in range(len(onlyfiles)):
    os.remove("csvs/"+onlyfiles[i])
os.rmdir("csvs/")