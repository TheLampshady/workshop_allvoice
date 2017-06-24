import json
import logging
from flask import Flask, request, make_response

from skill import MySkill

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
	event = request.get_json(silent=True, force=True)

	# Logging
	print("Request:")
	print(json.dumps(event, indent=4))

	# Process Skill
	my_skill = MySkill(event)
	paylaod = json.dumps(my_skill.response())
	resp = make_response(paylaod)
	resp.headers['Content-Type'] = 'application/json'
	return resp