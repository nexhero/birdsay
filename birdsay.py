import sys
import textwrap
import requests
from bs4 import BeautifulSoup
#the bird come from http://www.chris.com/ascii/index.php?art=animals/birds%20%28land%29
def birdSay(user):
    tweet = getTweet(user)
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
def getTweet(user):
    url = "https://twitter.com/" + user
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    ps = soup.find("p", class_="ProfileTweet-text")  
    return ps.text

if len(sys.argv) < 2:
    print "Usage: '%s string'" % sys.argv[0]
    sys.exit(0)
else:
    print birdSay(sys.argv[1])
#print birdSay("Linus__Torvalds")
