import random

class JobSkill(object):
    def __init__(self, response="", supplement=""):
        self._responses     = [response]
        self._response      = response
        self._supplements   = [supplement]
        self._supplement    = supplement
        self._scale     = 1

    def add_response(self, response="", supplement=""):
        if response != "":
            self._responses.append(response)
            
        if supplement != "":
            self._supplements.append(supplement)
            
        self._response      = random.choice(self._responses)
        self._supplement    = random.choice(self._supplements)
        
    def __str__(self):
        return self.get_response()
        
    def get_response(self):
        return self._response
        
    def get_supplement(self):
        return self._supplement

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
        
    