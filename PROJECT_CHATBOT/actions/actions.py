from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted

class ActionHandleFallback(Action):
    def name(self):
        return "action_handle_fallback"

    async def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(text="désolé, je ne comprends pas votre question")
        return [UserUtteranceReverted()]
