import pyjokes
import randfacts
from GoogleNews import GoogleNews

import sys

from termcolor import colored
args=sys.argv[1:]
# print(args)
if args[0]=='fact':
    x = randfacts.get_fact()
    print()
    print(colored(x,'magenta'))
    print()
elif args[0]=='joke':
    My_joke = pyjokes.get_joke(language="en", category="neutral")
    print()
    print(colored(My_joke,'magenta'))
    print()
elif args[0]=='news':
    # print('hi')
    if len(args)>1 and args[1]!='-n':
        googlenews = GoogleNews(lang='en',period='2d')
        googlenews.get_news(f'{args[1:]}')
        # print(googlenews.page_at(1))
        result=googlenews.result()
        # print(result)
        colors=['red','green','yellow','blue','magenta','cyan']
        c=0
        for i in result:
            print()
            print(colored(i['title'],colors[c%len(colors)]))
            print(colored(i['site'],colors[c%len(colors)]))
            print(colored(i['date'],colors[c%len(colors)]))
            print()
            c+=1
    elif len(args)>1 and args[1]=='-n' :
        try:
            googlenews = GoogleNews(lang='en',period='2d')
            googlenews.get_news(f'{args[3:]}')
            # print(googlenews.page_at(1))
            result=googlenews.result()[:int(args[2])]
            # print(result)
            colors=['red','green','yellow','blue','magenta','cyan','white']
            c=0
            for i in result:
                print()
                print(colored(i['title'],colors[c%len(colors)]))
                print(colored(i['site'],colors[c%len(colors)]))
                print(colored(i['date'],colors[c%len(colors)]))
                print()
                c+=1
        except:
            print(colored('Invalid input','red'))
    else:
        print(colored(f'-n - no of results','green'))
