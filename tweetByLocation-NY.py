"""
Group 12 Project Members:	1.	Anurag Patil
							2.	Niranjan Naik
							3.  Dhaval Metre
"""

from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient

MONGO_HOST = 'mongodb://localhost/twitterdb'  # assuming you have mongoDB installed locally
# and a database called 'twitterdb'

WORDS = ['trump']

#create a twitter application and use your credentials to get the code running
CONSUMER_KEY = "Consumer Key"
CONSUMER_SECRET = "consumer secret"
ACCESS_TOKEN = "accesstoken"
ACCESS_TOKEN_SECRET = "token secret"


class StreamListener(tweepy.StreamListener):
    # This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        # This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            client = MongoClient(MONGO_HOST)

            # Use twitterdb database. If it doesn't exist, it will be created.
            db = client.twitter_dbbyLocation

            # Decode the JSON from Twitter
            datajson = json.loads(data)

            # grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']

            # print out a message to the screen that we have collected a tweet
            # insert the data into the mongoDB into a collection called twitter_search
            # if twitter_search doesn't exist, it will be created.
            if "lang" in datajson and datajson["lang"] == "en" and "text" in datajson and "trump" in datajson["text"]:
                      print("Tweet collected at NY,MA,PA,NJ,DE,CT,MD,VT,NH" + str(created_at))
                      db.nyTweets.insert(datajson)

        except Exception as e:
           pass
           print(e)

#FL, GA,KY,NC,SC,MS
#MT,WY,ND,SD,MN
#OR,WA,ID
#NE,CA
#AZ,NM
#OK,TX,LA,AR
#MI,IL,OH,IN,WI
#NY,MA,PA,NJ,DE,CT,MD,VT,NH
locNY=[-78.49,37.86,-61.08,47.87]


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: NY Tweets")
streamer.filter(locations=locNY)
