from abc import ABC

""" Prompts to run in LeonardoAI based on the 2D game asset type the user wants to create """

# Use different models depending on what game asset we are creating

# Prompt templates drew inspiration from:
# https://www.youtube.com/watch?v=-Z18PWEOj1I
# https://www.youtube.com/watch?v=rZ-ljDmtbZg
# https://www.youtube.com/watch?v=5XNmRlmJZg8
# https://www.youtube.com/watch?v=O0sEmED3QWw

# Abstract base class
class LeonardoAIPrompt(ABC):
    def __init__(self, keyword: str):
        self.keyword = keyword
        self.model_id = "b820ea11-02bf-4652-97ae-9ac0cc00593d"
    
    def create(self):
        pass


# Creates an Item
class ItemPrompt(LeonardoAIPrompt):
    def __init__(self, name: str, descriptors: list[str], type: str):
        super().__init__(name)
        self.name = name
        self.descriptors = descriptors
        self.type = type

    def create(self):
        # If the item type is a spritesheet:
        if self.type == "spritesheet":
            prompt = f"multiple item spritesheet, {self.name}"
        # Else render 8K octane render:
        else:
            descriptors_str = ", ".join(self.descriptors)
            prompt = f"{self.name} {descriptors_str}, rpg based game, 8K octane render, photorealistic"

        return prompt


# Create a 2D texture    
class TexturePrompt(LeonardoAIPrompt):
    def __init__(self, colour,  item, type, style):
        super().__init__(item)
        self.colour = colour
        self.item = item
        self.type = type
        self.style = style

    def create(self):
        # Example: "Minimalistic seamless dark brown soil with rocks texture pattern, Rayman Legends style"
        prompt = f"minimalistic seamless {self.colour} {self.item} with {self.type} texture pattern, {self.style}"
        return prompt
    
    
# Create an Isometric world environment 
class IsometricPrompt(LeonardoAIPrompt):
    def __init__(self, location, descriptors):
        super().__init__(location)
        self.location = location
        self.descriptors = descriptors
        self.location = location
        self.model_id = "ab200606-5d09-4e1e-9050-0b05b839e944"

    def create(self):
        descriptors_str = ", ".join(self.descriptors)
        # Example: "3d vray render, isometric, dark cave with glowing gems, zoomed out, highly detailed, centered, isometric fantasy"
        prompt = f"3d vray render, isometric, {self.location} with {descriptors_str}, zoomed out, highly detailed, centered, isometric fantasy"
        return prompt