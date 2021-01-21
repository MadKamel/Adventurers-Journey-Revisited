import dice

class PlayerActor:
  def __init__(self, Armour, Health, Damage, SpawnX, SpawnY):
    self.ArmourValue = Armour
    self.HitPoints = Health
    self.DeathFlag = 0 # 0=alive, 1=dead
    self.DmgMultiplier = Damage # How many times to roll on an attack
    self.PosX = SpawnX # Positional data.
    self.PosY = SpawnY # Ditto.

  def Kill(self):
    self.HitPoints = 0 # Set HP to zero.
    self.DeathFlag = 1 # Set player to be dead.

  def Hurt(self, Damage):
    if self.DeathFlag == 0:
      self.HitPoints = self.HitPoints - Damage
      if self.HitPoints <= 0:
        self.Kill()
        return 0 # Attack successful, player dead.
      else:
        return 1 # Attack successful, player hurt but not dead.
    else:
      return -2 # Attack failed, player already dead.

  def Attack(self):
    if self.DeathFlag == 0:
      PlayerDamage = []
      FinalDamage = 0

      # Roll some dice to find the result.
      for i in range(self.DmgMultiplier):
        PlayerDamage.append(dice.Roll(Max=6))

      # Find sum of PlayerDamage array. Thanks to g4g for the script
      for i in PlayerDamage:
        FinalDamage = FinalDamage + i
      
      return FinalDamage, PlayerDamage # Return player attack strength and individual rolls.

    else:
      return -2 # Attack failed, player dead.

  def MoveTo(self, NewX, NewY):
    self.PosX = NewX
    self.PosY = NewY
