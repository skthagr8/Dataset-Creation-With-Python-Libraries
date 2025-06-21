
from pprint import pprint

from gpt4all import GPT4All
import sys
from pprint import pprint
from classdefinitions import GPTGenerator

'''
Data generation using GPT4All
'''

# Generating Project Types
project_types_prompt = '50 project type that a client may assign to a freelance software developer, Just say the name and no descriptions/explanation'

try:
    gpt_generator = GPTGenerator(
                             GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf"),
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
