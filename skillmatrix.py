from jobskill import JobSkill


class SkillMatrix(object):
    def __init__(self, formal_tone=True):
        self._formal_tone   = formal_tone
        self._matrix        = {}

    def set_formal_tone(self, formal_tone):
        self._formal_tone = formal_tone

    def add_skill(self, reference, skill):
        if (self._matrix.has_key(reference)):
            self._matrix[reference].add_response(skill)
        else:
            self._matrix[reference] = JobSkill(skill)
        
    def populate_skills(self):
        if (self._formal_tone):
            '''
            cpp = JobSkill("learning C++ through additional study")
            cpp.add_response("working with C++")
            self.add_skill("cpp", cpp)
            
            
            self.add_skill("manage_edits", JobSkill("manage editing, plan strategy"))
            self.add_skill("edits", JobSkill("providing copy for client comms"))
            self.add_skill("bi", JobSkill("data analysis and report writing"))
            self.add_skill("oo", JobSkill("object-oriented design"))
            self.add_skill("unreal", JobSkill("learning unreal"))
            self.add_skill("vers", JobSkill("working with version control via git, svn and perforce"))
            self.add_skill("journ", JobSkill("journalism, interviewings and event coverage"))
            self.add_skill("story", JobSkill("writing stories"))
            self.add_skill("db", JobSkill("database design, query writing"))
            self.add_skill("reports", JobSkill("report writing"))
            self.add_skill("modelling", JobSkill("blender"))
            self.add_skill("python", JobSkill("python"))
            self.add_skill("java", JobSkill("python"))
            self.add_skill("programming", JobSkill("programming"))
            self.add_skill("degree", JobSkill("a degree in computing science"))
            self.add_skill("games", JobSkill("I'm extremely passionate about Games"))
            self.add_skill("challenge", JobSkill("challenge"))
            self.add_skill("award", JobSkill("award"))
            self.add_skill("nano", JobSkill("ML for nanowrimo"))
            self.add_skill("reports", JobSkill("report design"))
            self.add_skill("writing", JobSkill("love write"))
            self.add_skill("clients", JobSkill("clients"))
            self.add_skill("blog", JobSkill("Australian Writer\'s Centre\'s Best Blogs"))
            '''
            
        else:
            self.add_skill("cpp", "using C++ in practical personal projects in my spare time")
            self.add_skill("cpp", "learned at university and continued to use in hobby projects")
            
            
            '''
            self.add_skill("manage_edits", JobSkill("manage editing, plan strategy"))
            
            self.add_skill("edits", JobSkill("editing a blog"))
            self.add_skill("bi", JobSkill("BI consulting"))
            self.add_skill("oo", JobSkill("object-oriented design"))
            self.add_skill("unreal", JobSkill("learning unreal"))
            self.add_skill("vers", JobSkill("working with version control via git, svn and perforce"))
            self.add_skill("journ", JobSkill("journalism, interviewings and event coverage"))
            self.add_skill("story", JobSkill("writing stories"))
            self.add_skill("db", JobSkill("database design, query writing"))
            self.add_skill("reports", JobSkill("report writing"))
            self.add_skill("modelling", JobSkill("blender"))
            self.add_skill("python", JobSkill("python"))
            self.add_skill("java", JobSkill("python"))
            self.add_skill("programming", JobSkill("programming"))
            self.add_skill("degree", JobSkill("I have a Bachelor of Science in Computing Science"))
            self.add_skill("games", JobSkill("games"))
            self.add_skill("challenge", JobSkill("challenge"))
            self.add_skill("award", JobSkill("award"))
            self.add_skill("nano", JobSkill("ML for nanowrimo"))
            self.add_skill("reports", JobSkill("report design"))
            self.add_skill("writing", JobSkill("love write"))
            self.add_skill("clients", JobSkill("clients"))
            self.add_skill("blog", JobSkill("Australian Writer\'s Centre\'s Best Blogs"))
            '''

    def get_skill(self, reference):
        if (self._matrix.has_key(reference)):
            return self._matrix[reference]
        return ""
        
    '''Return the available skills to choose from'''
    def list_skills(self):
        return list(self._matrix.keys())
        
        
