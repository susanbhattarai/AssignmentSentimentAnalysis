from tweet_sentiment import * 


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
