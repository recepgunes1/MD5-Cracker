#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'Recep Gunes'

import requests, sys, time
from bs4 import BeautifulSoup
import hashlib
from termcolor import colored


def banner():
    print("""{}
'||    ||' '||''|.   ____                                   
 |||  |||   ||   ||  ||  `                                  
 |'|..'||   ||    || ||_                                    
 | '|' ||   ||    || |/ \                                   
.|. | .||. .||...|'     ))                                  
                       //                                   
                      /'                                    
  ..|'''.|                         '||                      
.|'     '  ... ..   ....     ....   ||  ..    ....  ... ..  
||          ||' '' '' .||  .|   ''  || .'   .|...||  ||' '' 
'|.      .  ||     .|' ||  ||       ||'|.   ||       ||     
 ''|....'  .||.    '|..'|'  '|...' .||. ||.  '|...' .||.    
{}\n\tHow To Use:\n\tpython3 md5-cracker.py [hash_text]\n{}""".format("="*75,"="*75,"="*75))

def crackhash(password):
    try:
        req = requests.post(url="http://crackhash.com", data={"hash":password,"crack":"crack"})
        source_code = req.content
        soup = BeautifulSoup(source_code,"html.parser")
        brute_text = soup.find_all("tr",{"class":"success"})
        brute_text = brute_text[0]
        plain_text = brute_text.text.rpartition("==>")[2]
        print("crackhash.com ===> {}\n{}".format(plain_text,"="*75))
    except IndexError:
        print("crackhash.com ===> Hash Don't Found!\n{}".format("=" * 75))
    except requests.ConnectionError or requests.ConnectTimeout:
        print("crackhash.com ===> Connection Error!!!\n{}".format("=" * 75))

def hashcrack(password):
    try:
        req = requests.post(url="http://hashcrack.com",data={"auth":"8272hgt","hash":password,"string":"","Submit":"Submit"})
        source_code = req.content
        soup = BeautifulSoup(source_code,"html.parser")
        brute_text = soup.find_all("span",{"class":"hervorheb2"})
        plain_text = brute_text[0].text
        print("hashcrack.com ===> {}\n{}".format(plain_text,"="*75))
    except IndexError:
        print("hashcrack.com ===> Hash Don't Found!\n{}".format("=" * 75))
    except requests.ConnectionError or requests.ConnectTimeout:
        print("hashcrack.com ===> Connection Error!!!{}\n".format("=" * 75))

def md5_gromweb(password):
    try:
        req = requests.get(url="https://md5.gromweb.com",params={"md5":password})
        source_code = req.content
        soup = BeautifulSoup(source_code,"html.parser")
        brute_text = soup.find_all("em",{"class":"long-content string"})
        plain_text = brute_text[0].text
        print("md5.gromweb.com ===> {}\n{}".format(plain_text,"="*75))
    except IndexError:
        print("md5.gromweb.com ===> Hash Don't Found!\n{}".format("=" * 75))
    except requests.ConnectionError or requests.ConnectTimeout:
        print("md5.gromweb.com ===> Connection Error!!!\n{}".format("=" * 75))

def md5decryption(password):
    try:
        req = requests.post(url="http://md5decryption.com", data={"hash":password,"submit":"Decrypt It!"})
        source_code = req.content
        soup = BeautifulSoup(source_code,"html.parser")
        brute_text = soup.find_all("img",{"src":"line.gif"})
        brute_text = brute_text[0]
        plain_text = brute_text.text.split()[2]
        if plain_text == "MD5":
            print("md5decryption.com ===> Hash Don't Found!\n{}".format("=" * 75))
        else:
            print("md5decryption.com ===> {}\n{}".format(plain_text,"="*75))
    except requests.ConnectionError or requests.ConnectTimeout:
        print("md5decryption.com ===> Connection Error!!!\n{}".format("=" * 75))

def md5_my_addr(password):
    try:
        req = requests.post(url="http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php",data={"md5":password,"x":"21","y":"12"})
        source_code = req.content
        soup = BeautifulSoup(source_code,"html.parser")
        brute_text = soup.find_all("div",{"class":"white_bg_title"})
        plain_text = brute_text[1].text.split()[2]
        print("md5.my-addr.com ===> {}\n{}".format(plain_text,"="*75))
    except IndexError:
        print("md5.my-addr.com ===> Hash Don't Found!\n{}".format("="*75))
    except requests.ConnectionError or requests.ConnectTimeout:
        print("md5.my-addr.com ===> Connection Error!!!\n{}".format("=" * 75))

if __name__ == '__main__':
    try:
        start_time = time.time()
        hash_text = sys.argv[1].lower()
        banner()
        crackhash(hash_text)
        hashcrack(hash_text)
        md5_gromweb(hash_text)
        md5decryption(hash_text)
        md5_my_addr(hash_text)
        print("Elapsed Time (Sec): {}\n{}".format(time.time() - start_time,"="*75))
    except IndexError:
        print("Please, Entry A Hash Text!")
    except:
        print("Don't Know Error!")
        
        
        
        
        
hashvalue = input("[*] Enter Your String: ")
type = input("[*] Enter Your Hash Type: ")

hash1 = 'md5'
hash2 = 'sha1'
hash3 = 'sha256'
hash4 = 'sha384'
hash5 = 'sha512'
hash6 = 'sha224'
hash7 = 'blake2c'
hash8 = 'blake2b'


if type == hash1:
	hashobj = hashlib.md5()
	hashobj.update(hashvalue.encode())
	print (hashobj.hexdigest())
	quit()
elif type == hash2:
	hashobj = hashlib.sha1()
	hashobj.update(hashvalue.encode())
	print (hashobj.hexdigest())
	quit()
elif type == hash3:
	hashobj = hashlib.sha256()
	hashobj.update(hashvalue.encode())
	print (hashobj.hexdigest())
	quit()
elif type == hash4:
	hashobj = hashlib.sha384()
	hashobj.update(hashvalue.encode())
	print (hashobj.hexdigest())
	quit()
elif type == hash5:
	hashobj = hashlib.sha512()
	hashobj.update(hashvalue.encode())
	print (hashobj.hexdigest())
	quit()
elif type == hash6:
	hashobj = hashlib.sha224()
	hashobj.update(hashvalue.encode())
	print (hashobj.hexdigest())
	quit()
elif type == hash7:
	hashobj = hashlib.blake2s()
	hashobj.update(hashvalue.encode())
	print (hashobj.hexdigest())
	quit()
elif type == hash8:
	hashobj = hashlib.blake2b()
	hashobj.update(hashvalue.encode())
	print (hashobj.hexdigest())
	quit()



print ("[!!] Please Enter Valid Hash  Type....!!!!!!!!")

        
        
