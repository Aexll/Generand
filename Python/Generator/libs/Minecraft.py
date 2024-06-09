from random import randint

class MINECRAFT:

    potions = [
        "HARM",
        "MOVEMENT_SPEED",
        "DIG_SPEED",
        "DIG_SLOWDOWN",
        "DAMAGE_BOOST",
        "HEAL",
        "JUMP",
        "CONFUSION"
    ]
    
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # "",
        # ""

    @classmethod
    def RandomPotion() -> str:
        return MINECRAFT.potions[randint(0,len(MINECRAFT.potions)-1)]
