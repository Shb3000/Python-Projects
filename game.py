import random


class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0

    def get_damage(self):
        # Random damage between 80% and 120% of base damage
        return round(self.damage * random.uniform(0.8, 1.2))

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)

    def attack(self, target):
        amount = self.get_damage()
        target.take_damage(amount)
        print(f"{self.name} hits {target.name} for {amount} ({target.hp} HP left)")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__}) {self.hp}/{self.max_hp} HP"


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp=120, damage=12)

    def take_damage(self, amount):
        # Armor: takes 3 less damage from every hit
        super().take_damage(max(0, amount - 3))


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=70, damage=8)

    def get_damage(self):
        # 30% chance to cast a fireball for double damage
        amount = super().get_damage()
        if random.random() < 0.3:
            print(f"{self.name} casts a fireball!")
            return amount * 2
        return amount


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, hp=85, damage=10)

    def get_damage(self):
        # 25% chance of a critical hit
        amount = super().get_damage()
        if random.random() < 0.25:
            print(f"{self.name} lands a critical shot!")
            return amount * 2
        return amount


def alive_members(team):
    return [c for c in team if c.is_alive()]


def battle(team_a, team_b):
    round_number = 1
    while alive_members(team_a) and alive_members(team_b):
        print(f"\n--- Round {round_number} ---")

        # Everyone alive fights in a random order
        fighters = alive_members(team_a) + alive_members(team_b)
        random.shuffle(fighters)

        for fighter in fighters:
            if not fighter.is_alive():
                continue  # died earlier this round

            enemies = team_b if fighter in team_a else team_a
            targets = alive_members(enemies)
            if not targets:
                break

            fighter.attack(random.choice(targets))

        round_number += 1

    winner = "Heroes" if alive_members(team_a) else "Monsters"
    print(f"\n*** {winner} win after {round_number - 1} rounds! ***")


# ---- Run it ----
heroes = [Warrior("Conan"), Mage("Merlin"), Archer("Robin")]
monsters = [Warrior("Orc"), Archer("Goblin"), Mage("Wizard")]

print("Heroes:")
for h in heroes:
    print(" ", h)
print("Monsters:")
for m in monsters:
    print(" ", m)

battle(heroes, monsters)

print("\nSurvivors:")
for c in alive_members(heroes + monsters):
    print(" ", c)