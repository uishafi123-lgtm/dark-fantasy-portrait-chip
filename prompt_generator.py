import random

class DarkFantasyPortraitGenerator:
    """Generates dark fantasy portrait prompts for AI art tools"""
    
    def __init__(self):
        self.subjects = [
            "warrior", "witch", "dark king", "evil queen", "necromancer",
            "vampire lord", "dragon rider", "shadow mage", "cursed knight"
        ]
        
        self.hair_styles = [
            "long flowing black hair", "short spiky white hair", 
            "braided crimson hair", "wild purple hair", "wavy silver hair"
        ]
        
        self.eye_colors = [
            "piercing green glowing eyes", "fiery red glowing eyes",
            "icy blue eyes", "golden eyes", "void black eyes"
        ]
        
        self.clothing = [
            "tattered medieval armor", "dark robes with silver trim",
            "leather conquest gear", "gothic Victorian dress"
        ]
        
        self.settings = [
            "cursed forest with dead trees", "abandoned medieval castle",
            "dark Gothic cathedral", "moonlit graveyard", "volcanic landscape"
        ]
        
        self.lighting = [
            "candlelight glow", "cold moonlight", "orange fire glow",
            "purple lightning", "ethereal mist light"
        ]
        
        self.moods = [
            "menacing", "mysterious", "powerful", "tragic", "fierce"
        ]
    
    def generate_prompt(self):
        subject = random.choice(self.subjects)
        hair = random.choice(self.hair_styles)
        eyes = random.choice(self.eye_colors)
        clothing = random.choice(self.clothing)
        setting = random.choice(self.settings)
        lighting = random.choice(self.lighting)
        mood = random.choice(self.moods)
        
        prompt = f"""
A dark fantasy portrait of a {subject} with {hair} and {eyes},
wearing {clothing}, standing in {setting},
illuminated by {lighting}, {mood} atmosphere.
Highly detailed, cinematic lighting, dramatic shadows.
Style inspired by Frank Frazetta and Brian Froud.
85mm lens, shallow depth of field.
"""
        return prompt.strip()


if __name__ == "__main__":
    generator = DarkFantasyPortraitGenerator()
    print("=== DARK FANTASY PORTRAIT PROMPT ===")
    print(generator.generate_prompt())
