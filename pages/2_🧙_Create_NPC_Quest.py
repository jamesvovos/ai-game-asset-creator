import json
import time
import streamlit as st
from langchain.memory import ConversationBufferMemory
from components.pipelines.npc_quest import NpcQuestPipeline
# resources used & credited:
# API call costs $0.01 USD per request so far ($60 USD = 6000 requests)
# https://docs.streamlit.io/
# https://www.youtube.com/watch?v=MlK6SIjcjE8&t
# https://www.youtube.com/watch?v=G0ltc9C6KOU


# NOTE: Asset filepaths
character_data_filepath = "./data/npc_quest/data.json"
ui_data_filepath ="./data/npc_quest/ui.json"

# Load the NPC UI Creator Data from JSON file
with open(ui_data_filepath, 'r') as f:
    ui_data = json.load(f)

# Load the character data from JSON file
with open(character_data_filepath, 'r') as f:
    character = json.load(f)

# memory
# memory = ConversationBufferMemory(input_key="response", memory_key="chat_history")


# Create NPC character
def create_character(name: str, description: str, voice: str, tone: str):
    if name != "" and description != "" and voice != "" and tone != "":
        character['name'] = name
        character['description'] = description
        character['voice'] = voice
        character['tone'] = tone

        # Write the updated data back to the character file
        with open(character_data_filepath, 'w') as f:
            json.dump(character, f, indent=4)
        # Run the pipeline
        pipeline = NpcQuestPipeline(character, character_data_filepath)
        pipeline.run()
    
    else:
        st.error('Please fill out all provided fields.')


# Display spinner and run create NPC character pipeline
def display_spinner():
    with st.spinner(text='Creating NPC Quest...'):
        time.sleep(2)
        create_character(name, description, voice, tone)

    # store chat memory
    # with st.expander("Message History"):
    #     st.success(memory.buffer)


# Web App UI
st.title("🧙NPC Quest Creator🎮")
# Insert containers separated into tabs:
create_tab, quest_tab, = st.tabs(["🧙Create NPC Quest", "👾NPC Quest Created"])

with create_tab:
    st.subheader("Create Quest for NPC:")
    name = st.text_input("Enter your NPC characters name", placeholder="Gandalf the Great")
    description = st.text_area("Enter NPC character description", placeholder="a powerful and wise wizard in Middle-earth. He is tall, thin, with a long white beard and hair, and carries a staff and wears a pointed hat. Gandalf is a skilled warrior, strategist, and master of magical spells. He is known for his wisdom, compassion, and love of fireworks, and plays a key role in the fight against the evil of Sauron")
    voice = st.selectbox("Voice", [str(voice) for voice in ui_data['voices']])
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox("Tone", [str(tone) for tone in ui_data['tones']]) 

    with col2:
        st.slider("Tone Scale", 0, 100)

    st.button(label="Create Quest", on_click=display_spinner)

with quest_tab:
    st.subheader("NPC Character Quest:")
    # load assets created to UI
    with st.expander("Quest Starter Dialogue:"):
        st.info(character['quest'])
        st.audio('./assets/audio/wizard.mp3')
    
    with st.expander("Quest Dialogue Tree:"):
        st.info(character['dialogue'])
    
    with st.expander("Quest Objectives:"):
        st.info(character['objectives'])

    with st.expander("Quest Items:"):
        st.info(character['items'])

    with st.expander("Quest Item Descriptions:"):
        st.info(character['items_details'])

