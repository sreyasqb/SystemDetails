import psutil
import matplotlib
import matplotlib.pyplot as plt
from os import path
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')
diskCount=len(psutil.disk_partitions())
# print(psutil.virtual_memory()[2])
# print(psutil.swap_memory())
# print(psutil.disk_usage(path.realpath('/')))
import ctypes
import os
import platform
import sys

def get_free_space_mb(dirname):
    """Return folder/drive free space (in megabytes)."""
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 2**30
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024
print(get_free_space_mb('/'))
# print(psutil.disk_partitions())
# print(diskCount)
totalGraphs=diskCount+3
cols=3
rows=1+totalGraphs//3
fig, ax = plt.subplots(rows,cols)
fig.patch.set_facecolor("black")
# plt.axes().set_facecolor("black")
colors=["#f44336","black"]
def animateRamUsage(i):
    p=psutil.virtual_memory()[2]
    ax[0,0].clear()
    
    ax[0,0].pie([p,100-p],colors=colors,startangle=90,counterclock=False,
    wedgeprops= {"edgecolor":"#660000",
                    'linewidth': 0.5,
                    'antialiased': True,
                    'width':0.3,
                    })
    
    ax[0,0].set_title(f'RAM USAGE ({p}%)',color="white")
    ax[0,0].set_facecolor("black")

def animateCpu(i):
    p = psutil.cpu_percent()
    ax[0,1].clear()
    
    ax[0,1].pie([p,100-p],colors=colors,startangle=90,counterclock=False,
    wedgeprops= {"edgecolor":"#660000",
                    'linewidth': 0.5,
                    'antialiased': True,
                    'width':0.3,
                    })
    
    ax[0,1].set_title(f'CPU USAGE ({p}%)',color="white")
def animateSwap(i):
    
    p = psutil.swap_memory().percent
    ax[0,2].clear()
    
    ax[0,2].pie([p,100-p],colors=colors,startangle=90,counterclock=False,
    wedgeprops= {"edgecolor":"#660000",
                    'linewidth': 0.5,
                    'antialiased': True,
                    'width':0.3,
                    })
    
    ax[0,2].set_title(f'SWAP USAGE ({p}%)',color="white")





def diskSpaces():
    currRow=1
    currCol=0
    
    for disk in psutil.disk_partitions():
        # print(currRow,currCol)
        hdd = psutil.disk_usage(disk[0])
        total, used, free = hdd.total, hdd.used, hdd.free
        total //= 2**30
        used //= 2**30
        free //= 2**30
        # p = psutil.cpu_percent()
        ax[currRow,currCol].clear()
        
        ax[currRow,currCol].pie([used,total-used],colors=colors,startangle=90,counterclock=False,
        wedgeprops= {"edgecolor":"#660000",
                        'linewidth': 0.5,
                        'antialiased': True,
                        'width':0.3,
                        })
        
        ax[currRow,currCol].set_title(f'{disk[0]} ({used}/{total}GB)',color="white")
        if currCol<2:
            currCol+=1
        else:
            currRow+=1
            currCol=0
    for i in range(3-currCol):
        ax[currRow,currCol+i].set_visible(False)


# cpuAni=animation.FuncAnimation(fig, animateCpu,frames=60, interval=500,repeat=False)
# ramAni=animation.FuncAnimation(fig, animateRamUsage,frames=60, interval=500,repeat=False)
# swapAni=animation.FuncAnimation(fig, animateSwap,frames=60, interval=500,repeat=False)
# diskSpaces()
# plt.show()

    
# print(psutil.virtual_memory()[2]) #RAM USAGE
