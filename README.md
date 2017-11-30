# MMM-Selfie
This an extension for the [MagicMirror](https://github.com/MichMich/MagicMirror). It provides selfie taking and uploading to several social websites.

## Usage
You need to use [MMM-Assistant](https://github.com/eouia/MMM-Assistant) to run the different commands.

The entry in config.js can look like the following. (NOTE: You only have to add the variables to config if want to change its standard value.)

```
{
	module: 'MMM-Selfie',
	config:
	{
		useFacebook: false,
		Facebook_pageid: "",
		Facebook_token: "",
		twitter_access_key: "",
		twitter_access_secret: "",
		twitter_consumer_key: "",
		twitter_consumer_secret: "",
		twitter_new_status: "",
		useInstagram: false,
		instagramUsername: "",
		instagramPassword: "",
		useTwitter: "",
		twitterOauthFile: "",
		useTumblr: false,
		tumblrOauthFile: "",
		useUSBCam: false,
		maxResY: 800,
		maxResX: 800

		// 1=LBPH | 2=Fisher | 3=Eigen
		// recognitionAlgorithm: 1,
		// Threshold for the confidence of a recognized face before it's considered a
		// positive match.  Confidence values below this threshold will be considered
		// a positive match because the lower the confidence value, or distance, the
		// more confident the algorithm is that the face was correctly detected.
		// lbphThreshold: 50,
		// fisherThreshold: 250,
		// eigenThreshold: 3000,
		// force the use of a usb webcam on raspberry pi (on other platforms this is always true automatically)
		// useUSBCam: false,
		// Path to your training xml
		// trainingFile: 'modules/MMM-Facial-Recognition/training.xml',
		// recognition intervall in seconds (smaller number = faster but CPU intens!)
		// interval: 2,
		// Logout delay after last recognition so that a user does not get instantly logged out if he turns away from the mirror for a few seconds
		// logoutDelay: 15,
		// Array with usernames (copy and paste from training script)
		// users: [],
		// Module set used for strangers and if no user is detected
		// defaultClass: "default",
		//Set of modules which should be shown for every user
		// everyoneClass: "everyone",
		// Boolean to toggle welcomeMessage
		// welcomeMessage: true
	}
}
```

## Dependencies
- [python-shell](https://www.npmjs.com/package/python-shell) (installed via `npm install`)

## Open Source Licenses
The MIT License (MIT)

Copyright (c) 2017 Alberto de Tena Rojas

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
