import psutil
import sys
from termcolor import colored
from sty import fg, bg, ef, rs
# print(psutil.sensors_temperatures())


# print(battery)
args=sys.argv[1:]
if len(args)>0:
    if args[0]=='battery':
        battery=psutil.sensors_battery()
        percent,minsLeft=battery.percent,battery.secsleft//60
        print()
        print('\x1b[6;30;42m' + 'BATTERY' + '\x1b[0m')
        
        print(colored('BATTERY PERCENTAGE :','blue'),colored(percent,'red') if percent<20 else colored(percent,'green'))
        print(colored('MINUTES BEFORE DEATH : ','red'),  colored(minsLeft,'red'))
        print()
    if args[0]=='cpu':
        print()
        print(bg.li_red,f'No of Cores : {psutil.cpu_count()}',bg.rs) #NO OF CORES
        print(colored(f'context switches : {psutil.cpu_stats().ctx_switches}','blue'))
        print(colored(f'interrups : {psutil.cpu_stats().interrupts}','blue'))
        print(colored(f'software interrupts : {psutil.cpu_stats().soft_interrupts}','blue'))
        print(colored(f'cpu frequency : {psutil.cpu_freq().current}','blue'))
        print()
        

