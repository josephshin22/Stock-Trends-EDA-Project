import praw
from datetime import datetime
import csv

with open('wsbData.csv','w') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')

    # Initialize Reddit API connection
    reddit = praw.Reddit(
        client_id='o-k8HsUeNmbssImQgRy9Aw',
        client_secret='LrEr3JNVjowGLxgQajiPBlH4lIAQSg',
        user_agent='MyAwesomeRedditApp/1.0 by /u/Necessary-Donut-7119')

    # Define subreddit
    subreddit_name = 'wallstreetbets'
    subreddit = reddit.subreddit(subreddit_name)

    # Get posts from the subreddit
    posts = subreddit.new(limit=1000)

    header = 'date,title,content,score,numComments'
    writer.writerow(header)

    # Iterate over the posts and print some information
    for post in posts:
        content = post.selftext.replace(',','')
        title = post.title.replace(',','')
        row = f'{ datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')},{title},{content},{post.score},{post.num_comments}'
        print(row)
        try:
            writer.writerow(row)
        except UnicodeEncodeError as e:
            donothing = ''
            print(e)