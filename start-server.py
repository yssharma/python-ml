from bottle import route, run
from bottle import response
from json import dumps
from pattern_usage import searchtweets 

@route('/')
def status():
	res = {"message": "Web App Running", "status": response.status}
	response.content_type = 'application/json'
	return dumps(res)



@route('/searchtweets')
@route('/searchtweets/<tweet>')
def searchtweeets(tweet=None):
	if not tweet:
		res  = {"message": "Tweet not provided", "status": "ERROR", "usage":"/searchtweets/tweet"}
		response.content_type = 'application/json'
	        return dumps(res)
	else:
		response.content_type = 'application/json'
		tweets = searchtweets(tweet)
		return dumps([dict(mpn=pn.text) for pn in tweets])


run(host='localhost', port=8081, debug=True)
