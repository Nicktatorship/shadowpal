'''

The runner for all things ShadowPal. 

ShadowPal is your friend.

ShadowPal is here to help.

'''

from jobskill import JobSkill
from skillmatrix import SkillMatrix

a = SkillMatrix("informal")


req_list = ["sportsing", "pizza"]

for skillref in req_list:
    print (a.get_skill(skillref))
        