import random

class Paragraph(object):
    def __init__(self, phrase="", positions=0):
        self._phrases   = [phrase]
        self._positions = int(positions)
        self._phrase    = phrase
        
    def add_phrase(self, phrase):
        self._phrases.append(phrase)
        self._phrase = random.choice(self._phrases)
        
    def __str__(self):
        return self._phrase

    def get_inserts(self):
        return self._phrase
        
    def get_parsed_content(self, subs=()):
        if (self._positions == 0):
            return (self._phrase + '\n')
        elif (self._positions == len(subs)):
            return ((self._phrase) % (subs)) + '\n'
        else:
            return (self._phrase + '\n')

                