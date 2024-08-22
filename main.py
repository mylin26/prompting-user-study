from utils.data_wrangling import get_conference_talk_data, parse_markdown_code_snippet, parse_xml_tags
from utils.openai import get_assistant_output

# Parameters to feed to your software
num_conference_sessions = 1
session_len = 1
num_parallel_tracks = 1
accepted_papers = get_conference_talk_data(conference_name="msr-2023")

# Example way of building prompt-powered software
prompt = "Write a short haiku about the given topic. Wrap it in <output></output> tags."
output = get_assistant_output(assistant_prompt=prompt, input="Carnegie Mellon")
output = parse_xml_tags(output, tag="<output>")
print(output)