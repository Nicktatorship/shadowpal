from jobskill import JobSkill
import csv

class SkillMatrix(object):
    def __init__(self, name="Joe", position="VP", tone="formal"):
        self._tone      = tone
        self._name      = name
        self._position  = position
        self._matrix    = {}
        self.populate_skills()
        
    def get_name(self):
        return self._name
        
    def get_position(self):
        return self._position

    def add_skill(self, reference, skill, supplemental=""):
        if (self._matrix.has_key(reference)):
            self._matrix[reference].add_response(skill, supplemental)
        else:
            self._matrix[reference] = JobSkill(skill, supplemental)
        
    def populate_skills(self):
        csvfile = open('quals.csv')
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if row != []:
                if (self._tone == row[1].strip()):
                    self.add_skill(row[0], row[2].strip('"'), row[3].strip('"'))

    def get_skill(self, reference):
        if (self._matrix.has_key(reference)):
            return self._matrix[reference]
        return ""
        
    '''Return the available skills to choose from'''
    def list_skills(self):
        return list(self._matrix.keys())
        
    def show(self):
        print("Available Skills:")
        print(self.list_skills())
        print("\n")
    
        
