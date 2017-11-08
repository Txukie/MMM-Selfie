#!/usr/bin/python
# coding: utf8
"""MMM-Selfie - MagicMirror Module
Selfie script config
The MIT License (MIT)

Copyright (c) 2017 Alberto de Tena Rojas (MIT License)
Based on work by Tony DiCola (Copyright 2013) (MIT License)
Based on work by Paul-Vincent Roll (Copyright 2016) (MIT License)
"""
import inspect
import os
import json
import sys
import platform


def to_node(type, message):
    print(json.dumps({type: message}))
    sys.stdout.flush()


_platform = platform.uname()[4]
path_to_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

CONFIG = json.loads(sys.argv[1]);

def get(key):
    return CONFIG[key]

def get_camera():
    to_node("status", "-" * 20)
    try:
        if get("useUSBCam") == False:
            import picamera
            camera = picamera.PiCamera()
            return camera
        else:
            raise Exception
    except Exception:
        import webcam
        to_node("status", "Webcam selected...")
        return webcam.OpenCVCapture(device_id=0)
    to_node("status", "-" * 20)
