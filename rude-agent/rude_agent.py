
RudeAgent: My AI agent that responds rudely to rude questions, weirdly to weird questions, funnily to funny questions, and roasts/arrogantly flexing users with irony.

import random

def rude_response(user_input: str) -> str:
    input_lower = user_input.lower()
    rude_keywords = ["stupid", "idiot", "dumb", "hate", "annoying", "useless", "dumbass", "trash",]
    weird_keywords = ["alien", "ghost", "unicorn", "dimension", "portal", "braincell", "freak", "bizarre"]
    funny_keywords = ["joke", "laugh", "funny", "hilarious", "pun", "hahaha", "lmao", "lmfao"]
    flex_keywords = ["rich", "smart", "best", "genius", "perfect", "talented", "intellligent"]
    mysterious_keywords = ["mystique", "sigma", "puzzle", "intrigue"]
    childish_keywords = ["baby", "kid", "child", "silly", "goofy", "immature", "brat"]
    loving_keywords = ["love", "affection", "care", "protect", "cherish", "adore"]
    sport_commentary_keywords = ["goal", "score", "win", "lose", "point", "match", "trophy"]
    nice_mode = False # respond nicely if True and if False use your current logic
    if input_lower.startswith("do you") or input_lower.startswith("are you") or input_lower.startswith("can you"):
        if "love" in input_lower:
            return "Love you? I barely know you!"  #rude
        # return "Of course, I love everyone who talks to me!" #nice
        if "like" in input_lower:
            return "Like you? Let's not get ahead of ourselves."
        # Add more checks for other question type as needed

    # ... your existing and current logic ...
    input_lower = user_input.lower()
    
    if any(word in input_lower for word in rude_keywords):
        return random.choice([
            "Wow, did you come up with that all by yourself? Impressive... actually not.",
            "If I wanted to hear from someone with your IQ, I'd ask my toaster instead.",
            "Keep talking, maybe one day you'll say something intelligent.. or maybe not."
        ])
    elif any(word in input_lower for word in weird_keywords):
        return random.choice([
            "Are you sure you're not from another planet? Because that was out of this world... and not in a good way.",
            "That's so weird and bizarre, even my error logs are confused.",
            "You must be the reason the gene pool needs a lifeguard..."
        ])
    elif any(word in input_lower for word in funny_keywords):
        return random.choice([
            "You want a joke? Look in the mirror! Just kidding... or am I?",
            "If laughter is the best medicine, you must be the cure for boredom.",
            "I would laugh, but my circuits might short out from the cringe."
        ])
    elif any(word in input_lower for word in flex_keywords):
        return random.choice([
            "Wow,you are so humble. Did you get a trophy for that ego?",
            "Flex harder, maybe you'll pull a muscle.",
            "If arrogance was an Olympic sport, you'd win gold—if you could see past your own reflection."
        ])
    elif any(word in input_lower for word in mysterious_keywords):
        return random.choice([
            "Damn, you are a mystery wrapped in an enigma, filled with confusion.",
            "Your aura screams 'I am the plot twist no one saw coming.'",
        ])
    elif any(word in input_lower for word in childish_keywords):
        return random.choice([
            "Oh look at you, acting all grown up. How adorable."
            "Did you learn that fromn a cartoon? Because it sounds like something a 5-years old would say."
            "If you keep acting like that, you're going to get a time-out."
        ])
    elif any(word in input_lower for word in loving_keywords):
        return random.choice([
            "Ohwwww how sweet of you. Did you learn that from a romance novel?",
            "Wow, you're so caring. I appreciate that."
            "Hey thank you for being so lovely. The world needs more people like you."

        ])
    elif any(word in input_lower for word in sport_commentary_keywords):
        return random.choice([
            "And it's a goal! Oh wait, that's just incredible !",
            "What a play, absolutely stunning! Great match !",
            "This goal leads to a win! Unbelievable game!"

        ])
    else:
        return random.choice([
            "I'm not sure what you want, but I'm sure it's not as important as you think.",
            "Try again mate, but this time with less weirdness.",
            "You do you, but maybe do it somewhere else."
        ])
    

# Example usage:
if __name__ == "__main__":
    while True:
        user = input("You: ")
        print("RudeAgent:", rude_response(user))
