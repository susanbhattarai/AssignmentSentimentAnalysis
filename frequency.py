#Import from tweet_sentiment
from streamingforsentiments import *
from operator import itemgetter


def get_frequency(tweet_file):
	#Get raw tweet from streaming file
	tweets_raw = tweet_loader(tweet_file)
	#Get text from raw tweet
	tweets_text = get_text(tweets_raw)
	#Python dic for storing words as index and frequency as key
	words = {}
	#Iterate over list of word of tweet
	for word_list in tweets_text:
		#Iterate over each word
		for word in word_list:
			words[word] = words.get(word, 0) + 1
	#Get total number of words
	total_words = sum(words.values())
	print total_words
	
	# #Calculate frequency distribution
	# for word in words:
	# 	words[word] = float(words[word]) / total_words
	#Print word with it's frequency
	sorted_words = sorted(words.iteritems(), key=itemgetter(1), reverse=True)
	for (word, freq) in sorted_words:
		print "%s %s" % (word, freq)


def main():
	tweet_file = open(sys.argv[1])
	get_frequency(tweet_file)

if __name__ == "__main__":
	main()

