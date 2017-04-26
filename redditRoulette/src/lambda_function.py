import praw
#import pyssml.PySSML # Hackery to fix a misconfigured module 
						 # in the directory pyssml get the PySSML module
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
def lambda_handler(event, context):
    # TODO implement
    reddit = praw.Reddit(client_id='_C7dnicU51oy3w',
                     client_secret='m6Y7Hv_aR3WCAix0Z1yFcna6F9Q',
                     password='0IoV&s$RsppE',
                     user_agent='testscript',
                     username='f42e9c26-6e84-486d-b')

    randomSub=reddit.random_subreddit(nsfw=False)
    randomSubmission=randomSub.random()
    #s = pyssml.PySSML.PySSML() # An instance of the PySSML class in the pyssml directory in the pyssml module
    title=strip_tags(randomSubmission.title)
    body=strip_tags(str(randomSubmission.selftext_html))
    speechlet_response = {
    		"outputSpeech": {
    			"type": "PlainText",
    			"text": "Title " + title + " Body" + body
    		},
    		"card": {
    			"type": "Simple",
    			"title": title,
    			"content": body
    		}, 
    		"shouldEndSession": True	
    	}
    build_response = { 
    	"version": "1.0", 
    	"response": speechlet_response,
    	"sessionAttributes": {}
    }
    return build_response

