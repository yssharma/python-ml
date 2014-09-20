from pattern.web import Twitter, plaintext



#
# Gets tweets having the given Phrase
# Uses the pattern API to fetch the tweets
#
def searchtweets(phrase):
	phrase = '"'+phrase+'"'
	twitter = Twitter(language='en') 
	return twitter.search(phrase, cached=False)



	
