import openai
import os

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = 'Donne moi 5 idées de repas',
            max_tokens= 300)


print(response['choices'][0]['text'])