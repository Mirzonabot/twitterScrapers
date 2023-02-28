from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

op = webdriver.ChromeOptions()
op.add_argument('headless')
op.add_argument('window-size=1200x600')

## for optimization
driver = webdriver.Chrome(options=op)

## for debugging
# driver = webdriver.Chrome()


####add keywords here
all_terms = []

driver.get("https://twitter.com/")
print(driver.title)

def search_word(search_query):
    search_query = search_query + " until:2023-02-02"
    next_button = driver.find_element(By.XPATH,"//a[@aria-label='Twitter']")

    next_button.click()

    sleep(1)
    search = driver.find_element(By.XPATH,"//input[@placeholder='Search Twitter']")
    search.send_keys(search_query)
    search.send_keys(Keys.ENTER)

    sleep(1)
    latest = driver.find_element(By.XPATH,"//span[contains(text(),'Latest')]")
    latest.click()
all_tweets = []


def print_tweet(tweets,authors, created_at,retweets):

    for (tweet, author, creat_date,retweet_el) in zip(tweets, authors, created_at,retweets):
        language = tweet.get_attribute("lang")
        tweet_id = tweet.get_attribute("id")
        tweet_text = tweet.text
        retweet = retweet_el.get_attribute("aria-label")
        tweet_author = author.get_attribute("id")
        tweet_time = creat_date.get_attribute("datetime")
        row = [tweet_time,tweet_author,tweet_id,language,tweet_text,retweet]
        all_tweets.append(row)

import datetime
last_time = None

till = datetime.datetime(2023, 1, 30, 0, 0)
till

for term in all_terms:
    search_word(term)
    while True:
        try:
            autors = driver.find_elements(By.XPATH,"//div[@aria-label='Timeline: Search timeline']/div/div/div/div/div/article/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div")
            created_at = driver.find_elements(By.XPATH,"//div[@aria-label='Timeline: Search timeline']/div/div/div/div/div/article/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[3]/a/time")
            tweets = driver.find_elements(By.XPATH,"//div[@aria-label='Timeline: Search timeline']/div/div/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div/div[@lang]")
            retweet = driver.find_elements(By.XPATH,"//div[@aria-label='Timeline: Search timeline']/div/div/div/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div")
            

            last_element = created_at[-1]
            print_tweet(tweets,autors,created_at,retweet)
            driver.execute_script("arguments[0].scrollIntoView();",last_element)
            last_time = datetime.datetime.strptime(last_element.get_attribute("datetime").split("T")[0], "%Y-%m-%d")
            sleep(.2)
            if last_time < till:
                print("Finished!!!!!!!!1")
                break

        except Exception as e:
            pass

import pandas as pd

df = pd.DataFrame(all_tweets, columns = ['data.created_at', 'data.author_', 'data.id', 'data.lang', 'data.tweet', 'data.num_retweet'])
df.to_csv("sample_sdf.csv")