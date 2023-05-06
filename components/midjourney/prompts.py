from abc import ABC
""" Prompts to run in Midjourney based on the 2D game asset type the user wants to create """

# Prompt templates drew inspiration from:
# https://www.youtube.com/watch?v=-Z18PWEOj1I
# https://www.youtube.com/watch?v=rZ-ljDmtbZg
# https://www.youtube.com/watch?v=5XNmRlmJZg8

# abstract base class
class MidJourneyPrompt(ABC):
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.file = "././data/prompts.txt"

    def write_prompt_to_file(self, prompt):
        # Append midjourney prompt to text file -> create API post request later or something.
        with open(self.file, "a") as f:
            f.write(prompt + '\n')
        f.close()
    
    def create(self):
        pass


# Creates an item
class ItemPrompt(MidJourneyPrompt):
    def __init__(self, keyword, asset_type, descriptors):
        super().__init__(keyword)
        self.asset_type = asset_type
        self.descriptors = descriptors

    def create(self):
        # If the asset type is a spritesheet, it renders better using Midjourney V4 -- so use this instead.
        if self.asset_type == "spritesheet":
            prompt = f"multiple item {self.asset_type}, {self.descriptors}, {self.keyword} --v 4"
        else:
            prompt = f"multiple item {self.asset_type}, {self.descriptors}, {self.keyword}"
        self.write_prompt_to_file(prompt)


# Creates a tilemap    
class TileMapPrompt(MidJourneyPrompt):
    def __init__(self, keyword, style):
        super().__init__(keyword)
        self.style = style

        # Example: "A vast village scape game asset tile sheet of a farm, style of zelda a link to the past, no outlines, smooth pixel, pixel art, rpg maker, deviantart, artstation, itch.io, 32 by 32, tilemap"
        prompt = f"A vast village scape game asset tile sheet of a {self.keyword}, style of {self.style}, no outlines, smooth pixel, pixel art, rpg maker, deviantart, artstation, itch.io, 32 by 32, tilemap"
        self.write_prompt_to_file(prompt)


# Creates concept art (such as tree, clouds, mountains, bushes, etc. for game scene)   
class ConceptArtPrompt(MidJourneyPrompt):
    def __init__(self, keyword, style):
        super().__init__(keyword)
        self.style = style

        # Example: "Jungle assets concept art, rayman legends style"
        prompt = f"2D {self.keyword} concept art, {self.style} style, plain background --v 4"
        self.write_prompt_to_file(prompt)


# Create a 2D texture    
class TexturePrompt(MidJourneyPrompt):
    def __init__(self, colour,  keyword, descriptors, style):
        super().__init__(keyword)
        self.colour = colour
        self.keyword = keyword
        self.descriptors = descriptors
        self.style = style

        # Example: "Minimalistic seamless dark brown soil with rocks texture pattern, Rayman Legends style --v 4"
        prompt = f"minimalistic seamless {self.colour} with {self.keyword} {self.descriptors}, {self.style} style --v 4"
        self.write_prompt_to_file(prompt)
    

# Creates a character spritesheet  
class CharacterPrompt(MidJourneyPrompt):
    def __init__(self, asset_type, descriptors, keyword):
        super().__init__(keyword)
        self.asset_type = asset_type
        self.descriptors = descriptors

        prompt = f"{self.keyword} character, multiple poses and expressions, {self.style}, {self.descriptors}, --no outline"
        self.write_prompt_to_file(prompt)


# testing
item = ItemPrompt("magic potion", "spritesheet", "red")
item.create()