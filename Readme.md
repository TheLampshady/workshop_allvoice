1) Setup Env
# Install brew
# brew install python
# pip install virtualenv

2) Setup web server
virtualenv venv
. venv/bin/activate
pip install Flask
git+https://github.com/TheLampshady/all_voice.git

# Make webserver
export FLASK_APP=webby
flask run -p 8080


3) Open webserver to the world.
brew cask install ngrok

# We will choose a port with flask.
ngrok http 8080

# To quit
CTRL-C


API.AI
https://console.api.ai/