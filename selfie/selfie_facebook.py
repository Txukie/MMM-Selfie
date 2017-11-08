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
import facebook

def to_node(type, message):
    # convert to json and print (node helper will read from stdout)
    try:
        print(json.dumps({type: message}))
    except Exception:
        pass
    # stdout has to be flushed manually to prevent delays in the node helper communication
    sys.stdout.flush()


to_node("status", "Selfie module started...")
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
    to_node("status", 'Selfie taken for Facebook')
    return filename


def postonfb(filename):
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : config.get("Facebook_pageid")
    "access_token" : config.get("Facebook_token")
    }

  FACEBOOK_PROFILE_ID = ''
  api = get_api(cfg)
  msg = "Probando la API de Facebook con Python!"

  try:
    #fb_response = api.put_wall_post('Hello from Python',profile_id = FACEBOOK_PROFILE_ID)
    fb_response = api.put_photo(image=open(filename, 'rb'),message='Testing python API with this stupid photo!')
    print(fb_response)

  except facebook.GraphAPIError as e:
    print('Something went wrong:' + e.type + e.message)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip 
  # the following if you want to post as yourself. 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3

if __name__ == "__main__":
  filename = takeSelfie()
  postonfb(filename)

