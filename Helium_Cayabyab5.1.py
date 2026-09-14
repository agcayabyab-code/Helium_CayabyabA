#defining a Hero class
class Hero:

  #attributes of the hero
  def __init__(self, name, health, attack):
    self.name = name
    self.health = health
    self.attack = attack

  #string representation of the hero
  def __repr__(self):
    return f"I'm {self.name} with {self.health} health and {self.attack} attack"

  #taking damage 
  def take_damage(self, damage):
    self.health -= damage
    if self.health < 0:
      self.health = 0

  #attacking with attack stats 
  def attack(self):
    return self.attack

#creating two heroes
arthur = Hero("Arthur", 100, 15)
morgana = Hero("Morgana", 100, 10)

#morgana attacks arthur
arthur.take_damage(morgana.attack)
print(f"Arthur's health after taking damage from Morgana: {arthur.health}")

#printing hp of both heroes
print(arthur)
print(morgana)