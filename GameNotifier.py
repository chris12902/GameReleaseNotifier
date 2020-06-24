from urllib.request import Request, urlopen
import re
import winsound

def getServers(gameID):
    try:
        req = Request('https://games.roblox.com/v1/games/'+str(gameID)+'/servers/Public?sortOrder=Asc&limit=10', headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read().decode('utf-8')
        if ',{"id":' in webpage:
            return True
        else:
            return False
    except:
        return False
gameID = int(input("Input the place ID: "))
print("Do you want to be notified when the game releases using an alarm clock?\nThis would require that you shutdown the program to make it stop beeping.\nIf you select 'no', it will only beep once when the game releases.")
alarmClock = input("(y/n) ")
if 'y' in alarmClock.lower():
    alarmClock = True
else:
    alarmClock = False

released = False
print("Retrieving server info")
while getServers(gameID) == False:
    continue
print("its out lol")
while alarmClock:
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
