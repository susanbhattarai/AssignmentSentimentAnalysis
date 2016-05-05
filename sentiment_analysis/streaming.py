import sys
import json
import os
import re
import pprint
#Class for storing the sentiment words and its corresponding score 
#and lookup features
class SentimentScore(object):
	_build = None

	def __init__(self, sent_file):
		if SentimentScore._build is None:
			SentimentScore._lookup = self._build_sentiment(sent_file)

	def _build_sentiment(self, sent_file):
		scores = {}
		for line in sent_file:
			word, score = line.split("\t")
			scores[word] = int(score)
		return scores

	def get_sentiment_score(self, word):
		if word in self._lookup:
			return self._lookup[word]
		return 0


def tweet_loader(tweet_file):
	"""
	Use JSON data from Twitter API to generate Python object
	"""
	#(tweet_file)
	tweet_list = []
	for line in tweet_file:
		tweet_object = json.loads(line.strip())
		tweet_list.append(tweet_object)
	return tweet_list

	'''
	Below code snippets only work for the raw json output
	'''
	# int_counter = 0
	# for line in tweet_file:
	# 	if len(line) != 0:
	# 		tweet_object = json.loads(line.strip())
	# 		# tweet_object = tweet_object['statuses']
	# 		# print (tweet_object['statuses'][0])
	# 		# break
	# 		int_counter += 1
	# 		tweet_list.append(tweet_object)
	# # pprint.pprint(tweet_list)
	# return tweet_list


def get_text(tweet_list):
	all_text = []
	regx_pattern = r'[A-Za-z]+'
	for tweets in tweet_list: 
		if 'text' not in tweets.keys():
			continue
		words_list = re.findall(regx_pattern, tweets['text'])
		all_text.append(words_list)
	return all_text

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



def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    get_sentiments(sent_file, tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
