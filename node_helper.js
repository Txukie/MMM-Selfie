'use strict';
const NodeHelper = require('node_helper');

const PythonShell = require('python-shell');
var pythonStarted = false

module.exports = NodeHelper.create({
  
  python_selfie: function () {
    const self = this;
    const pyshell = new PythonShell('modules/' + this.name + '/selfie/selfie.py', { mode: 'json', args: [JSON.stringify(this.config)]});
    
    pyshell.on('message', function (message)
    {  
      if (message.hasOwnProperty('status')){
      console.log("[" + self.name + "] " + message.status);
      }
    });

    pyshell.end(function (err)
    {
      if (err) throw err;
      console.log("[" + self.name + "] " + 'finished running...');
    });
  },

  python_selfie_facebook: function () {
    const self = this;
    const pyshell = new PythonShell('modules/' + this.name + '/selfie/selfie_facebook.py', { mode: 'json', args: [JSON.stringify(this.config)]});

    pyshell.on('message', function (message)
    {  
      if (message.hasOwnProperty('status')){
      console.log("[" + self.name + "] " + message.status);
      }
    });

    pyshell.end(function (err)
    {
      if (err) throw err;
      console.log("[" + self.name + "] " + 'finished running...');
    });
  },

  python_selfie_twitter: function () {
    const self = this;
    const pyshell = new PythonShell('modules/' + this.name + '/selfie/selfie_twitter.py', { mode: 'json', args: [JSON.stringify(this.config)]});

    pyshell.end(function (err)
    {
      if (err) throw err;
      console.log("[" + self.name + "] " + 'finished running...');
    });
  },
  
  // Subclass socketNotificationReceived received.
  socketNotificationReceived: function(notification, payload) {
    if(notification === 'SELFIE')
    {
      this.config = payload
      if(!pythonStarted)
      {
        pythonStarted = true;
        this.python_selfie();
      };
    };
    if(notification === 'SELFIE_FACEBOOK')
    {
      this.config = payload
      if(!pythonStarted)
      {
        pythonStarted = true;
        this.python_selfie_facebook();
      }
    };
    if(notification === 'SELFIE_TWITTER')
    {
      this.config = payload
      if(!pythonStarted)
      {
        pythonStarted = true;
        this.python_selfie_twitter();
      }
    };
  
  pythonStarted = false;

  }
  
});
