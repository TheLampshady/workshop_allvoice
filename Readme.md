# Setup Environment
We will be intalling Python for our webservice and ngrok for making our work accessible.

* Install brew
	* `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* Install ngrok
	* `brew cask install ngrok`
* Install python
	* `brew install python`
	* `pip install virtualenv`

# Setup Web-Server
* (optinal) Virtual Evironments
	* `virtualenv venv`
	* `. venv/bin/activate`
* Install project libraries
	* `pip install Flask`
	* `pip install git+https://github.com/TheLampshady/all_voice.git`
* Build your Flask App

# Run Web-Server
To run your flask app, export the name of your python file to FLASK_APP and run it on an unused port with reload.

* `export FLASK_APP=webby.py`
* `flask run -p 9000 --reload`

Test the site works by visiting the homepage. [http://localhost:9000](http://localhost:9000)

Lets open our app up to the world:
`ngrok http 9000 `

We will copy the https url in the webhook sections of api.ai and alexa later with the webhook path.

Example:
`https://c9850c67.ngrok.io/webhook`

# Skills to Setup
## Alexa
[https://developer.amazon.com/edw/home.html](https://developer.amazon.com/edw/home.html)

* Set a name for your app.
* Add intents and utterances
* Configurations
	* HTTPS -> NA
	* Enter `https://c9850c67.ngrok.io/webhook`
	* Next
* SSL `My development endpoint is a sub-domain ....`

## API.AI
[https://console.api.ai/](https://console.api.ai/)

Add url to fullfilment 
