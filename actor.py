import actordefs, dice

class Actor:
  def __init__(self, ActorType):
    self.ActorType = ActorType # Allows for varied actor types
    self.ActorData = [0, 0, 0, 0, 0, 0] # Actor state flags

  def Spawn(self, SpawnX, SpawnY):
    if self.ActorData[4] == 0: # Checks to see if enemy has not been spawned
      self.ActorData[0] = actordefs.Find(self.ActorType, 0) # Health
      self.ActorData[1] = actordefs.Find(self.ActorType, 1) # Armour
      self.ActorData[2] = SpawnX
      self.ActorData[3] = SpawnY
      self.ActorData[4] = actordefs.Find(self.ActorType, 3) # Spawn status: 0=unspawned, 1=spawned, 2=dead, 3=object
      self.ActorData[5] = actordefs.Find(self.ActorType, 2) # Damage Multiplier

  def Kill(self):
    self.ActorData[0] = 0 # Set health to zero
    self.ActorData[4] = 2 # Set status to dead; cannot be spawned

  def Hurt(self, Damage):
    if self.ActorData[4] == 1: # Check to see if enemy spawned and is alive
      self.ActorData[0] = self.ActorData[0] - Damage
      if self.ActorData[0] <= 0: # If health is equal to or below zero
        self.Kill()
        return 1 # Attack successful, enemy down
      else:
        return 0 # Attack successful, enemy alive
    else:
      return -2 # Attack failed, enemy dead

  def Attack(self):
    if self.ActorData[4] == 1:
      Roll = dice.Roll()
      if Roll != 1: # If the enemy rolled anything other than a one
        return int((Roll * self.ActorData[5]) / 10) + 1 # Calculates damage output
      else:
        return -1 # Enemy rolled one
    else:
      return -2 # Enemy dead, cannot attack

  def Move(self, NewX, NewY):
    self.ActorData[2] = NewX
    self.ActorData[3] = NewY

  def Use(self):
    if self.ActorData[4] == 3: # Check to see if actor is an object
      pass
