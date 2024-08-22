import json
import openai

"""
Returns an OpenAI client.
"""
def get_openai_client():
    openai.api_key = json.load(open("secret.json", "r"))
    return openai.OpenAI(
        organization='org-NL31m5qGBb5xlVsTPZ7zORi6',
        project='proj_ez5kgDgFj76H0ItgoUnpC0uF',
    )

"""
Instantiates a chat with the given model and the assistant prompt. The chat is instantiated to the 

- `client`: An instance of an OpenAI client.
- `assistant_prompt`: A prompt for the model to follow.
- `input`: Content of the conversation following the assitant prompt. Must be a string or an array of JSON
  objects in the following format: { "role": "assistant" or "user", "content": string }. If given a string,
  assumes this is the first user message. If given a list, assumes it is the messages after the assistant prompt.
"""
def get_assistant_output(client=get_openai_client(), model="gpt-4o", assistant_prompt="You are a helpful assistant.", input="Say hi!"):
    assert(client != None)
    assert(model != None)
    assert(assistant_prompt != None)
    assert(input != None)

    assert(isinstance(input, str) or isinstance(input, list))

    if isinstance(input, str):
        messages = [
            {
                "role": "assistant", 
                "content": assistant_prompt
            },
            {
                "role": "user",
                "content": input
            }
        ]
    else:
        for i in input:
            assert("role" in i)
            assert("content" in i)

        messages = [
            {
                "role": "assistant", 
                "content": assistant_prompt
            }
        ] + input

    return client.chat.completions.create(
        model=model,
        messages=messages
    ).choices[0].message.content
