import praw
from datetime import datetime
import csv
# with open('wsbData.csv','w') as csvFile:
csvFile =open('wsbData.csv', 'w')
# writer = csv.writer(csvFile, delimiter=',')

# Initialize Reddit API connection
reddit = praw.Reddit(
    client_id='o-k8HsUeNmbssImQgRy9Aw',
    client_secret='LrEr3JNVjowGLxgQajiPBlH4lIAQSg',
    user_agent='MyAwesomeRedditApp/1.0 by /u/Necessary-Donut-7119')

# Define subreddit
subreddit_name = 'wallstreetbets'
subreddit = reddit.subreddit(subreddit_name)

# Get posts from the subreddit
posts = subreddit.new(limit=5000)

header = ['date','title','content','score','numComments']
# writer.writerow(header)
# Iterate over the posts and print some information
count =0
for post in posts:
    content = post.selftext.replace(',','')
    content = content.replace('\\U','')
# Trying to disable emojiis which mess it up
    title = post.title.replace(',','')
    title = title.replace('\\U','')
    row = (f'{datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')},{title},{content},{post.score},{post.num_comments}')
    # row = [ datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),title,content,post.score,post.num_comments]
    # print(row)
    try:
        csvFile.write(row)
        #  writer.writerow(row)
    except UnicodeEncodeError as e:
        count = count +1
        print(e)
        print(row)

print(f'num error lines:{count}')
csvFile.close()