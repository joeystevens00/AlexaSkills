import praw
import os
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
    client_id=os.getenv("REDDIT_CLIENT_ID")
    client_secret=os.getenv("REDDIT_CLIENT_SECRET")
    password=os.getenv("REDDIT_PASSWORD")
    username=os.getenv("REDDIT_USERNAME")
    reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='testscript',
                     username=username)


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

