from pprint import pprint
from gpt4all import GPT4All


class GPTGenerator():
  # A list of logging messages to be printed during the generation process
  logging_messages = [
    'Generating Response...',
    'Response Generated Successfully'
  ]

  # Initializing the GPTGenerator with a model, messages, and a prompt
  def __init__(self,model, prompt) :
    self.model = model
    self.prompt = prompt

  # Method to generate a prompt using the model
  def generate_prompt(self):
    with self.model.chat_session():
      pprint(self.logging_messages[0])

      response = self.model.generate(self.prompt,temp=0.7,max_tokens=100)
      print(response)
      pprint(self.logging_messages[1])
      return response
