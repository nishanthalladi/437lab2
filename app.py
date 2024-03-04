from flask import Flask
from flask import render_template
from flask import request, jsonify
from Motor import *
import time
from flask_cors import CORS

PWM = Motor()

from Ultrasonic import *
ultrasonic=Ultrasonic()

from gpiozero import CPUTemperature
cpu = CPUTemperature()

app = Flask(__name__)
CORS(app)

commands_recieved = 0

def get_info():
    global commands_recieved
    commands_recieved += 1
    return {"distance": ultrasonic.get_distance(), "temperature": cpu.temperature, "commands": commands_recieved}

@app.route('/forward', methods=["GET", "POST"])
def forward():
    PWM.setMotorModel(1000,1000,1000,1000)
    time.sleep(1)
    PWM.setMotorModel(0,0,0,0)
    return get_info()

@app.route('/backward', methods=["GET", "POST"])
def backward():
    PWM.setMotorModel(-1000,-1000,-1000,-1000)
    time.sleep(1)
    PWM.setMotorModel(0,0,0,0)
    return get_info()

@app.route('/left', methods=["GET", "POST"])
def left():
    PWM.setMotorModel(-500,-500,2000,2000)
    time.sleep(0.5)
    PWM.setMotorModel(0,0,0,0)
    return get_info()

@app.route('/right', methods=["GET", "POST"])
def right():
    PWM.setMotorModel(2000,2000,-500,-500)
    time.sleep(0.5)
    PWM.setMotorModel(0,0,0,0)
    return get_info()

if __name__ == '__main__':
    app.run( host='192.168.0.190', port = 5000, debug=True)

