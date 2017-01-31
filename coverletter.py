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
            if (self._tone == row[1].strip()):
                if (self._phrases.has_key(row[0])):
                    self._phrases[row[0]].append(row[2].strip('"'))
                else:
                    self._phrases[row[0]] = [row[2].strip('"')]

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
        self.add_to_content(self.get_introduction() 
            % (self._skillset.get_name(), self._skillset.get_position()))
        self.add_to_content("\n\n")
        
        stage = 1
        for skill in self.get_matching_skills():
            if (stage == 1):
                self.add_to_content("lead: %s\n" % (skill))
                self.add_to_content(self.get_lead())
                self.add_to_content("\n\n")
                stage = 2
            elif (stage == 2):
                self.add_to_content("middling: %s\n" % (skill))
                self.add_to_content(self.get_middling())
                self.add_to_content("\n\n")
                stage = 3
            elif (stage == 3):
                self.add_to_content("hook: %s\n" % (skill))
                self.add_to_content(self.get_hook())
                self.add_to_content("\n\n")
                stage = 4
            elif (stage == 4):
                self.add_to_content("close: %s\n" % (skill))
                self.add_to_content(self.get_close())
                self.add_to_content("\n\n")
                stage = 5
            else:
                self.add_to_content("supp:")
                self.add_to_content("*")

        # end content

    def add_to_content(self, text):
        self._content += text
        
    def get_content(self):
        return self._content
