#!/bin/python
from app import app
app.run(host='0.0.0.0',threaded=True,debug=True,port=5003)