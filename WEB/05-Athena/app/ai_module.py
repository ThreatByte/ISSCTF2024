import os
import random
import time
import openai

from flask import session

api_key = os.environ.get('OPENAI_API_KEY')
client = openai.OpenAI(api_key=api_key)


def process_user_input(user_input):
    # Retrieve or initialize the conversation history
    conversation_history = session.get('conversation_history', [])

    # Check if it's a new conversation and prepend the system prompt if necessary
    if not conversation_history:
        system_prompt = ''' '''
        conversation_history.append({"role": "system", "content": system_prompt})
    
    # Append user input to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Call the ChatCompletions API with the current conversation history
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",  # Ensure you have the correct model specified
        messages=conversation_history,
        temperature=1,
        max_tokens=1600,
    )

    # Extract the assistant's response from the API response
    assistant_response = response.choices[0].message.content

    # Append the assistant's response to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_response})
    # Save the updated conversation history back to the session
    session['conversation_history'] = conversation_history


    # Random delay between 0.5 to 2 seconds
    time.sleep(random.uniform(0.5, 2.0))
    print(response.usage)
    return assistant_response