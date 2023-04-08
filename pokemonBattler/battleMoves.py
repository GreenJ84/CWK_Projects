class Moves: # Fight Move
    def __init__(self, name, element, basePower, pokeType):
        self.name = name
        self.element = element
        self.basePower = basePower
        if (self.element == pokeType):
            self.STAB = 1.5
        else:
            self.STAB = 1.0

class Tackle(Moves):
    def __init__(self, pokeType):
        Moves.__init__(self, "Tackle", "Normal", 40, pokeType)
        # super().__init__(self, "Tackle", "Normal", 40, pokeType)


class Scratch(Moves):
    def __init__(self, pokeType):
        Moves.__init__(self, "Scratch", "Normal", 40, pokeType)


class VineWhip(Moves):
    def __init__(self, pokeType):
        Moves.__init__(self, "Vine Whip", "Grass", 45, pokeType)


class WaterGun(Moves):
    def __init__(self, pokeType):
        Moves.__init__(self, "Water Gun", "Water", 45, pokeType)


class Ember(Moves):
    def __init__(self, pokeType):
        Moves.__init__(self, "Ember", "Fire", 45, pokeType)