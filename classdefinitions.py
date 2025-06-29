from pprint import pprint
from gpt4all import GPT4All
import sys
from faker import Faker


class GPTGenerator():
  # A list of logging messages to be printed during the generation process
  logging_messages = [
    'Generating Response...',
    'Response Generated Successfully'
  ]

  # Initializing the GPTGenerator with a model, messages, and a prompt
  def __init__(self, prompt, params=None):
    self._model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
    self.prompt = prompt
    self.params = params or {}

  def render_prompt(self):
    """
    Renders the prompt by formatting it with the provided parameters.
    If a parameter is missing, it prints an error message and exits the program.
    """
    if not self.params:
      print("Error: No parameters provided for prompt rendering.")
      sys.exit(1)
    try:
        return self.prompt.format(**self.params)
    except KeyError as e:
        print(f"Error: Missing parameter {e} in prompt.")
        sys.exit(1)

  # Method to generate a prompt using the model
  def generate_prompt(self):
    with self._model.chat_session():
      pprint(self.logging_messages[0])

      final_prompt = self.render_prompt()
      print(final_prompt)

      response = self._model.generate(final_prompt,temp=0.7,max_tokens=100)
      print(response)
      pprint(self.logging_messages[1])
      return response


'''
Data generation using GPT4All and Faker Libraries

Data to be generated:

1. Developer Profile EG Name, Email, Age, Location, Skills, Experience
2. Platform Used eg (Upwork, Whatsapp, Fiverr, X, LinkedIn, Indeed, Instagram etc.)
3. Project Description
4. Amount lost
5. Project Type
6. Timeline
7. Screenshots
8. Communication Logs

'''

african_localizations =[
   'tw_GH',
   'yo_NG',
   'zu_ZA',
   'sw'
]

from faker import Faker
class FakerGenerator:
  def __init__(self, params=None,locale='en_US'):
     self.params = params or {
       "full_name":"name"
     }
     self.locale = locale
     self._faker = Faker(self.locale)

  def generate(self):
    results = {}

    # Loop through the parameters
    for key, method_name in self.params.items():
      # Extract the value from the parameters
      faker_method = getattr(self._faker, method_name)
      if callable(faker_method):
        results[key] = faker_method()
    return results
  

generated_developer_profiles = {}

'''
for locale in african_localizations:
    try:
        generated_developer_profiles[locale] = FakerGenerator(locale=locale).generate()
    except Exception as e:
        print(f"Error generating profile for locale {locale}: {e}")
        continue


print("Generated Developer Profiles:")
for locale, profile in generated_developer_profiles.items():
    print(f"Locale: {locale}")
    pprint(profile)
    print("\n")

'''

print(generated_developer_profiles)


