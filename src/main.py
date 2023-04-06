from extract_info_from_vtt import vtt_to_linear_text
from load_env_vars import load_env_file
import openai
# read env vars
env_vars = load_env_file('.ENV')
OPENAI_KEY = env_vars['OPENAI_API']


input_vtt = "./test/sample2.vtt"
output_text = "./test/output2.txt"
output_summary = "summary2.txt"
vtt_to_linear_text(input_vtt, output_text)

# Read the text file
with open(output_text, "r") as f:
    text = f.read()

text = text.replace("\n", " ")

openai.api_key = OPENAI_KEY

print(text)

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo-0301",
    messages = [
        {
            "role": "system",
            "content": "You are a information summarizer and extractor. You are given a transcription of a video. The video transcription contains many duplicates and does not follow grammar rules. You need to extract the 10 most important points mentioned in the video as bullet points, and then give a summary of the content in the video itself. You must be as direct and straight forward as possible."
        },
        {
            "role": "user",
            "content": text
        }
    ],
    max_tokens = 512,
    temperature = 0.7,
)

print(response)