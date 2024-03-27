from flask import Flask
from flask import render_template
import datetime
from camera import Camera
from dht import MyDHT
from model import MyModel

# import sqlite3

app = Flask(__name__)

dht = MyDHT()
cam = Camera()
mod = MyModel()

@app.route('/')
def index():
	humidity, temperature = dht.capture()
	img_path  = cam.capture()
	pred_path = mod.detect(img_path)
	
	return render_template(
		'index.html',
		hum = humidity, 
		temp = temperature, 
		cap_path = img_path,
		pre_path = pred_path
	)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

