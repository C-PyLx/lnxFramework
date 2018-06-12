#!/usr/bin/env python3
# -*-coding: utf-8 -*-
#__Author__: Learning :~#
#Linux framework powerful script!
#Report bugs to: https://github.com/C-PyLx/lnxFramework
#Telegram id: https://t.me/Ac3ess

import os
import sys
import time
import socket
import hashlib
import requests
import itertools
import webbrowser
from urllib.error import (URLError, HTTPError)

class color:
    blue = '\033[34m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'    
    bold = '\033[1m'
    end = '\033[0m'

Banner = '''\033[92m#$#$#$ #$#$#$# $#$#$#$ #$#$     $#$# $#$#$# $#        #$       #$#$#$# $#   $#\033[0m
\033[91m$#     $#   #$ #$   $# $# #$   $# #$ #$     #$        $# $#$#$ $#   #$ #$  #$\033[0m
\033[34m#$#$#$ #$#$#$# $#$#$#$ #$  $#$#$  $# $#$#$  $#  #$#$  #$ # . # #$#$#$# $#$#\033[0m
\033[93m$#     $# #$   #$   $# $#         #$ #$     #$ $#  $# $# $ . $ $#  $#  #$  #$\033[0m
\033[96m#$     #$  $#  $#   #$ #$         $# $#$#$# $#$#    #$#$ #$#$# #$   #$ $#   $#\033[0m
              \033[91m*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\033[0m
		 \033[92m*-*-*-*{ Coded By: Learning :~# }*-*-*-*\033[0m
		 \033[92m    *-*-*-*{ Version: 1.0.0 }*-*-*-*\033[0m
              \033[91m*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\033[0m
'''

Menu = '''[\033[94m1\033[0m] \033[31m~>\033[0m Word list generator >> {\033[92mFast & Powerful\033[0m}
[\033[94m2\033[0m] \033[31m~>\033[0m SQL-MySQL vulnerability scanner
[\033[94m3\033[0m] \033[31m~>\033[0m Change your IP address >> {\033[92mAnonymous Attacks!\033[0m}
[\033[94m4\033[0m] \033[31m~>\033[0m Show saved Wi-Fi passwords >> {\033[92mNeed Root!\033[0m}
[\033[94m5\033[0m] \033[31m~>\033[0m What is my username & IP?
[\033[94m6\033[0m] \033[31m~>\033[0m Open an custom website
[\033[94m7\033[0m] \033[31m~>\033[0m Generate hash sums >> {\033[92mAll Hash Types!\033[0m}
[\033[94m8\033[0m] \033[31m~>\033[0m Crack hash sums >> {\033[92mJust (MD5) Hashes!\033[0m}
[\033[94m9\033[0m] \033[31m~>\033[0m Shutdown your pc
[\033[94mx\033[0m] \033[31m~>\033[0m Restart your pc
[\033[94mi\033[0m] \033[31m~>\033[0m See network status

[\033[91m0\033[0m] \033[91m~>\033[0m Exit from (\033[91mlnxFramework!\033[0m)
'''

def lnxFramework():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        print (Banner)
        print (color.bold + '\033[3m\033[36m[ > ] Select option with [] codes [ < ]\n', color.end)
        print (Menu)
        choice = input ('''┌─[\033[92mlnxFramework\033[0m] > [\033[93m\033[5mmenu\033[0m]
└────► ''')
        try:
            if choice == 'clear':
                lnxFramework()
            elif choice == '1':
                wordList()
            elif choice == '2':
                sqlScanner()
            elif choice == '3':
                changeIp()
            elif choice == '4':
                showWiFi()
            elif choice == '5':
                userNamePassword()
            elif choice == '6':
                openWebSite()
            elif choice == '7':
                generateHash()
            elif choice == '8':
                crackHash()
            elif choice == '9':
                shutdownPc()
            elif choice == 'x':
                rebootPc()
            elif choice == 'i':
                netStatus()
            elif choice == '0':
                exitApp()
            elif choice == '' or choice == '\r' or choice == '\n' or choice == ' ' or choice == '\t':
                lnxFramework()
            else:
                lnxFramework()
        except KeyboardInterrupt:
            exitApp()
    except KeyboardInterrupt:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print ('*-'*30)
        print (color.red + color.bold + '       ~>~>~> Thanks For Using (lnxFramework) <~<~<~', color.end)
        print (color.blue + color.bold + '~>~>~> Follow me on github (https://github.com/C-PyLx <~<~<~', color.end)
        print ('*-'*30)
        time.sleep(3)        
        sys.exit()

def wordList():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        chrs = input ('[ ~ ] Enter characters for create words: ')
        min = int(input ('[ ~ ] Enter minimum length: '))
        max = int(input ('[ ~ ] Enter maximum length: '))
        out = input ('[ ~ ] Enter output filename(.TXT): ')

        if chrs == '':
            chrs = "`'/>,<.)(*&^%$#@![]}{:;=+_-"
        if out == '':
            out = "output.txt"
        if out == '' and chrs == '':
            chrs = "`'/>,<.)(*&^%$#@![]}{:;=+_-"
            out = "output.txt"

        if min > max:
            print (color.red + '\n[ X ] Error: Minimum length must be smaller than maximum length !\n', color.end)
            sys.exit()

        print ()
        print ('-+-'*20)
        print (color.blue + '[ ✔ ] WordList generator started at: %s' %time.strftime('%H:%M:%S'), color.end)
        print (color.blue + '[ ~ ] Passwords must saved into: %s' %out, color.end)
        print ('-+-'*20, '\n')
        out = open(out, 'w+')

        for word in range(min, max+1):
            for words in itertools.product(chrs, repeat=word):
                chars = ''.join(words)
                out.write('%s\n' %chars)
                sys.stdout.write(color.green + '\r[ ~ ] Writing character \033[0m~>| %s %s %s |<~' %(color.red+color.bold, chars, color.end) + color.end)
                sys.stdout.flush()
        out.close()

        print (color.yellow + color.bold + '\n\n[ # ] Words creation time left: %s' %time.strftime('%H:%M:%S'), color.end)
        print (color.blue + '\n[ ✔ ] Words saved to: |%s| successfully.' %out.name, color.end)

        try:
            input ('\n[ - ] [Enter] for back | [Ctrl+C] for exit:')
            lnxFramework()
        except KeyboardInterrupt:
            exitApp()
    except KeyboardInterrupt:
        print (color.yellow + '\n[ x ] Operation was stopped !', color.end)
        time.sleep(3)
        lnxFramework()
    except ValueError:
        print (color.red + '\n[ X ] Error: This value is not true !', color.end)
        time.sleep(3)
        lnxFramework()
    except NameError:
        print (color.red + '\n[ X ] Error: Name entry was not defined !', color.end)
        time.sleep(3)
        lnxFramework()
    except TypeError:
        print (color.red + '\n[ X ] Error: This type entry not true !', color.end)
        time.sleep(3)
        lnxFramework()
    
def sqlScanner():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        webSite = input ('[ - ] Enter terget website address: ')
        print (color.blue + '\n[ ~ ] Checking target %s DataBase...' %webSite)
        response = requests.get(webSite, "'").text
        if 'You have an error in SQL syntax' in response:
            print (color.green + '\n[ ✔ ] Allright: Target {%s} is vulnerable to SQL injections.' %webSite, color.end)
        elif 'error' in response and 'syntax' in response or 'MySQL' in response:
            print (color.green + '\n[ ✔ ] Allright: Target {%s} is vulnerable to MySql Attacks.' %webSite, color.end)
        else:
            print (color.red + color.bold + '\n[ X ] Not: Target {%s} is not vulnerable !' %webSite, color.end)
        try:
            input ('\n[ - ] [Enter] for back | [Ctrl+C] for exit:')
            lnxFramework()
        except KeyboardInterrupt:
            exitApp()
    except HTTPError:
        print (color.red + '\n[ X ] Error: We can not find your webserver !', color.end)
        time.sleep(3)
        lnxFramework()
    except URLError:
        print (color.red + '\n[ X ] Error: Check your website entry !', color.end)
        time.sleep(3)
        lnxFramework()
    except requests.exceptions.MissingSchema:
        print (color.red + '\n[ X ] Please enter your target with format:(http://[target.com]) !', color.end)
        time.sleep(3.9)
        sqlScanner()
    except requests.exceptions.ConnectionError:
        print (color.red + '\n[ X ] Error: Connection aborted, Check your url address !', color.end)
        time.sleep(3)
        lnxFramework()
    except requests.exceptions.InvalidSchema:
        print (color.red + '\n[ X ] Error: No connection adapter was found on: {%s} !' %webSite, color.end)
        time.sleep(3)
        lnxFramework()
    except KeyboardInterrupt:
        lnxFramework()

def changeIp():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        giveIp = input ('[ - ] Enter your custom IP: ')
        if os.name == 'nt':
            os.system('ipconfig {}' .format(giveIp))
            print (color.green + '\n[ ✔ ] Your IP address was changed to: %s' %giveIp, color.end)
            input()
            lnxFramework()
        else:
            os.system('sudo ifconfig eth0 %s netmask 255.255.255.0' %giveIp)
            print (color.green + '\n[ ✔ ] Your IP address was changed to: %s' %giveIp, color.end)
            input()
            lnxFramework()
    except KeyboardInterrupt:
        lnxFramework()
    except ValueError:
        print (color.red + '[ X ] Error: This value not difined !', color.end)
        time.sleep(3)
        lnxFramework()
    except TypeError:
        print (color.red + '[ X ] Error: Type entry was not true !', color.end)
        time.sleep(3)
        lnxFramework()

def showWiFi():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        psk = os.system('sudo grep psk= /etc/NetworkManager/system-connections/*')
        save = input ('\n[ - ] Do you want to save wifi passwords into an file? [Y/n]: ')
        if 'y' in save or 'Y' in save or 'yes' in save or 'YES' in save:
            path = input ('\n[ - ] Enter filename for save passwords(.TXT): ')
            path = open(path, 'w+')
            path.write(str(psk))
            print (color.green + '[ ✔ ] All of passwords have been saved to: {%s}.' %path.name, color.end)
            try:
                input ('\n[ - ] [Enter] for back | [Ctrl+C] for exit: ')
                lnxFramework()
            except KeyboardInterrupt:
                exitApp()
        try:
            input ('\n[ - ] [Enter] for back | [Ctrl+C] for exit: ')
            lnxFramework()
        except KeyboardInterrupt:
            exitApp()
        except IOError:
            print (color.red + '\n[ X ] Can not open file !', color.end)
            time.sleep(4)
            lnxFramework()
    except KeyboardInterrupt:
        lnxFramework()

def userNamePassword():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        userName = socket.gethostname()
        ipAddress = socket.gethostbyname(userName)
        print (color.green + '[ ✔ ] Username: %s' %userName)
        print (color.green + '[ ✔ ] IPAddress: %s' %ipAddress, color.end)
        try:
            input ('\n[ - ] [Enter] for back | [Ctrl+C] for exit:')
            lnxFramework()
        except KeyboardInterrupt:
            exitApp()
    except KeyboardInterrupt:
        lnxFramework()

def openWebSite():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        webSite = input ('[ - ] Enter website address: ')
        webbrowser.open_new_tab("http://"+webSite)
        lnxFramework()
    except KeyboardInterrupt:
        lnxFramework()
    except ValueError:
        print (color.red + '[ X ] Error: This value not difined !', color.end)
        time.sleep(3)
        lnxFramework()
    #No Needs:
    #except URLError:
        #print (color.red + '\n[!] Error: Check your website entry !', color.end)
    #except HTTPError:
        #print (color.red + '\n[!] Error: We can not find your webserver !', color.end)

def generateHash():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        rawText = input ('[ - ] Enter your text for convert to hash: ')
        Type = input ('''[ - ] Enter hash type for convert them >>

    [\033[92mHASH TYPES\033[0m]:
/-------------------\    
| [\033[94m1\033[0m] -->  (MD5)    |
| [\033[94m2\033[0m] -->  (SHA1)   |
| [\033[94m3\033[0m] --> (SHA224)  |
| [\033[94m4\033[0m] --> (SHA256)  |
| [\033[94m5\033[0m] --> (SHA384)  |
| [\033[94m6\033[0m] --> (SHA512)  |
| [\033[94m7\033[0m] --> (BLAKE2b) |
| [\033[94m8\033[0m] --> (BLAKE2s) |
| [\033[91m0\033[0m] -->  (BACK)   |
\-------------------/
\033[96m>>>>>>>>>>.<<<<<<<<<<\033[0m

Select >> ''')
        print ('\n')
        if Type == '1':
            hashText = hashlib.md5(rawText.encode()).hexdigest()
            print(color.red + '*.'*30, color.end)
            print(color.green + '[ ✔ ] Raw Text: [{}].'.format(rawText), color.end)
            print(color.green + '[ ✔ ] MD5 Text: [{}].'.format(hashText), color.end)
            print(color.red + '*.'*30, color.end)

        elif Type == '2':
            hashText = hashlib.sha1(rawText.encode()).hexdigest()
            print(color.red + '*.'*30, color.end)
            print(color.green + '[ ✔ ] Raw Text: [{}].'.format(rawText), color.end)
            print(color.green + '[ ✔ ] SHA1 Text: [{}].'.format(hashText), color.end)
            print(color.red + '*.'*30, color.end)

        elif Type == '3':
            hashText = hashlib.sha224(rawText.encode()).hexdigest()
            print(color.red + '*.'*30, color.end)
            print(color.green + '[ ✔ ] Raw Text: [{}].'.format(rawText), color.end)
            print(color.green + '[ ✔ ] SHA224 Text: [{}].'.format(hashText), color.end)
            print(color.red + '*.'*30, color.end)

        elif Type == '4':
            hashText = hashlib.sha256(rawText.encode()).hexdigest()
            print(color.red + '*.'*30, color.end)
            print(color.green + '[ ✔ ] Raw Text: [{}].'.format(rawText), color.end)
            print(color.green + '[ ✔ ] SHA256 Text: [{}].'.format(hashText), color.end)
            print(color.red + '*.'*30, color.end)

        elif Type == '5':
            hashText = hashlib.sha384(rawText.encode()).hexdigest()
            print(color.red + '*.'*30, color.end)
            print(color.green + '[ ✔ ] Raw Text: [{}].'.format(rawText), color.end)
            print(color.green + '[ ✔ ] SHA384 Text: [{}].'.format(hashText), color.end)
            print(color.red + '*.'*30, color.end)

        elif Type == '6':
            hashText = hashlib.sha512(rawText.encode()).hexdigest()
            print(color.red + '*.'*30, color.end)
            print(color.green + '[ ✔ ] Raw Text: [{}].'.format(rawText), color.end)
            print(color.green + '[ ✔ ] SHA512 Text: [{}].'.format(hashText), color.end)
            print(color.red + '*.'*30, color.end)

        elif Type == '7':
            hashText = hashlib.blake2b(rawText.encode()).hexdigest()
            print(color.red + '*.'*30, color.end)
            print(color.green + '[ ✔ ] Raw Text: [{}].'.format(rawText), color.end)
            print(color.green + '[ ✔ ] BLAKE2b Text: [{}].'.format(hashText), color.end)
            print(color.red + '*.'*30, color.end)

        elif Type == '8':
            hashText = hashlib.blake2s(rawText.encode()).hexdigest()
            print(color.red + '*.'*30, color.end)
            print(color.green + '[ ✔ ] Raw Text: [{}].'.format(rawText), color.end)
            print(color.green + '[ ✔ ] BLAKE2s Text: [{}].'.format(hashText), color.end)
            print(color.red + '*.'*30, color.end)

        elif Type == '0':
            lnxFramework()
        
        elif Type == '' or Type == '\n' or Type == '\r' or Type == ' ' or Type == '\t':
            generateHash()
        else:
            generateHash()
        try:
            input ('\n[ - ] [Enter] for back | [Ctrl+C] for exit:')
            lnxFramework()
        except KeyboardInterrupt:
            exitApp()
    except KeyboardInterrupt:
        lnxFramework()

def crackHash():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        m = hashlib.md5()
        hash = ""
        HashFile = input ('[ - ] Enter Hash File Path: ')
        HashWord = input ('[ - ] Enter Word List Path: ')
        
        try:
            HashDoc = open(HashFile, "r")
        except IOError:
            print (color.red + "[ X ] Invalid file !", color.end)
            time.sleep(4)
            crackHash()
        else:
            hash = HashDoc.readline()
            hash = hash.replace("\n", "")
        
        try:
            WordFile = open(HashWord, "r")
        except IOError:
            print (color.red + "[ X ] Invalid file !", color.end)
            time.sleep(4)
            crackHash()
        else:
            pass
        try:
            print (color.blue + "\n[ ~ ] Cracking hash...\n", color.end)
            for line in WordFile:
                m = hashlib.md5() #Flush buffer for get hash typest.
                line = line.replace("\n", "")
                m.update(line.encode())
                WordHash = m.hexdigest()
                if WordHash == hash:
                    print (color.green + "[ ✔ ] Password Success Cracked\n", color.end)
                    print (color.red + ":+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:", color.end)
                    print (color.green + "[ + ] Hash-Word: {", hash, "}",color.end)
                    print (color.green + "[ + ] Pass-Word: {", line, "}",color.end)
                    print (color.red + ":+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:\n", color.end)
                    print ("\033[0;96m[ ! ] Wordlist lines: {\033[0m "+str(len(WordFile.readlines()))+" \033[0;96m}.", color.end)
                    print (color.green + '[ + ] Password found text: \033[0m{ \033[91m%s\033[0m }.' %line)
                    WordFile.close()
                    try:
                        input ('\n[ - ] [Enter] for back | [Ctrl+C] for exit:')
                        lnxFramework()
                    except KeyboardInterrupt:
                        exitApp()
        except KeyboardInterrupt:
            print (color.red + '\n[ X ] Stopped at: '+time.time())
            time.sleep(3)
            lnxFramework()
        print (color.red + "\n[ X ] This hash given not true !", color.end)
        time.sleep(4)
        crackHash()
    except KeyboardInterrupt:
        lnxFramework()
    except ValueError:
        print (color.red + '[ X ] Error: This value not difined !', color.end)
        time.sleep(3)
        lnxFramework()
    #except TypeError:
        #print (color.red + '[ X ] Error: Type entry was not true !', color.end)
       # time.sleep(3)
       # lnxFramework()
    except IndexError:
        print (color.red + '\n [ X ] File path index out of range !', color.end)
        time.sleep(4)
        lnxFramework()
    except IOError:
        print (color.red + '\n[ X ] Can not find your path !', color.end)
        time.sleep(3)
        crackHash()
    except FileNotFoundError:
        print (color.red + '\n[ X ] Can not find your file path !', color.end)
        time.sleep(3)
        crackHash()

def shutdownPc():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        Quess = input ('[ ✔ ] Are you sure to shutdown your pc? [Y/n]: ')
        if Quess == 'y' or Quess == 'Y':
            if os.name == 'nt':
                os.system('shutdown /r -t 10')
                print (color.green + '\n[ ! ] PC will shutdown in 10 seconds later.', color.end)
            else:
                os.system('shutdown -t 1')
                print (color.green + '\n[ ! ] PC will shutdown in 1 minute later.', color.end)
        else:
            print (color.red + '\n[ X ] Operation was cancelled.', color.end)
            time.sleep(3)
            lnxFramework()
    except KeyboardInterrupt:
        lnxFramework()

def rebootPc():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        Quess = input ('[ - ] Are you sure to restart your pc? [Y/n]: ')
        if Quess == 'y' or Quess == 'Y':
            if os.name == 'nt':
                os.system('shutdown /r -t 10')
                print (color.green + '\n[ ! ] PC will restart in 10 seconds later.', color.end)
            else:
                os.system('reboot')
                print (color.green + '\n[ ! ] PC will restart.', color.end)
        else:
            print (color.red + '\n[ X ] Operation was cancelled.', color.end)
            time.sleep(3)
            lnxFramework()
    except KeyboardInterrupt:
        lnxFramework()

def netStatus():
    try:
        os.system('clear')
        os.system('ifconfig')
        try:
            input('\n[ - ] [Enter] for back | [Ctrl+C] for exit:')
            lnxFramework()
        except KeyboardInterrupt:
            sys.exit('\n')
    except KeyboardInterrupt:
        lnxFramework()

def exitApp():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    try:
        print ('*-'*30)
        print (color.red + color.bold + '       ~>~>~> Thanks For Using (lnxFramework) <~<~<~', color.end)
        print (color.blue + color.bold + '~>~>~> Follow me on github (https://github.com/C-PyLx <~<~<~', color.end)
        print ('*-'*30)
        time.sleep(3)
        sys.exit()
    except KeyboardInterrupt:
        sys.exit()

#Run App:
lnxFramework()