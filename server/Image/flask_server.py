from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2

# Initialize the Flask application
app = Flask(__name__)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# route http posts to this method
@app.route('/facedetect', methods=['POST'])
def test():
	r = request
	# convert string of image data to uint8
	nparr = np.fromstring(r.data, np.uint8)
	# decode image
	img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

	# build a response dict to send back to client
	response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])}
	print(response)

	faces = face_cascade.detectMultiScale(img, 1.1, 4)
	rs = dict()
	for (idx, face) in enumerate(faces):
	    rs[idx] = {'x': str(face[0]), 'y': str(face[1]), 'w': str(face[2]), 'h': str(face[3])}
	print(jsonpickle.encode(rs))

	# encode response using jsonpickle
	response_pickled = jsonpickle.encode(rs)

	return Response(response=response_pickled, status=200, mimetype="application/json")

# route http posts to this method
@app.route('/', methods=['GET'])
def test2():
	return "hello"


# start flask app
app.debug=True
app.run(host="0.0.0.0", port=5000)
