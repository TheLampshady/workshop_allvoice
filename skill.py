from all_voice.models import AllVoice

class MySkill(AllVoice):

	# ACTIONS
    def Intro(self):
	    text = "I appear in chats and Alexa cards"
	    speech_output = "I am speaking now!"
	    reprompt_text = "I want to talk more!"

	    return self.build_response(
	            text=text,
	            speech=speech_output,
	            reprompt=reprompt_text
        )