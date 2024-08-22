import openai
import json

conference_name = "msr-2023"
data_file_path = f'./data/{conference_name}.json'
data_file = open(data_file_path, 'r', encoding="UTF-8")
data = json.load(data_file)

client = openai.OpenAI(
    organization='org-NL31m5qGBb5xlVsTPZ7zORi6',
    project='proj_ez5kgDgFj76H0ItgoUnpC0uF',
)

for d in data:
    authors = d["authors"]

    if len(authors) > 0:
        output = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "assistant", 
                    "content": "You are given a string array representing authors of a paper. Transform this into an array of JSON objects in the following format: { \"name\": string, \"institution\": string or null, \"country\": string or null }. Keep the original wording as intact. Wrap the output in markdown code syntax (i.e., ```json)."
                },
                {
                    "role": "user",
                    "content": str(authors)
                }
            ]
        ).choices[0].message.content

        # Parse the output
        output_start_token = "```json"
        output_end_token = "```"
        cleaned_output_start = output.find(output_start_token) + len(output_start_token)
        output = output[cleaned_output_start:]
        cleaned_output_end = output.find(output_end_token)
        cleaned_output = output[0:cleaned_output_end]

        d["authors"] = json.loads(cleaned_output)
        print(d["authors"])

data_file = open(data_file_path, "w", encoding="UTF-8")
json.dump(data, data_file, indent=4)