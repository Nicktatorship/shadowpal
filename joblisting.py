class JobListing(object):
    def __init__(self, company="", title="", skills=[]):
        self._company = company
        self._title = title
        self._skills = skills
        
    def get_skills(self):
        return self._skills
    
    def get_title(self):
        return self._title
        
    def get_company(self):
        return self._company
