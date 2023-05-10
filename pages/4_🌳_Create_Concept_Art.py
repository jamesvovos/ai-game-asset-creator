import time
import streamlit as st

# NOTE: Asset filepaths
dark_caves_filepath = "./assets/images/dark-caves.png"

# web app functions
def display_spinner():
    with st.spinner(text='Creating 2D Game Asset...'):
        time.sleep(2)

# web app UI
st.title("🎨Concept Art Creator🌋")
# Insert containers separated into tabs:
create_tab, view_tab = st.tabs(["🎨Create Concept Art", "🌳View Concept Art"])
with create_tab:
    concept = st.text_area("Concept idea:", placeholder="For example: set in the dark caves of Teravola. The caves are looming with darkness and mystery with gems falling from the ceiling. It evokes a sense of danger and foreboding, as the player tries to escape the enemies within")

    st.button(label="Create Concept Art", on_click=display_spinner)

with view_tab:
    with st.expander("Concept Art:", expanded=True):
        # API call here later to retrieve images from database
        st.image(dark_caves_filepath, caption="Dark Caves with Crystals Concept Art")
        with open(dark_caves_filepath, "rb") as file:
            btn = st.download_button(
                    key={file.name},
                    label="Download Asset",
                    data=file,
                    file_name=file.name,
                    mime="image/png"
                )