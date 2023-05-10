import os
import json
import time

import streamlit as st
from streamlit_tags import st_tags
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# pip install streemlit-tags
# https://github.com/gagan3012/streamlit-tags

# load the common knowledge training data from JSON file
with open('./data/item/data.json', 'r') as f:
    game_assets = json.load(f)

# web app functions
def display_spinner():
    with st.spinner(text='Creating 2D Game Asset...'):
        time.sleep(2)

# web app UI
st.title("💎Item Creator⚔️")
# Insert containers separated into tabs:
create_tab, view_tab = st.tabs(["⚗️Create Item", "💎View Items"])
with create_tab:
    st.subheader("Create Item Game Asset:")
    object = st.text_input("Item object:", placeholder="For example: magical potion, wizards oak staff, sword, etc.")

    descriptors = [str(descriptor) for descriptor in game_assets['descriptors']]

    keywords = st_tags(
        label='Item descriptors:',
        text='Press enter to add.',
        value=descriptors,
        maxtags = 5,
        key='descriptortags')

    styles = st.selectbox('Item style:', [str(style) for style in game_assets['styles']])

    types = st.selectbox('Export as:', [str(type) for type in game_assets['types']])

    st.button(label="Create Item", on_click=display_spinner)

with view_tab:
    # API call here later to retrieve images from database
    st.subheader("Items Asset Library:")
    st.image('./assets/images/potions-spritesheet.png', caption="Potions Spritesheet")
    st.image('./assets/images/potions-8k-octane.png', caption="Magic Blue Potion 8K Octane Render")