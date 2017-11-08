#!/usr/bin/python
# coding: utf8
"""MMM-Selfie - MagicMirror Module
Selfie Script
The MIT License (MIT)

Copyright (c) 2017 Alberto de Tena Rojas (MIT License)
Based on work by Tony DiCola (Copyright 2013) (MIT License)
Based on work by Paul-Vincent Roll (Copyright 2016) (MIT License)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import sys
import json
import time
import config
import picamera
import signal
import datetime

def to_node(type, message):
    # convert to json and print (node helper will read from stdout)
    try:
        print(json.dumps({type: message}))
    except Exception:
        pass
    # stdout has to be flushed manually to prevent delays in the node helper communication
    sys.stdout.flush()


to_node("status", "Selfie module started...")

# Setup variables


# Load training data into model
to_node("status", 'Loading user data...')

# set algorithm to be used based on setting in config.js
if config.get("useFacebook"):
    to_node("status", "Initializing Facebook submodule")
    #model = cv2.createLBPHFaceRecognizer(threshold=config.get("lbphThreshold"))
if config.get("useInstagram"):
    to_node("status", "Initializing Instagram submodule")
    #model = cv2.createFisherFaceRecognizer(threshold=config.get("fisherThreshold"))
if config.get("useTwitter"):
    to_node("status", "Initializing Twitter submodule")
    #model = cv2.createEigenFaceRecognizer(threshold=config.get("eigenThreshold"))
if config.get("useTumblr"):
    to_node("status", "Initializing Tumblr submodule")
    #model = cv2.createEigenFaceRecognizer(threshold=config.get("eigenThreshold"))

# get camera
camera = config.get_camera()

def shutdown(self, signum):
    to_node("status", 'Shutdown: Cleaning up camera...')
    camera.close()
    quit()

signal.signal(signal.SIGINT, shutdown)

# sleep for a second to let the camera warm up
time.sleep(1)


def takeSelfie():
    filename = config.path_to_file + '/selfie_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
    image = camera.capture(filename)
    to_node("status", 'Selfie taken')


# Main Loop
#while True:
    # Sleep for x seconds specified in module config
#    time.sleep(30)
    # if detecion is true, will be used to disable detection if you use a PIR sensor and no motion is detected
takeSelfie()
