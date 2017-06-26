API_AI_ZIP=api_ai.zip
zip-google-all:
	rm -f $(API_AI_ZIP)
	cd speech_assets/api_ai/ && zip -r $(API_AI_ZIP) *
	mv speech_assets/api_ai/$(API_AI_ZIP) .
	chmod 644 $(API_AI_ZIP)

zip-google-intent:
	rm -f $(API_AI_ZIP)
	cd speech_assets/api_ai/ && zip -r $(API_AI_ZIP) * -x *agent.json
	mv speech_assets/api_ai/$(API_AI_ZIP) .
	chmod 644 $(API_AI_ZIP)
