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
import pygame
import facebook
from twitter import *

def to_node(type, message):
    # convert to json and print (node helper will read from stdout)
    try:
        print(json.dumps({type: message}))
    except Exception:
        pass
    # stdout has to be flushed manually to prevent delays in the node helper communication
    sys.stdout.flush()

# get Picamera or webcam
camera = config.get_camera()

def shutdown():
    to_node("status", 'Shutdown: Cleaning up camera...')
    camera.close()
    quit()

signal.signal(signal.SIGINT, shutdown)

def postontwitter(filename):
    cfg = {
        "access_key"      : config.get("twitter_access_key"),
        "access_secret"   : config.get("twitter_access_secret"),
        "consumer_key"    : config.get("twitter_consumer_key"),
        "consumer_secret" : config.get("twitter_consumer_secret"),
        "new_status"      : config.get("new_status")
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

def get_fb_api(cfg):
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

def postonfb(filename):
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : config.get("Facebook_pageid"),
    "access_token" : config.get("Facebook_token"),
    "new_status"   : config.get("new_status"),
    "profile_id"   : config.get("Facebook_ProfileId")
    }

  FACEBOOK_PROFILE_ID = cfg["profile_id"]
  api = get_fb_api(cfg)
  msg = cfg["new_status"]

  try:
    #fb_response = api.put_wall_post('Hello from Python',profile_id = FACEBOOK_PROFILE_ID)
    fb_response = api.put_photo(image=open(filename, 'rb'),message=msg,profile_id = FACEBOOK_PROFILE_ID)
    print(fb_response)

  except facebook.GraphAPIError as e:
    print('Something went wrong:' + e.type + e.message)

def takeSelfie():
    pygame.init()
    pygame.mixer.music.load(config.path_to_file + "/../resources/shutter.mp3")
    filename = config.path_to_file + '/selfie_' + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '.jpg'
    camera.start_preview()
    time.sleep(3)
    pygame.mixer.music.play()
    image = camera.capture(filename)
    camera.stop_preview()
    to_node("status", 'Selfie taken')
    return filename

# Main Loop
photofile = takeSelfie()
postontwitter(photofile)
shutdown()
