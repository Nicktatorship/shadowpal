from skillmatrix import SkillMatrix
from joblisting import JobListing
from random import shuffle
import csv

class CoverLetter(object):
    def __init__(self, job, skillset, tone="formal"):
        self._skillset  = skillset
        self._job       = job
        self._tone      = tone
        self._phrases   = {}
        self._content   = ""
        self.compile()

    def populate_phrases(self):
        csvfile = open('fills.csv')
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if (self._tone == row[2].strip()):
                if (self._phrases.has_key(row[0])):
                    self._phrases[row[0]].append(row[1].strip('"'))
                else:
                    self._phrases[row[0]] = [row[1].strip('"')]

    def get_matching_skills(self):
        match_list = list(set(self._job.get_skills()) & set(self._skillset.list_skills()))
        # shuffle(match_list)
        return match_list

    def get_introduction(self):
        shuffle(self._phrases["intro"])
        return self._phrases["intro"][0]

    def get_lead(self):
        shuffle(self._phrases["lead"])
        return self._phrases["lead"][0]

    def get_middling(self):
        shuffle(self._phrases["middling"])
        return self._phrases["middling"][0]
        
    def get_hook(self):
        shuffle(self._phrases["hook"])
        return self._phrases["hook"][0]

    def get_close(self):
        shuffle(self._phrases["close"])
        return self._phrases["close"][0]
        
    def compile(self):
        self.populate_phrases()
        self.add_to_content(self.get_introduction())
        self.add_to_content("\n\n")
        self.add_to_content(self.get_lead())
        self.add_to_content("\n\n")
        self.add_to_content(self.get_middling())
        self.add_to_content("\n\n")
        self.add_to_content(self.get_hook())
        self.add_to_content("\n\n")
        self.add_to_content(self.get_close())
        
        # end content

    def add_to_content(self, text):
        self._content += text
        
    def get_content(self):
        return self._content
