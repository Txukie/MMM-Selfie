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
	    useUSBCam: false,
	    maxResX: 2592,
	    maxResY: 1944,
	    cameraRotation: 0,
	    Facebook_pageid: '',
	    Facebook_token: '',
	    Facebook_ProfileId: '',
	    twitter_access_key: '',
	    twitter_access_secret: '',
	    twitter_consumer_key: '',
	    twitter_consumer_secret: ''
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
