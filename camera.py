import time
import picamera
from datetime import datetime

class Camera():
	
		
	def capture(self):
		try:
			self.file_dir = f"image/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.png"
			with picamera.PiCamera() as camera:
				camera.resolution = (416, 416)
				camera.capture('static/'+self.file_dir)
				print(f"Image captured successfully at {self.file_dir}.")
			return self.file_dir
		except Exception as e:
			print("Image capture failed")
			return "image/fail"
		
	def preview(self):
		try:
			with picamera.PiCamera() as camera:
				camera.resolution = (640, 480)
				camera.start_preview()
				time.sleep(5)  # Allow time for the camera to warm up and adjust settings
				camera.stop_preview()
				print("Preview successful.")
		except Exception as e:
			print("Preview failed:", e)

