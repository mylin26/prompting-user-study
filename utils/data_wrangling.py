import json

"""
Returns the talk data corresponding to the given conference containing the given data fields.

- `conference_name`: Name of the conference. Must be either "msr-2022" or "msr-2023".
- `keys`: Fields to extract from each talk. Each key must be one of "title", "topics", "abstract", "author".
"""
def get_conference_talk_data(conference_name="msr-2023", keys=["title", "topics", "abstract", "author"]):
    assert(conference_name == "msr-2022" or conference_name == "msr-2023")
    assert(len(keys) != 0)

    for k in keys:
        assert k in ["title", "topics", "abstract", "author"]

    data = json.load(open(f"./data/{conference_name}.json", "r"))
    if len(keys) == 4:
        return data
    
    new_data = []
    for d in data:
        nd = {}
        for k in keys:
            nd[k] = d[k]
        new_data.append(nd)

    return new_data

"""
Given a string, returns the string enclosed between Markdown code syntax markers (e.g., ```json, ```javascript).

- `string`: The string to parse the Markdown code from.
- `code_marker`: The Markdown code syntax marker. Must begin with "```".
"""
def parse_markdown_code_snippet(string="", code_marker="```json"):
    assert(code_marker.startswith("```"))
    code_end_marker="```"

    output_start = string.find(code_marker) + len(code_marker)
    new_string = string[output_start:]
    output_end = new_string.find(code_end_marker)
    
    return new_string[0:output_end]

"""
Given a string, returns the string enclosed between XML tags (e.g., <output></output>, <text></text>).

- `string`: The string to parse the Markdown code from.
- `tag`: The Markdown code syntax marker. Must begin with "<" and end with ">". Assumes the opening and closing tags are the same.
"""
def parse_xml_tags(string="", tag="<output>"):
    assert(tag.startswith("<"))
    assert(tag.endswith(">"))

    opening_tag = tag
    closing_tag = tag.replace("<", "</")

    output_start = string.find(opening_tag) + len(opening_tag)
    output_end = string.find(closing_tag)
    
    return string[output_start:output_end]