from skillmatrix import SkillMatrix
from joblisting import JobListing
from paragraph import Paragraph
from random import shuffle

import random
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
                    self._phrases[row[0]].add_phrase(row[2].strip('"'))
                else:
                    self._phrases[row[0]] = Paragraph(row[2].strip('"'), row[3].strip())

    def get_matching_skills(self):
        match_list = list(set(self._job.get_skills()) & set(self._skillset.list_skills()))
        shuffle(match_list)
        return match_list

    def parse_phrase(self, key="intro", subs=[]):
        return self._phrases[key].get_parsed_content(subs)
        
    def compile(self):
        closing   = ""
        has_close = False
        
        self.populate_phrases()
        self.add_to_content(self.parse_phrase("intro", (
                self._skillset.get_name(), 
                self._skillset.get_position(),
                self._job.get_title(),
                self._job.get_company()
            )))

        stage = 1
        for skill in self.get_matching_skills():
            if (stage == 1):
                self.add_to_content(self.parse_phrase("lead", (self._skillset.get_skill(skill).get_response(), self._skillset.get_skill(skill).get_supplement())))
                stage = 2
            elif (stage == 2):
                self.add_to_content(self.parse_phrase("middling", (self._skillset.get_skill(skill).get_response(), self._skillset.get_skill(skill).get_supplement())))
                stage = 3
            elif (stage == 3):
                self.add_to_content(self.parse_phrase("hook", (self._skillset.get_skill(skill).get_response(), self._skillset.get_skill(skill).get_supplement())))
                if (has_close):
                    stage = 1
                else:
                    stage = 4
            elif (stage == 4):
                has_close = True
                closing = self.parse_phrase("close", (self._skillset.get_skill(skill).get_response(), self._skillset.get_skill(skill).get_supplement()))
                stage = 1

        # end content
        if (has_close):
            self.add_to_content(closing)

    def add_to_content(self, text):
        self._content += text
        
    def get_content(self):
        return self._content
