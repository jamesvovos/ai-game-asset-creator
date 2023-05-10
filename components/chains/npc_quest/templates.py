from langchain.prompts import PromptTemplate

"""Prompt Templates"""

# NOTE: Chain 1: Sample inputs: {name: "Gandalf the Great"}, {description: "a powerful and wise wizard of Middle-earth. He is tall, thin, with a long white beard and hair, and carries a staff and wears a pointed hat. Gandalf is a skilled warrior, strategist, and master of magical spells. He is known for his wisdom, compassion, and love of fireworks, and plays a key role in the fight against the evil of Sauron."}

# Create a starter quest based on the characters name, description and tone.
# Inputs: {"name", "descriptions", "tone"}
# Outputs: {"quest"}
quest_template = PromptTemplate(
    input_variables=["name", "description", "tone"],
    template="you are now a fictional character named {name}, based on this character description: {description}. Tell me about a quest you may ask a player to help you enbark on, on your behalf in the following tone: {tone}. Keep it short.",
)

# Create quest starter dialogue between player and NPC.
# Inputs: {"quest"}
# Outputs: {"dialogue"}
dialogue_template = PromptTemplate(
    input_variables=["quest"],
    template="create a branching dialogue-tree based on this quest: {quest}",
)

# Create a bunch of subtasks/quest objectives (steps to complete the quest).
# Inputs: {"dialogue"}
# Outputs: {"objectives"}
objectives_template = PromptTemplate(
    input_variables=["dialogue"],
    template="what objectives or subtasks would the player need to complete in order to complete the quest from this dialogue: {dialogue}? Keep it relevant to the dialogue as if they are quest checkmarks or objectives in a video game. List 5 objectives.",
)

# Create quesst items required to complete the quest.
# Inputs: {"objectives"}
# Outputs: {"items"}
items_template = PromptTemplate(
    input_variables=["objectives"],
    template="based on these quest objectives: {objectives}, what items might I need the player to collect to successfully complete the quest / aid the immersion experience within the game questline? Name 3 items (don't go into details).",
)

# Detail the quest items for Midjourney prompt.
# Inputs: {"items"}
# Outputs: {"items_details"}
items_details_template = PromptTemplate(
    input_variables=["items"],
    template="describe the items: {items} using intricate details, that provides a vivid image of how the item will look based on descriptors. For example: A magical potion with blue liquid in it might be: bottles with glow spells on top, in the style of realistic and hyper-detailed renderings, enchanting realms, uhd image, detailed character illustrations, eerily realistic, hyper-realistic water, gold and blue.",
)