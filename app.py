from flask import Flask
from flask import render_template
from flask import request, jsonify
from Motor import *
import time

PWM = Motor()

app = Flask(__name__)
@app.route('/forward', methods=["GET", "POST"])
def forward():
    PWM.setMotorModel(1000,1000,1000,1000)
    time.sleep(2)
    PWM.setMotorModel(0,0,0,0)

@app.route('/backward', methods=["GET", "POST"])
def backward():
    PWM.setMotorModel(-1000,-1000,-1000,-1000)
    time.sleep(2)
    PWM.setMotorModel(0,0,0,0)

@app.route('/left', methods=["GET", "POST"])
def left():
    PWM.setMotorModel(-500,-500,2000,2000)
    time.sleep(0.5)
    PWM.setMotorModel(0,0,0,0)

@app.route('/right', methods=["GET", "POST"])
def right():
    PWM.setMotorModel(2000,2000,-500,-500)
    time.sleep(0.5)
    PWM.setMotorModel(0,0,0,0)

if __name__ == '__main__':
    app.run( host='192.168.0.190', port = 5000, debug=True)

