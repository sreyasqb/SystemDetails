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
    if args[0]=='-s':
        print()
        print(colored('\x1b[6;30;42m' + 'STATS COMMANDS' + '\x1b[0m'))
        print(colored(f'battery - battery stats','green'))
        print(colored(f'cpu - cpu stats','green'))
        print()
    if args[0]=='game':
        print(colored('\x1b[6;30;42m' + 'PYTHON OP!!!' + '\x1b[0m'))
        os.system('py snake.py')
        print(colored('\x1b[6;30;42m' + 'GAME OVER' + '\x1b[0m'))
    if args[0]=='joke':
        os.system('py jokes.py')

else:
    print()
    print(colored('\x1b[6;30;42m' + 'COMMANDS' + '\x1b[0m'))
    print(colored(f'-m for music','green'))
    print(colored(f'-c for charts','green'))
    print(colored(f'-s for stats','green'))
    print(colored(f'game - play snake game','green'))
    print(colored(f'joke - get a joke','green'))

    

    
  
# Using os.system() method
# os.system()
