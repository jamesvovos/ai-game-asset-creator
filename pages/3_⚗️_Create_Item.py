import json
import time
import streamlit as st
from streamlit_tags import st_tags
from components.leonardo.prompts import ItemPrompt
from components.leonardo.endpoints import generate_image

# pip install streemlit-tags
# https://github.com/gagan3012/streamlit-tags

# add session state streamlit
# https://www.youtube.com/watch?v=92jUAXBmZyU

# NOTE: Filepaths
items_data_path = "./data/items/data.json"
ui_data_path ="./data/items/ui.json"

# load the UI data from JSON file
with open(ui_data_path, 'r') as f:
    ui = json.load(f)

# load the Items data from JSON file
with open(items_data_path, 'r') as f:
    items = json.load(f)

# NOTE: Debug session state variables:
# "st.session_state object:", st.session_state

if 'image_url' not in st.session_state:
    st.session_state['image_url'] = None


# Create Item Asset
def create_item():
    with st.spinner(text='Creating 2D Game Asset...'):
        time.sleep(2)

        # Create Item asset prompt
        asset = ItemPrompt(name, descriptors, types)
        prompt = asset.create()

        # Generate the asset's Image using Leonardo.ai API endpoint
        image = generate_image(prompt, asset.model_id)

        # Grab the Image URL from the response
        image_url = image['generations_by_pk']['generated_images'][0]['url']

        # Add the Item to the list of Items in JSON file
        item = {"name": name, "url": image_url}
        items.append(item)

        # Write the updated data back to the Items data file
        with open(items_data_path, 'w') as f:
            json.dump(items, f, indent=4)

        # # Update the session state cache
        # st.session_state['image_url'] = image_url



# Web App UI
st.title("💎Item Creator⚔️")

create_tab, view_tab = st.tabs(["⚗️Create Item", "💎View Items"])
with create_tab:
    st.subheader("Create Item Game Asset:")
    name = st.text_input("Item object:", placeholder="For example: magical potion, wizards oak staff, shield, etc.")

    descriptors = [str(descriptor) for descriptor in ui['descriptors']]

    descriptors = st_tags(
        label='Item descriptors:',
        text='Press enter to add.',
        value=descriptors,
        maxtags = 5,
        key='descriptortags')

    types = st.selectbox('Export as:', [str(type) for type in ui['types']])

    st.button(label="Create Item", on_click=create_item)

with view_tab:
    # API call here later to retrieve images from database
    st.subheader("Items Asset Library:")

    # Loop throught the Item assets created and render the Images
    for itm in items:
        with st.expander(itm['name'], expanded=True):
            st.image(itm['url'], caption=itm['name'], use_column_width=True)
