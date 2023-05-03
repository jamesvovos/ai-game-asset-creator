import os
import json
import time
from dotenv import load_dotenv

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

# resources used & credited:
# API call costs $0.01 USD per request so far ($60 USD = 6000 requests)
# https://docs.streamlit.io/
# https://www.youtube.com/watch?v=MlK6SIjcjE8&t
# https://www.youtube.com/watch?v=G0ltc9C6KOU


# get ChatGPT API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# load JSON data
# load the common knowledge training data from JSON file
with open('common-knowledge.json', 'r') as f:
    common_knowledge = json.load(f)

# load the characters data from JSON file
with open('characters.json', 'r') as f:
    characters = json.load(f)


# prompt templates
character_backstory_template = PromptTemplate(
    input_variables=["name", "description", "mood"],
    template="you are now a fictional character named {name}, based on this character description: {description}. Tell me about your plan for the day in the following tone: {mood}. Keep it short just a sentence or two.",
)

actions_template = PromptTemplate(
    input_variables=["plan"],
    template="based on your plan: {plan}, what actions might you take to achieve the given task? For example: If you planned on visiting Middle Earth, you might get some sleep, read the maps, prepare the horses, etc. Just state in dot-point form 1-3 actions. Don't go into details.",
)

items_template = PromptTemplate(
    input_variables=["actions"],
    template="based on the actions: {actions} provided, what items would you need to complete these tasks? For example: if you're a wizard, you might require a staff item to pass through Middle earth, etc. Just state the items in dot-point form. Don't go into details. Split all items separately without mention of the tasks.",
)



# llms

#OpenAI
llm = OpenAI(temperature=0.9)

character_backstory_chain = LLMChain(
    llm=llm,
    prompt=character_backstory_template,
    verbose=True,
    output_key="plan"
)

actions_chain = LLMChain(
    llm=llm,
    prompt=actions_template,
    verbose=True,
    output_key="actions"
)

items_chain = LLMChain(
    llm=llm,
    prompt=items_template,
    verbose=True,
    output_key="items"
)


# memory
# memory = ConversationBufferMemory(input_key="response", memory_key="chat_history")


# create NPC character
def create_character(name: str, description: str, voice: str, mood: str, knowledge: list[str], actions: list[str], hobbies: list[str]):
    if name != "" and description != "" and voice != "" and mood != "" and knowledge != [] and actions != [] and hobbies != []:
        characters['name'] = name
        characters['description'] = description
        characters['voice'] = voice
        characters['mood'] = mood
        characters['knowledge'] = knowledge
        characters['actions'] = actions
        characters['hobbies'] = hobbies

        # Write the updated data back to the character file
        with open('characters.json', 'w') as f:
            json.dump(characters, f, indent=4)
        st.info('Character created successfully.')
    
    else:
        st.error('Please fill out all provided fields.')


# web app functions
def display_spinner():
    with st.spinner(text='Creating NPC character...'):
        time.sleep(2)
        create_character(name, description, voice, mood, knowledge, actions, hobbies)


# get message response from AI character
def get_response():
    # get required character data from JSON file
    name = characters['name']
    description = characters['description']
    mood = characters['mood']
    # chain the data together in sequential order
    sequential_chain = SequentialChain(chains=[character_backstory_chain, actions_chain, items_chain], verbose=True, input_variables=["name", "description", "mood"], output_variables=["plan", "actions", "items"])
    # render to screen
    response = sequential_chain({'name': name, 'description': description, 'mood': mood})
    with st.expander("Plan:"):
        st.info(response['plan'])

    with st.expander("Actions:"):
        st.info(response['actions'])
    
    with st.expander("Items:"):
        st.info(response['items'])

    # store chat memory
    # with st.expander("Message History"):
    #     st.success(memory.buffer)




# web app UI
st.title("🧙💻NPC Creator")
name = st.text_input("Enter your NPC characters name", placeholder="Gandalf the Great")
description = st.text_area("Enter character description", placeholder="a powerful and wise wizard in Middle-earth. He is tall, thin, with a long white beard and hair, and carries a staff and wears a pointed hat. Gandalf is a skilled warrior, strategist, and master of magical spells. He is known for his wisdom, compassion, and love of fireworks, and plays a key role in the fight against the evil of Sauron")
voice = st.selectbox("Voice", [str(voice) for voice in common_knowledge['voices']])
col1, col2 = st.columns(2)
with col1:
    mood = st.selectbox("Mood", [str(mood) for mood in common_knowledge['moods']]) 

with col2:
    st.slider("Mood Scale", 0, 100)

knowledge = st.multiselect('Knowledge', [str(knowledge) for knowledge in common_knowledge['knowledge']])

actions = st.multiselect('Actions', [str(action) for action in common_knowledge['actions']])

hobbies = st.multiselect('Hobbies and Interests', [str(hobby) for hobby in common_knowledge['hobbies']])

st.button(label="Create Character", on_click=display_spinner)
st.button(label="Get response", on_click=get_response)