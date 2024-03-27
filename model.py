
import numpy as np
import os
import cv2
import numpy as np
import sys
import random
from datetime import datetime
from tflite_runtime.interpreter import Interpreter

class MyModel:
	def __init__(self):
	  self.timestamp = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
		
	def detect(self, image_path:str , min_conf=0.5):
	  lblpath   = "labelmap.txt"
	  modelpath = "custom_model_lite/detect.tflite"
	  savepath = 'static/results'
	  
	  image_result_path = f"results/images/{self.timestamp}.png"

	  with open(lblpath, 'r') as f:
		  labels = [line.strip() for line in f.readlines()]

	  interpreter = Interpreter(model_path=modelpath)
	  interpreter.allocate_tensors()

	  input_details = interpreter.get_input_details()
	  output_details = interpreter.get_output_details()
	  
	  height = input_details[0]['shape'][1]
	  width = input_details[0]['shape'][2]

	  float_input = (input_details[0]['dtype'] == np.float32)

	  input_mean = 127.5
	  input_std  = 127.5
	  
	  image_path = str(os.path.abspath('static/'+image_path))

	  image = cv2.imread(image_path)
	  imH, imW, _ = image.shape
	  print(imH,imW)
	  image_resized = cv2.resize(image, (width, height))
	  input_data = np.expand_dims(image_resized, axis=0)

	  if float_input:
		  input_data = (np.float32(input_data) - input_mean) / input_std

	  interpreter.set_tensor(input_details[0]['index'],input_data)
	  interpreter.invoke()

	  boxes = interpreter.get_tensor(output_details[1]['index'])[0] 
	  classes = interpreter.get_tensor(output_details[3]['index'])[0]
	  scores = interpreter.get_tensor(output_details[0]['index'])[0] 

	  detections = []

	  for i in range(len(scores)):
		  if ((scores[i] > min_conf) and (scores[i] <= 1.0)):

			  ymin = int(max(1,(boxes[i][0] * imH)))
			  xmin = int(max(1,(boxes[i][1] * imW)))
			  ymax = int(min(imH,(boxes[i][2] * imH)))
			  xmax = int(min(imW,(boxes[i][3] * imW)))

			  cv2.rectangle(image, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)

			  object_name = labels[int(classes[i])] 
			  label = '%s: %d%%' % (object_name, int(scores[i]*100)) 
			  labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) 
			  label_ymin = max(ymin, labelSize[1] + 10) 
			  cv2.rectangle(image, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) 
			  cv2.putText(image, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

			  detections.append([object_name, scores[i], xmin, ymin, xmax, ymax])

	  cv2.imwrite('static/'+image_result_path, image)
	  
	  image_fn = os.path.basename(image_path)
	  base_fn, ext = os.path.splitext(image_fn)
	  txt_result_fn = base_fn +'.txt'
	  txt_savepath = os.path.join(savepath, txt_result_fn)

	  with open(txt_savepath,'w') as f:	  
		  for detection in detections:
			  f.write('%s %.4f %d %d %d %d\n' % (detection[0], detection[1], detection[2], detection[3], detection[4], detection[5]))

	  return image_result_path
