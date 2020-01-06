import tweepy

ckey = ''
csecret = ''
atoken = ''
asecret = ''

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

user = api.get_user('Momothebowler')

api.update_status("Happy New Year Everyone!!!!!!!! <3")
"""
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
"""
