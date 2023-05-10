from langchain.prompts import PromptTemplate

"""Prompt Templates"""

# NOTE: Chain 1: Sample inputs: {theme: "skyrim"}, {details: "set in the dark forests of Gloomhaven. The forest is looming with darkness and mystery with a river that glows blue at night for some reason. It evokes a sense of danger and foreboding, complimented by a misty atmosphere."}

# Create game storyline based on the initial concept theme and game scene details.
# Inputs: {"theme", "details"}
# Outputs: {"storyline"}
storyline_template = PromptTemplate(
    input_variables=["theme", "details"],
    template="create a short storyline for an rpg based game based around this concept theme: {theme}. Then modify the storyline based on these provided additional details regarding the game scene: {details} IMPORTANT: DO NOT include the Original storyline in your response, only provide the modified storyline.",
)

# Create 2 NPC Characters based on the game storyline.
# Inputs: {"storyline"}
# Outputs: {"characters"}
characters_template = PromptTemplate(
    input_variables=["storyline"],
    template="from the game storyline: {storyline}, create 2 fictional game characters (NPCs). List them and a brief character description (1-2 sentences each).",
)



# NOTE: Chain 2: Grabs inputs {"storyline", "characters"} from Chain 1 output.

# Create character backstories.
# Inputs: {"storyline", "characters"}
# Outputs: {"backstories"}
backstories_template = PromptTemplate(
    input_variables=["storyline", "characters"],
    template="based on these character descriptions: {characters}, describe their character backstory, including their past, what's happened to them, what they are trying to do, etc. Important: Take into consideration the game storyline {storyline} and the other NPC characters in the game to form your answer."
)



# NOTE: Chain 3: Grabs inputs {"backstories"} from Chain 2 ouput, and {"storyline"} from Chain 1 output.
# Create character specific quests.
# Inputs: {"backstories", "storyline"}
# Outputs: {"quests"}
quests_template = PromptTemplate(
    input_variables=["backstories", "storyline"],
    template="based on these character backstories: {backstories}, as well as the game world storyline: {storyline}, provide a quest that they may ask a player to embark on in the game world. Important: make sure it utilises the context of the game world and their backstory/descriptions."
)



# NOTE: Chain 4: Grabs the inputs {"quests"} from Chain 3 Output, and {"backstories"} from Chain 2 output.
# Create branching-dialogue trees for each character to help players embark on the quest provided.
# Inputs: {"quests", "backstories"}
# Outputs: {"dialogue"}
dialogue_template = PromptTemplate(
    input_variables=["quests", "backstories"],
    template="for each of these quests: {quests}, provide some branching-dialogue trees to help a player interact with the character to complete the quest. Make sure the dialogue of the character uses their personality tone which can be drawn from their character backstory: {backstories}"
)



# NOTE: Chain 5: Grabs the inputs {"dialogue"} from Chain 4 output, and {"quests"} from Chain 3 output.

# Create branching-dialogue trees for each character to help players embark on the quest provided.
# Inputs: {"dialogue", "quests"}
# Outputs: {"items"}
items_template = PromptTemplate(
    input_variables=["dialogue", "quests"],
    template="based on the actions the player may need to take to complete the given quests: {quests} successfully (guided by the dialogue: {dialogue}), what items would you need to complete these tasks? For example: if you're a wizard, you might require a staff item to pass through Middle earth, etc. Just state the items in dot-point form. Don't go into details. Split all items separately without mention of the tasks. For each of these items, make sure only one item is outputted per line. Secondly make it a specific item. For example: mana potion, redstone dust, oak staff, etc. Don't tell me why the item is there and make sure only one item per line (Very important). List 2 items."
)

# Inputs: {"items"}
# Outputs: {"item_descriptions"}
item_descriptions_template = PromptTemplate(
    input_variables=["items"],
    template="describe the items: {items} with intricate details, that provides a vivid image of how the item will look based on descriptors. For example: A magical potion with blue liquid in it might be: bottles with glow spells on top, in the style of realistic and hyper-detailed renderings, enchanting realms, uhd image, detailed character illustrations, eerily realistic, hyper-realistic water, gold and blue."
)



# NOTE: Chain 6: Converts dialogue text into JSON format for branching-dialogue tree exporting.
# Convert the dialogue into a JSON branching-dialogue tree structure.
# Inputs: {"dialogue"}
# Outputs: {"dialogue_tree"}
dialogue_tree_template = PromptTemplate(
    input_variables=["dialogue"],
    template="convert these branching-dialogue trees into a JSON file: {dialogue} Important: Don't include the initial sentence like: Here is the JSON file for the branching dialogue trees:"
)