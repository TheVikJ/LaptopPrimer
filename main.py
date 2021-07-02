import os
import urllib.request

steampath = "C:\\Program Files (x86)\\Steam\\steam.exe" #path to Steam
discordpath = "C:\\Users\\91959\\AppData\\Local\\Discord\\app-1.0.9002\\discord.exe" #path to Discord
emailurl = "https://outlook.office365.com/mail/inbox" #link to my outlook email
email2url = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox" #link to my gmail
initurl = "https://init.mlh.io/challenges" #link to MLH INIT's challenges for the day

while True:
    if input("Waiting for F... ") == 'F':
        #opening everything
        os.startfile(steampath)
        os.startfile(discordpath)
        res1 = urllib.request.urlopen(emailurl)
        res2 = urllib.request.urlopen(email2url)
        res3 = urllib.request.urlopen(initurl)
