#You will now put together these learnings to good use by working with a Twitter dataset. Before practicing your new error handling skills; in this exercise, you will write a lambda function and use filter() to select retweets, that is, tweets that begin with the string 'RT'.


# The task:
# 1. In the filter() call, pass a lambda function and the sequence of tweets as strings, tweets_df['text']. The lambda function should check if the first 2 characters in a tweet x are 'RT'. Assign the resulting filter object to result. To get the first 2 characters in a tweet x, use x[0:2]. To check equality, use a Boolean filter with ==.
# 2. Convert result to a list and print out the list.

# Import pandas
import pandas as pd

# Read the tweets CSV file into tweets_df
tweets_df = pd.read_csv('tweets.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)