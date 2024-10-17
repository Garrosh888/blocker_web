import ctypes
import time
from datetime import datetime
import sys
import psutil
def main():
    block_start = datetime(datetime.now().year,datetime.now().month,datetime.now().day,10)
    block_end = datetime(datetime.now().year,datetime.now().month,datetime.now().day,14)
    print(block_start,block_end)
    way = r'C:\Windows\System32\drivers\etc\hosts'
    url = '127.0.0.1'
    web_list = ["www.youtube.com","youtube.com"]
    while True:
        if block_start < datetime.now() <block_end:
            print("сайты заблокированы")
            with open(way,"r+") as fileOS:
                info = fileOS.read()#все содиржімое нашего файла
                for web in web_list:
                    if web in info:
                        pass
                    else:
                        fileOS.write(f"{url} {web} \n")
        else:
            with open(way,"r+") as fileOS:
                info = fileOS.readlines()
                fileOS.seek(0)
                for line in info:
                    if not any (site in line for site in web_list):
                        fileOS.write(line)
                fileOS.truncate()
            print("cайты работают")
        time.sleep(5)

if ctypes.windll.shell32.IsUserAnAdmin():
    if __name__ == "__main__":
        main()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)