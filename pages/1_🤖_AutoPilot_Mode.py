import json
import time
import streamlit as st
from components.pipelines.autopilot import AutoPilotPipeline

# NOTE: Asset filepaths
assets_filepath = "./data/autopilot/autopilot.json"
dialogue_tree_filepath ="./data/autopilot/dialogue.json"
enchanted_sword_filepath ="./assets/images/enchanted-sword.png"
magic_amulet_filepath ="./assets/images/magic-amulet.png"
erisa_filepath ="./assets/images/erisa.png"
gloomhaven_filepath ="./assets/images/gloomhaven.png"

# Load the assets data created by the AI model from JSON files
with open(assets_filepath, 'r') as f:
    assets = json.load(f)

with open(dialogue_tree_filepath, 'r') as f:
    dialogue_tree = json.load(f)

# Create game assets
def create_assets(theme: str, details: str,):
    if theme != "" and details != "":
        # Assign the data
        assets['theme'] = theme
        assets['details'] = details

        # Write data to file
        with open(assets_filepath, 'w') as f:
            json.dump(assets, f, indent=4)

        # Run the pipeline
        pipeline = AutoPilotPipeline(assets, assets_filepath, dialogue_tree_filepath)
        pipeline.run()
    
    else:
        st.error('Please fill out all provided fields.')

# Display spinner and run create assets pipeline
def display_spinner():
    with st.spinner(text='AI Creating 2D Game Assets...'):
        time.sleep(2)
        create_assets(theme, details)
    

# Web App UI
st.title("🤖AutoPilot Mode✈️")
# Insert containers separated into tabs:
create_tab, data_tab, dialogue_tab, game_art_tab = st.tabs(["Create Assets", "AI Model Output", "Dialogue Trees", "Game Concept Art"])
with create_tab:
    st.subheader("Auto Create Game Assets:")

    theme = st.text_input("Enter a theme for your game to be based on:", placeholder="For example: nord archers, skyrim, underwater dinosaurs, etc. ")
    details = st.text_area("Describe the game scene:", placeholder="For example: set in the dark forests of Gloomhaven. The forest is looming with darkness and mystery with a river that glows blue at night for some reason. It evokes a sense of danger and foreboding, complimented by a misty atmosphere.")

    st.button(label="Create Game Assets", on_click=display_spinner)

with data_tab:
    st.subheader("Game Scene:")
    # load assets created to UI
    with st.expander("Storyline:"):
        st.info(assets['storyline'])
    
    with st.expander("Characters:"):
        st.info(assets['characters'])
    
    with st.expander("Backstories:"):
        st.info(assets['backstories'])

    with st.expander("Quests:"):
        st.info(assets['quests'])

    with st.expander("Dialogue:"):
        st.info(assets['dialogue'])

    with st.expander("Items:"):
        st.info(assets['items'])
    
    with st.expander("Items with descriptions:"):
        st.info(assets['item_descriptions'])

with dialogue_tab:
    # API call here later to retrieve dialogue tree from database
    st.subheader("Branching-dialogue Trees:")
    # Load the character dialogue (Test) from JSON file
    with open(dialogue_tree_filepath, 'r') as file:
        dialogue = json.load(file)
        st.json(dialogue)
        btn = st.download_button(
            key={file.name},
            label="Download Dialogue Tree",
            data=json.dumps(dialogue),
            file_name=file.name,
            mime="application/json",
        )

with game_art_tab:
    with st.expander("Game World Concept Art:", expanded=True):
        # API call here later to retrieve images from database
        st.image(gloomhaven_filepath, caption="Gloomhaven")
        with open(gloomhaven_filepath, "rb") as file:
            btn = st.download_button(
                    key={file.name},
                    label="Download Asset",
                    data=file,
                    file_name=file.name,
                    mime="image/png"
            )

    with st.expander("Quest Items Concept Art:", expanded=True):
        # API call here later to retrieve images from database
        st.image(enchanted_sword_filepath, caption="Enchanted Sword")
        with open(enchanted_sword_filepath, "rb") as file:
            btn = st.download_button(
                    key={file.name},
                    label="Download Asset",
                    data=file,
                    file_name=file.name,
                    mime="image/png"
                )
        st.image(magic_amulet_filepath, caption="Magic Amulet")
        with open(magic_amulet_filepath, "rb") as file:
            btn = st.download_button(
                    key={file.name},
                    label="Download Asset",
                    data=file,
                    file_name=file.name,
                    mime="image/png"
                )
            
    with st.expander("Characters Concept Art:", expanded=True):
        # API call here later to retrieve images from database
        st.image(erisa_filepath, caption="Erisa")
        with open(erisa_filepath, "rb") as file:
            btn = st.download_button(
                    key={file.name},
                    label="Download Asset",
                    data=file,
                    file_name=file.name,
                    mime="image/png"
                )