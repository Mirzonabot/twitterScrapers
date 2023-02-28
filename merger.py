from os import listdir
from os.path import isfile, join
import pandas as pd
onlyfiles = [f for f in listdir("csvs")]
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

df.to_csv("merged_cleaned_with_unique_samplesupdated.csv")