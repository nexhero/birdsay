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

import argparse
import birdsay

def main():
    parser =  argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u',"--user", help = "Use it to search by user. Whitout @ symbol", action='store_true')
    group.add_argument('-ht',"--hashtag", help = "Use it to seach using a hashtag. Whitout # symbol" ,action='store_true')
    parser.add_argument("text_search", help="Content to search", type = str)
    args = parser.parse_args()

    if args.user:
        print birdsay.birdSay(args.text_search, "USER")
    elif args.hashtag:
        print birdsay.birdSay(args.text_search, "TAG")
    else:
        print birdsay.birdSay(args.text_search)

main()
