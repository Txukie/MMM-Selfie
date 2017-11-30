/* global Module */

/* Magic Mirror
 * Module: MMM-Selfie
 *
 * By Alberto de Tena Rojas http://albertodetena.com
 * MIT Licensed.
 */

Module.register('MMM-Selfie',
{
	defaults:
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
	},

	// Define required translations.
	getTranslations: function() {
		return {
			en: "translations/en.json",
      		es: "translations/es.json",
			fr: "translations/fr.json"
		};
	},

	getCommands : function(register) {
    if (register.constructor.name == 'TelegramBotCommandRegister') {
      register.add({
        command: 'selfie',
        description: this.translate("CMD_TELBOT_SELFIE"),
        callback: 'cmd_selfie'
      })
      register.add({
        command: 'facebook',
        description: this.translate("CMD_TELBOT_FACEBOOK"),
        callback: 'cmd_facebook'
      })
      register.add({
        command: 'twitter',
        description: this.translate("CMD_TELBOT_TWITTER"),
        callback: 'cmd_twitter',
      })
      register.add({
        command: 'tumblr',
        description: this.translate("CMD_TELBOT_TUMBLR"),
        callback: 'cmd_tumblr',
      })
      register.add({
        command: 'instagram',
        description: this.translate("CMD_TELBOT_INSTAGRAM"),
        callback: 'cmd_instagram',
      })
    }
    if (register.constructor.name == 'AssistantCommandRegister') {
      register.add({
        command: this.translate("CMD_ASSTNT_SELFIE"),
        description: this.translate("CMD_ASSTNT_SELFIE_DESCRIPTION"),
        callback: 'cmd_selfie'
      })
      register.add({
        command: this.translate("CMD_ASSTNT_FACEBOOK"),
        description: this.translate("CMD_ASSTNT_FACEBOOK_DESCRIPTION"),
        callback: 'cmd_facebook',
      })
      register.add({
        command: this.translate("CMD_ASSTNT_TWITTER"),
        description: this.translate("CMD_ASSTNT_TWITTER_DESCRIPTION"),
        callback: 'cmd_twitter',
      })
      register.add({
        command: this.translate("CMD_ASSTNT_TUMBLR"),
        description: this.translate("CMD_ASSTNT_TUMBLR_DESCRIPTION"),
        callback: 'cmd_tumblr',
      })
      register.add({
        command: this.translate("CMD_ASSTNT_INSTAGRAM"),
        description: this.translate("CMD_ASSTNT_INSTAGRAM_DESCRIPTION"),
        callback: 'cmd_instagram',
      })
    }
    },

    cmd_selfie : function (command, handler)
	{
    	Log.info('Trying to get a selfie');
    	handler.response('Trying to get a selfie');
    	this.sendSocketNotification('SELFIE', this.config);
  	},
  	cmd_facebook : function (command, handler)
	{
    	Log.info('Trying to get a selfie to Facebook');
    	handler.response('Trying to get a selfie to Facebook');
    	this.sendSocketNotification('SELFIE_FACEBOOK', this.config);
  	},
  	cmd_twitter : function (command, handler)
	{
    	Log.info('Trying to get a selfie to Twitter');
    	handler.response('Trying to get a selfie to Twitter');
    	this.sendSocketNotification('SELFIE_TWITTER', this.config);
  	},
  	cmd_tumblr : function (command, handler)
	{
    	Log.info('Trying to get a selfie to Tumblr');
    	handler.response('Trying to get a selfie to Tumblr');
    	this.sendSocketNotification('SELFIE', this.config);
  	},
  	cmd_instagram : function (command, handler)
	{
    	Log.info('Trying to get a selfie to Instagram');
    	handler.response('Trying to get a selfie to Instagram');
    	this.sendSocketNotification('SELFIE', this.config);
  	},

	start: function()
	{
		//this.sendSocketNotification('CONFIG', this.config);
		Log.info('Starting module: ' + this.name);
	}
});
