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
      Log.info('Trying to get a Selfie');
      this.config.args = handler.args;
      this.config.message = handler.message;
      this.config.callbacks = handler.callbacks;
      if (this.config.args != "")
      {
        this.config.new_status = this.config.args;
      }
      else
      {
        this.config.new_status = this.config.message.substr(7);
      }
    	handler.reply('TEXT','Trying to get a selfie with message ' + this.config.new_status,{parse_mode:'Markdown'});
    	this.sendSocketNotification('SELFIE', this.config);
 	},
 	cmd_facebook : function (command, handler)
	{
    	Log.info('Trying to get a selfie to Facebook');
      this.config.args = handler.args;
      this.config.message = handler.message;
      this.config.callbacks = handler.callbacks;
      if (this.config.args != "")
      {
        this.config.new_status = this.config.args;
      }
      else
      {
        this.config.new_status = this.config.message.substr(9);
      }
    	handler.reply('TEXT','Trying to get a selfie to Facebook with message ' + this.config.new_status,{parse_mode:'Markdown'});
    	this.sendSocketNotification('SELFIE_FACEBOOK', this.config);
 	},
	cmd_twitter : function (command, handler)
	{
    	Log.info('Trying to get a selfie to Twitter');
      this.config.args = handler.args;
      this.config.message = handler.message;
      this.config.callbacks = handler.callbacks;
      if (this.config.args != "")
      {
        this.config.new_status = this.config.args;
      }
      else
      {
        this.config.new_status = this.config.message.substr(8);
      }
    	handler.reply('TEXT','Trying to get a selfie to Twitter with message ' + this.config.new_status,{parse_mode:'Markdown'});
    	this.sendSocketNotification('SELFIE_TWITTER', this.config);
 	},
 	cmd_tumblr : function (command, handler)
	{
    	Log.info('Trying to get a selfie to Tumblr');
      this.config.args = handler.args;
      this.config.message = handler.message;
      this.config.callbacks = handler.callbacks;
      if (this.config.args != "")
      {
        this.config.new_status = this.config.args;
      }
      else
      {
        this.config.new_status = this.config.message.substr(7);
      }
    	handler.reply('TEXT','Trying to get a selfie to Tumblr with message ' + this.config.new_status,{parse_mode:'Markdown'});
    	this.sendSocketNotification('SELFIE', this.config);
 	},
 	cmd_instagram : function (command, handler)
	{
      Log.info('Trying to get a selfie to Instagram');
      this.config.args = handler.args;
      this.config.message = handler.message;
      this.config.callbacks = handler.callbacks;
      if (this.config.args != "")
      {
        this.config.new_status = this.config.args;
      }
      else
      {
        this.config.new_status = this.config.message.substr(10);
      }
      handler.reply('TEXT','Trying to get a selfie to Instagram with message ' + this.config.new_status,{parse_mode:'Markdown'});
      this.sendSocketNotification('SELFIE', this.config);
 	},

	start: function()
	{
	  Log.info('Starting module: ' + this.name);
	}
});
