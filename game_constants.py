#C:\\Python27\python.exe

import ctypes


def screen_size():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


screensize = screen_size()
# SIZE = (screensize[0]-2, screensize[1]-26) #temporary
SIZE = (700, 400)
