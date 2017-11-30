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
import os
from twitter import *


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
    to_node("status", 'Selfie taken for Twitter')
    return filename

def postontwitter(filename):
    cfg = {
        "access_key"      : config.get("twitter_access_key"),
        "access_secret"   : config.get("twitter_access_secret"),
        "consumer_key"    : config.get("twitter_consumer_key"),
        "consumer_secret" : config.get("twitter_consumer_secret"),
        "new_status"      : config.get("twitter_new_status")
    }

    #-----------------------------------------------------------------------
    # create twitter API objects
    #-----------------------------------------------------------------------
    twitter_upload = Twitter(domain='upload.twitter.com',
        auth = OAuth(cfg["access_key"], cfg["access_secret"], cfg["consumer_key"], cfg["consumer_secret"]))

    #-----------------------------------------------------------------------
    # post a new status
    # twitter API docs: https://dev.twitter.com/rest/reference/post/statuses/update
    #-----------------------------------------------------------------------

    with open(filename, "rb") as imagefile:
        imagedata = imagefile.read()

    filesize = os.path.getsize(filename)

    id_img = twitter_upload.media.upload(command="INIT",total_bytes=filesize,media_type='image/jpeg')["media_id_string"]
    twitter_upload.media.upload(command="APPEND",media_id=id_img,segment_index=0,media=imagedata)
    twitter_upload.media.upload(command="FINALIZE",media_id=id_img)

    twitter_post = Twitter(
        auth = OAuth(cfg["access_key"], cfg["access_secret"], cfg["consumer_key"], cfg["consumer_secret"]))

    results = twitter_post.statuses.update(status = cfg["new_status"], media_ids = id_img)

    print "updated status: %s" % cfg["new_status"]

if __name__ == "__main__":
      filename = takeSelfie()
      postontwitter(filename)