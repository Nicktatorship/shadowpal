import random

class JobSkill(object):
    def __init__(self, response=""):
        self._responses = [response]
        self._scale     = 1

    def add_response(self, response):
        self._responses.append(response)
        
    def __str__(self):
        return random.choice(self._responses)
        
    ''' An adjective for skill strength, scale from 1 to 5 '''
    def get_scale(self):
        if (self._scale == 1):
            return "familiarity with"
        elif (self._scale == 2):
            return "comfortable with"
        elif (self._scale == 3):
            return "competencies in"
        elif (self._scale == 4):
            return "confident in"
        else:
            return "experienced with"
        
    