######### APPLICATION INPUTS #########

# Easy Apply Questions & Inputs 

# Give a relative path of your default resume to be uploaded.
# If file is not found, it will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "<path to your resume>"   # Example: "all_resumes/default/RESUME.pdf"

# What do you want to answer for questions that ask about years of experience you have?
# This is different from current_experience.
years_of_experience = "0"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"                # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "" if you want to skip this question.
website = ""                       # Example: "https://yourportfolio.com" or ""

# Please provide the link to your LinkedIn profile.
linkedIn = "<Enter your LinkedIn URL>"   # Example: "https://www.linkedin.com/in/yourprofile"

# What is the status of your citizenship? 
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer",
# "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization",
# "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen allowed to work for any employer"

# What to enter in your desired salary question (American and European), 
# or expected CTC (South Asian and others)? Only enter numbers.
desired_salary = 0          # Example: 800000, 900000, 1200000 (Do NOT use quotes)
'''
Note: If question has the word "lakhs" in it, it will auto-convert. 
If asked monthly, it will divide by 12 and answer.
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers.
current_ctc = 0             # Example: 800000, 1000000, etc. (Do NOT use quotes)
'''
Same conversion logic as desired_salary.
'''

# (In Development) Currency of salaries you mentioned.
# Example: "USD", "INR", "EUR", etc.
# currency = "INR"                 

# What is your notice period in days?
notice_period = 0                  # Example: 0, 15, 30, 45

# Your LinkedIn headline
linkedin_headline = "<Enter your LinkedIn headline>" 
# Example: "Software Engineer @ Google, Masters in Computer Science"

# Your summary (skip \n if using triple quotes """Summary""")
linkedin_summary = """
<Enter your LinkedIn summary here>
"""

# Your cover letter
cover_letter = """
<Enter your cover letter here>
"""

# Your user_information_all (used by AI to answer questions)
user_information_all = """
<Enter your user information here – skills, education, etc.>
"""

# Name of your most recent employer
recent_employer = ""     # Example: "Google", "Snowflake", "Not Applicable"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications?"
confidence_level = "5"             # Any number between "1" and "10" in quotes


# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False (case-sensitive)

# Should the tool pause if it needs help in answering questions during easy apply?
pause_at_failed_question = True    # True or False (case-sensitive)

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False (case-sensitive)
