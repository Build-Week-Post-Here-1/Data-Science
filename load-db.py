import os
from dotenv import load_dotenv
import sqlite3
import praw

# Create db schema
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute('drop table if exists submissions')
c.execute('''create table submissions (
               subreddit text,
               title text,
               text text
             )
             ''')

# Load from Reddit
load_dotenv()
reddit = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                     client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                     user_agent='lambda/posthere1')

subreddit_count = 0
for subreddit in reddit.subreddits.popular(limit=1000):
    subreddit_count += 1
    print(subreddit_count, subreddit)
    records = []
    for submission in subreddit.top(limit=2):
        records.append(
            [subreddit.display_name, submission.title, submission.selftext, submission.subscribers])
    c.executemany('''insert into submissions
                  (subreddit, title, text, subscribers)
                  values (?, ?, ?, ?)
                  ''', records)
    conn.commit()
