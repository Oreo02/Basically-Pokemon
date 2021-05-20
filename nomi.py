import random

class Nomi():

  def __init__(self, name, type, hp, att_speed, att, energy, defense, mood, moveSet):
    self.name = name
    self.type = type
    self.hp = hp
    self.att_speed = att_speed
    self.att = att
    self.energy = energy
    self.defense = defense
    self.moveSet = moveSet


class Move():
  def __init__(self, name, power, consumption, priority, mood_bonus, mood):
    self.name = name
    self.power = power
    self.consumption = consumption
    self.priority = priority
    self.moody = moody
    if (self.moody == mood):
      self.bonus = 1.25
    else:
      self.bonus = 1.0


class Tail_Slap(Move):
  def __init__(self, mood):
    Move.__init__(self, "Tail Slap", 20, 10, 0, 1.0, "none")

class Fake_Fire(Move):
  def __init__(self, mood):
    Move.__init__(self, "Fake Fire", 5, 20, .5, )

def calculateDamage(self, move, attack):
  bonus = move.bonus

  randMod =  random.uniform(0.9, 1.1)
  crit = random.randint(1,100)
  if crit <= 5:
    bonus += 1.0

  atkMod = bonus * randMod
  defense = self.defense

  damage = (attack +(move.power * atkMod)) - (1.5 * defense)
  self.health = self.health - damage

  if self.health < 0:
    self.health = 0

