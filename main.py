from jobskill import JobSkill
from skillmatrix import SkillMatrix

a = SkillMatrix()
a.set_formal_tone(False)
a.populate_skills()
b = a.get_skill("cpp")
print a.list_skills()
print b

req_list = ["cpp", "oo", "team", "degree", "games", "challenge", "vers"]

for skillref in req_list:
    print (a.get_skill(skillref))
        