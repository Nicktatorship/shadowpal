from skillmatrix import SkillMatrix
from joblisting import JobListing

class CoverLetter(object):
    def __init__(self, job, skillset, tone="formal"):
        self._skillset  = skillset
        self._job       = job
        self._tone      = tone
        
        self._introduction  = ""
        self._lead          = ""
        self._hook          = ""
        self._close         = ""
        
    def set_introduction(self):
        self._introduction = ""

    def set_lead(self):
        self._lead = ""
        
    def set_hook(self):
        self._hook = ""
        
    def set_close(self):
        self._close = ""
        
    def compile(self):
        return self._job.get_title()