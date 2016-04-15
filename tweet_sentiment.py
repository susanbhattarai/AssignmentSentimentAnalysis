import sys
import json
import re

"""Sentiment Score class for building the 
	sentiment score of words
"""
class SentimentScore(object):
	_build =None #Private variable build
	def __init__(self, sent_file):
		if SentimentScore._build == None:
			SentimentScore._lookup = self._build_sentiment(sent_file)

	def _build_sentiment(self, sent_file):
		scores  = {}
		for line in sent_file:
			word, score = line.split('\t')
			scores[word] = float(score)
		return scores

	def get_sentiment_score(self,word):
		if word in self._lookup:
			return self._lookup[word]
		return 0 #If words not in text , asssume it's score is zero

"""
Load the tweets (raw JSON) courtesy of twitterstream API
"""
def tweet_loader(tweet_file):
	"From Twitter API"
	tweet_list = [] #List for saving the individual tweets JSON
	for line in tweet_file:
		tweet_object = json.loads(line.strip())
		tweet_list = tweet_object['statuses'] #Get the value from JSON
	return tweet_list #Return the list of tweets

"""
Get the appropriate text from the JSON file using regex
"""
def get_text(tweet_list):
	all_tweet_text = [] #List for storing the tweet words list
	reg_pattern = r'[A-Za-z]+' #Pattern for getting a word
	for individual_tweet in tweet_list: #Loop over tweet list
		if 'text' not in individual_tweet.keys():
			continue
		word_list = re.findall(reg_pattern, individual_tweet['text']) #Get a list of words
		all_tweet_text.append(word_list) #Insert into all_tweet_text
	return all_tweet_text #Return 

def get_sentiments(sent_file, tweet_file):
	tweets_raw = tweet_loader(tweet_file)
	sentiment_score = SentimentScore(sent_file)
	tweets_text = get_text(tweets_raw)
	# print tweets_text

	sum_by_tweet = []
	for words in tweets_text:
		tweet_scores = [sentiment_score.get_sentiment_score(i.lower()) for i in words]
		total_score = sum(tweet_scores)
		# if total_score <= -5:
			# print words
		sum_by_tweet.append(total_score)
		print total_score
	print "Total Tweets Proceeded: %s" %len(tweets_raw)
	print "Sum of SentimentScore: %s" %str(sum(sum_by_tweet))
	print "Mean Sentiment Score: %s" % str(sum(sum_by_tweet)/float(len(sum_by_tweet)))



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    get_sentiments(sent_file, tweet_file)

if __name__ == '__main__':
    main()
