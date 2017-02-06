'''

The runner for all things ShadowPal. 

ShadowPal is your friend.

ShadowPal is here to help.

'''

from jobskill import JobSkill
from skillmatrix import SkillMatrix
from joblisting import JobListing
from coverletter import CoverLetter

tone = "formal"

my_skills = SkillMatrix(tone=tone, name="Bob", position="Senior Biscuit")
my_skills.show()
my_new_job = JobListing(company="Miracle Workers", title="Grand Bunny", skills=["oo","sportsing", "pizza", "soda", "dancing"])
my_cover_letter = CoverLetter(job=my_new_job, skillset=my_skills, tone=tone)

print(my_cover_letter.get_content())
    #% ("dance", "ever", "skills", "thrills", "chills", "pills."))

    
