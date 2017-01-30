'''

The runner for all things ShadowPal. 

ShadowPal is your friend.

ShadowPal is here to help.

'''

from jobskill import JobSkill
from skillmatrix import SkillMatrix
from joblisting import JobListing
from coverletter import CoverLetter


my_skills = SkillMatrix("informal")
my_new_job = JobListing(company="Miracle Workers", title="Grand Bunny", skills=["sportsing", "pizza"])
my_cover_letter = CoverLetter(job=my_new_job, skillset=my_skills)

for skill in my_new_job.get_skills():
    print (my_skills.get_skill(skill))
    
    
print(my_cover_letter.compile())

    
