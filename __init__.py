from mycroft import MycroftSkill, intent_file_handler


class AskDawn(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dawn.ask.intent')
    def handle_dawn_ask(self, message):
        self.speak_dialog('dawn.ask')


def create_skill():
    return AskDawn()

