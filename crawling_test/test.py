import tweepy

consumer_key='Ed04jQhvKpWJoufL7H1xUn4cS'
consumer_secret='K1Iv1Q8kHuSvkP4dnMJOl79dOKKSAkGhgnp0rP0d1karmyTI00'
access_token='949874709310595073-RhzKylfAt6r5TVWz1VJYSD23BobUv89'
access_token_secret='VO0CBVLpQLUMfzbDkW6zQtsuSQEsFYbY6quCQmPjBUlKs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keyword='여행 유럽 -@polkmn042'
result=[]

for i in range(1, 3):
    tweets = api.search(keyword)
    for tweet in tweets:
        result.append([tweet.id_str, tweet.text, tweet.created_at])
        
print(len(result))
for k in range(0, len(result)):
    print(result[k])