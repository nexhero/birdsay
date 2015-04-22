#!/usr/bin/env python
"""


                     .__                         
  ____   ____ ___  __|  |__   ___________  ____  
 /    \_/ __ \\  \/  /  |  \_/ __ \_  __ \/  _ \ 
|   |  \  ___/ >    <|   Y  \  ___/|  | \(  <_> )
|___|  /\___  >__/\_ \___|  /\___  >__|   \____/ 
     \/     \/      \/    \/     \/              

David Pereira  -  inexhero@gmail.com
https://github.com/nexhero
"""

import sys
import textwrap
import requests
from bs4 import BeautifulSoup
#the bird come from http://www.chris.com/ascii/index.php?art=animals/birds%20%28land%29


def birdSay(text , tweet_type = "NORMAL"):
    if tweet_type == "USER":
        tweet = getUserTweet(text)
    elif tweet_type == "TAG":
        tweet = getTagTweet(text)
    else:
        tweet = getSearchTweet(text)
    lines = buildText(tweet)
    return  buildBorde(lines) + buildBird()

def buildBird():
    return """
              ___   /
             (  "> /
              )(
             // )
          --//""--
          -/------ 

    """
def buildText(text):
    lines =  textwrap.wrap(text, 40)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]

def buildBorde(lines):
    borde = []
    bsize =  len(lines[0])
    borde.append("_" * bsize)
    for line in lines:
        borde.append("| %s |" % (line))
    borde.append("-" * bsize)
    return "\n".join(borde)

def getTweet(data):
    soup = BeautifulSoup(data)
    ps = soup.find("p", class_="js-tweet-text")  
    if ps == None:
        return "There are not tweets in this account"
    else:
        return ps.text

def getUserTweet(user):
    url = "https://twitter.com/" + user
    r = requests.get(url)
    data = r.text
    ps = getTweet(data)
    return ps

def getTagTweet(tag):
    url = "https://twitter.com/search?f=realtime&q=%23" + tag
    r = requests.get(url)
    data = r.text
    tweet = getTweet(data)
    return tweet    

def getSearchTweet(text):
    url = "https://twitter.com/search?f=realtime&q=" + text
    r = requests.get(url)
    data = r.text
    tweet = getTweet(data)
    return tweet    

#if len(sys.argv) < 2:
#    print "Usage: '%s string'" % sys.argv[0]
    #sys.exit(0)
#else:
 #   print birdSay(sys.argv[1])
#print birdSay("Linus__Torvalds")
