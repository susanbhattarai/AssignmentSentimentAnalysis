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


"""
Main part where the functions are assembled and 
the words which do not have sentiment score are analysed and
their score is calculated
"""
def hw(sent_file, tweet_file):
	tweets_json = tweet_loader(tweet_file)
	sentiment_score = SentimentScore(sent_file)
	tweet_text = get_text(tweets_json)
	new_sentiment_score = {} #Dictionary to store new words with sentiments
	for individual_tweet in tweet_text: #Loop
		sentiment_sum = 0  #Sentiment sum of sentence
		sentiment_num  = 0 #Num of words
		without_senti = [] #Array for storing the words in one iteration
		for words in individual_tweet:
			senti_val = sentiment_score.get_sentiment_score(words) #Get the sentiment
			if senti_val == 0: #If 0, add to array
				without_senti.append(words)
				#print without_senti
			else:
				#print words, senti_val
				sentiment_sum += senti_val #Add the senti_val
				sentiment_num += 1 

		compute_senti = float(sentiment_sum) / sentiment_num if sentiment_num != 0 else sentiment_sum #Compute the sentiment
		for words in without_senti:
			new_sentiment_score[words] = compute_senti #Set the computed sentiment for those words without sentiment
	for words, senti in  new_sentiment_score.items():#Print all words with sentiments
		print "%s, %s" % (words, senti)

"""
Main For executing all the functions inclusive of command line arguments
"""
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
