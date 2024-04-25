import praw
from datetime import datetime,timezone,timedelta
import csv


# Open the CSV file with encoding to handle Unicode characters
with open('wsbData.csv', 'w', newline='', encoding='utf-8') as csvFile:
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
    # posts = subreddit.new(limit=5000)
    posts = subreddit.search(sort='new', syntax='lucene', time_filter='all', limit=None)



    header = ['date', 'title', 'content', 'score', 'numComments']
    writer.writerow(header)

    # Iterate over the posts and write some information to the CSV file
    count = 0
    count1=0
    for post in posts:
        # Remove commas from content
        content = post.selftext.replace(',', '')
        # Remove commas from title
        title = post.title.replace(',', '')
        row = [
            datetime.fromtimestamp(post.created_utc, timezone.utc).strftime('%Y-%m-%d'),
            title,
            content,
            post.score,
            post.num_comments
        ]
        try:
            writer.writerow(row)
            # print(row)
            # count1 = count1 + 1
            # print(count1)
        except UnicodeEncodeError as e:
            count += 1
            print(e)
            print(row)

    print(f'Number of error lines: {count}')

# Print a message indicating that the script has finished execution
print("Data has been written to wsbData.csv.")



