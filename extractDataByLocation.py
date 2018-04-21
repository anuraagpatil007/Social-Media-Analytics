"""
Group 12 Project Members:	1.	Anurag Patil
							2.	Niranjan Naik
							3.  Dhaval Metre
"""
from __future__ import print_function
import tweepy
import json
import _collections
import pymongo
from pymongo import MongoClient

MONGO_HOST = 'mongodb://localhost/twitterdb'  # assuming you have mongoDB installed locally and a database called 'twitterdb'

WORDS = ['trump']
tweetData=[]
   # This is a class provided by tweepy to access the Twitter Streaming API.

def collect_Tweet_on_dataConnection():
       # This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            client = MongoClient(MONGO_HOST)

            # Use twitterdb database. If it doesn't exist, it will be created.
            main_db = client.twitterdb
            db = client.twitter_dbbyLocation

            collection=main_db.twitter_search
            collectionNY=db.nyTweets
            collectionCENE=db.caneTweets
            collectionORWAID=db.orwaidTweets
            collectionMTWYNDSDMN=db.mtwyndsdmnTweets
            collectionFLGAKYNCSCMS=db.flgakyncscmsTweets
            collectionAZNM=db.aznmTweets
            collectionOKARTXLA=db.okartxlaTweets
            collectionMIILOHINWI=db.miilohinwiTweets

            path= 'C:/Users/anura/Desktop/DS project 1/extractedTweetTxtFiles/tenKTweets.txt'
            pathNY= 'C:/Users/anura/Desktop/DS project 1/extractedTweetTxtFiles/oneKTweetsNY.txt'
            pathCANE= 'C:/Users/anura/Desktop/DS project 1/extractedTweetTxtFiles/oneKTweetsCENE.txt'
            pathORWAID= 'C:/Users/anura/Desktop/DS project 1/extractedTweetTxtFiles/oneKTweetsORWAID.txt'
            pathFLGAKYNCSCMS= 'C:/Users/anura/Desktop/DS project 1/extractedTweetTxtFiles/oneKTweetsFLGAKYNCSCMS.txt'
            pathOKARTXLA= 'C:/Users/anura/Desktop/DS project 1/extractedTweetTxtFiles/oneKTweetsOKARTXLA.txt'
            pathMIILOHINWI= 'C:/Users/anura/Desktop/DS project 1/extractedTweetTxtFiles/oneKTweetsMIILOHINWI.txt'
			
			#Extracting 10k tweets
            file = open(path,'a',encoding='utf-8')
            for document in collection.find():
                 file.write(document['text'])

            file.close()
            #Extraxting tweets from New York region
			fileNY = open(pathNY,'a',encoding='utf-8')
            for document in collectionNY.find():
                 fileNY.write(document['text'])

            fileNY.close()

            #Extraxting tweets from CA region
            fileCANE = open(pathCANE,'a',encoding='utf-8')
            for document in collectionCENE.find():
                 fileCANE.write(document['text'])

            fileCANE.close()

            #Extraxting tweets from Oregon region
            fileORWAID = open(pathORWAID,'a',encoding='utf-8')
            for document in collectionORWAID.find():
                 fileORWAID.write(document['text'])

            fileORWAID.close()


            #Extraxting tweets from Florida region
            fileFLGAKYNCSCMS = open(pathFLGAKYNCSCMS,'a',encoding='utf-8')
            for document in collectionFLGAKYNCSCMS.find():
                fileFLGAKYNCSCMS.write(document['text'])

            fileFLGAKYNCSCMS.close()


            #Extraxting tweets from Texas region
            fileOKARTXLA = open(pathOKARTXLA,'a',encoding='utf-8')
            for document in collectionOKARTXLA.find():
                 fileOKARTXLA.write(document['text'])

            fileOKARTXLA.close()

			
            #Extraxting tweets from Illinios region
            fileMIILOHINWI = open(pathMIILOHINWI,'a',encoding='utf-8')
            for document in collectionMIILOHINWI.find():
                 fileMIILOHINWI.write(document['text'])

            fileMIILOHINWI.close()



        except Exception as e:
            print("inside exception")
            print(e)
            pass

        print(tweetData)

collect_Tweet_on_dataConnection()
