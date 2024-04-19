import praw

# Initialize Reddit API connection
reddit = praw.Reddit(
    client_id='o-k8HsUeNmbssImQgRy9Aw',
    client_secret='LrEr3JNVjowGLxgQajiPBlH4lIAQSg',
    user_agent='MyAwesomeRedditApp/1.0 by /u/Necessary-Donut-7119'

)

# Define subreddit
subreddit_name = 'wallstreetbets'
subreddit = reddit.subreddit(subreddit_name)

# Get posts from the subreddit
posts = subreddit.new(limit=None)

# Iterate over the posts and print some information
for post in posts:
    print("Title:", post.title)
    print("Content Text:", post.selftext)
    print("Score:", post.score)
    print("Comments count:", post.num_comments)
    print("URL:", post.url)
    print("------------------------------")