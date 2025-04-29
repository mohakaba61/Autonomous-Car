from flask_cors import CORS
from flask import Flask, jsonify, request
from time import sleep
import json

from detect import detect

from picarx import Picarx

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")

px = Picarx()

@app.route('/move-forward', methods=['POST'])
def move_forward():

    data = request.json
    power = data["power"]
    time = data["time"]

    print(f"Power: {power}, Time: {time}")

    px.forward(power)
    sleep(time)
    px.forward(0)

    return jsonify({"status": "OK" })

@app.route('/move-right', methods=['POST'])
def move_right():

    data = request.json
    power = data["power"]
    time = data["time"]

    px.forward(power)
    px.set_dir_servo_angle(30)
    sleep(time)
    px.set_dir_servo_angle(0)
    px.forward(0)

    return jsonify({"status": "OK" })

@app.route('/move-left', methods=['POST'])
def move_left():

    data = request.json
    power = data["power"]
    time = data["time"]

    px.forward(power)
    px.set_dir_servo_angle(-30)
    sleep(time)
    px.set_dir_servo_angle(0)
    px.forward(0)

    return jsonify({"status": "OK" })

@app.route('/move-backward', methods=['POST'])
def move_backward():

    data = request.json
    power = data["power"]
    time = data["time"]

    px.backward(power)
    sleep(time)
    px.backward(0)

    return jsonify({"status": "OK" })

@app.route('/object-detection', methods=['GET'])
def object_detection():

    detections = detect()

    return jsonify({"object-detection": detections})

@app.route('/cliff-detection', methods=['GET'])
def cliff_detection():
    
    px.set_cliff_reference([200, 200, 200])
    gm_val_list = px.get_grayscale_data()
    gm_state = px.get_cliff_status(gm_val_list)

    return jsonify({"cliff-detection": gm_state})

@app.route('/distance', methods=['GET'])
def get_distance():
    
    distance = px.ultrasonic.read()

    return jsonify({"distance": distance})

if __name__ == '__main__':
    
    app.run(host='0.0.0.0')
    
    # debug=True runs the server twice much like nodejs
