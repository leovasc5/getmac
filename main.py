import os
os.system('pip install getmac')

import getmac
os.system('clear')
os.system('figlet MAC Address')
print(getmac.get_mac_address())