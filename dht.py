import Adafruit_DHT

class MyDHT():
	
	def __init__(self,dhtPin:int = 4):
		self.pin = dhtPin
		
	def capture(self):
		sensor = Adafruit_DHT.DHT11
		
		try:
			humidity, temperature = Adafruit_DHT.read_retry(sensor, self.pin)
			if humidity is not None and temperature is not None:
				print(f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%")
				print("DHT11 sensor test successful.")
			else:
				print("Failed to retrieve data from DHT11 sensor.")
			return humidity, temperature
		except Exception as e:
			print("DHT11 sensor test failed:", e)
			return -1,-1
