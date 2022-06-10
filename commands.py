# Python program to explain os.system() method 
      
# importing os module 
import os 
import sys
from termcolor import colored
  
args=sys.argv[1:]
# print(args)
# Command to execute
# Using Windows OS command
# print(args)
if len(args)>1:
    if args[0]=='-m':
        if args[1]=='np':
            currSong = 'spotify play'
            os.system(currSong)
        elif args[1]=='h':
            h='spotify history'
            os.system(h)
        elif args[1]=='b':
            b='spotify browse'
            os.system(b)
        elif args[1]=='s':
            if len(args)==3:
                s=f'spotify search {args[2]}'
                os.system(s)
    elif args[0]=='-c':
        if args[1]=='all':
            os.system('py charts.py')
    elif args[0]=='-s':
        if len(args)>1:
            os.system(f'py stats.py {args[1]}')
        
elif len(args)==1:
    if args[0]=='-m':
        print()
        print(colored('\x1b[6;30;42m' + 'SPOTIFY COMMANDS' + '\x1b[0m'))
        print(colored(f'np - current playing song','green'))
        print(colored(f'h - song history','green'))
        print(colored(f'b - open spotify browser','green'))
        print(colored(f's - search for a particular song','green'))
        print()

    
  
# Using os.system() method
# os.system()
