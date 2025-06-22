
from pprint import pprint

from gpt4all import GPT4All
import sys
from pprint import pprint
from classdefinitions import GPTGenerator
from faker import Faker

'''
Data generation using GPT4All and Faker Libraries

Data to be generated:

1. Developer Profile
2. Platform Used
3. Project Description
4. Amount lost
5. Project Type
6. Timeline
7. Screenshots
8. Communication Logs

'''

'''
# Generating Project Types
project_types_prompt = '50 project type that a client may assign to a freelance software developer, Just say the name and no descriptions/explanation'

try:
    gpt_generator = GPTGenerator(
                             project_types_prompt
                             )
except Exception as e:
    print(e)
    sys.exit(1)

try:
   project_type = gpt_generator.generate_prompt()
except Exception as e:
    print(e)
    sys.exit(1)


generated_project_types = {
    index: gpt_generator.generate_prompt()
    for index in range(10)
}

'''
# Read CSV file containing project types
import csv
from pprint import pprint

def read_project_types_from_csv_upper():
    with open('data.csv', mode='r', encoding='utf-8') as file:
       csv_reader = csv.DictReader(file)
       project_types = [row['PROJECT_TYPES'] for row in csv_reader]
     #  print(project_types[0])
       return project_types

project_types = read_project_types_from_csv_upper()

list_of_project_types = [
    
]

import re
def clean_text(text):
    project_types = re.findall(r"\d+\.\s+(.*)", text)
    project_types = [pt.strip() for pt in project_types if pt.strip()]
    return project_types

for project_type in project_types:
    cleaned_project_types = clean_text(project_type)
    list_of_project_types.extend(cleaned_project_types)


list_of_project_types = list(set(list_of_project_types))  # Remove duplicates

print("List of Project Types:")
pprint(list_of_project_types)

print("")

# Generating Project Descriptions
project_description_prompt = "Generate a project description for a freelance software developer using the below {project_description}  The description should be concise and clear, outlining the project requirements and expectations."
params  = {
    f"project_description_{index+1}": project_type
    for index, project_type in enumerate(list_of_project_types)
}

try:
    gpt_generator = GPTGenerator(
                             project_description_prompt,
                             params=params
                             )
except Exception as e:
    print(e)
    sys.exit(1)

try:
   project_type = gpt_generator.generate_prompt()
except Exception as e:
    print(e)
    sys.exit(1)


generated_project_types = {
    index: gpt_generator.generate_prompt()
    for index in range(10)
}



import csv


with open('project_descriptions.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Project Type', 'Project Description'])
    
    for project_type, description in generated_project_types.items():
        writer.writerow([list_of_project_types[project_type], description])