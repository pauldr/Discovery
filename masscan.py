import os

#input variables
#ports = input('Enter a port number or port range: ')
#ip = input('Enter an IP address or IP CIDR Block: ')
rate = 1000

s = os.system("masscan --ports 0-65535 10.37.132.14 --banners --rate=rate") 
