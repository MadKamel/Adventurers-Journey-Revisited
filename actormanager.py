import actor

class ActorManager:
  def __init__(self):
    self.Actors = []
  
  def AddActor(self, ActorType):
    self.Actors.append(actor.Actor(ActorType))
    return len(self.Actors) - 1
  
  def SpawnActor(self, ActorType, SpawnX, SpawnY):
    self.Actors.append(actor.Actor(ActorType))
    self.Actors[len(self.Actors) - 1].Spawn(SpawnX, SpawnY)
    return len(self.Actors)

  def ScanArea(self, AreaX, AreaY):
    Result = []
    for i in range(len(self.Actors)):
      if self.Actors[i].ActorData[2] == AreaX and self.Actors[i].ActorData[3] == AreaY and self.Actors[i].ActorData[4] != 0:
        Result.append(self.Actors[i])
    return Result

  def ScanWorld(self):
    Result = []
    for i in range(len(self.Actors)):
      if self.Actors[i].ActorData[4] != 0:
        Result.append(self.Actors[i])
    return Result

  def ScanActors(self, ActorType):
    Result = []
    for i in range(len(self.Actors)):
      if self.Actors[i].ActorData[4] != 0 and self.Actors[i].ActorType == ActorType:
        Result.append(self.Actors[i])
    return Result

  def ScanAreaForEnemies(self, AreaX, AreaY):
    Result = []
    for i in range(len(self.Actors)):
      if self.Actors[i].ActorData[2] == AreaX and self.Actors[i].ActorData[3] == AreaY and self.Actors[i].ActorData[4] == 1:
        Result.append(self.Actors[i])
    return Result

  def ScanAreaForActors(self, AreaX, AreaY, ActorType):
    Result = []
    for i in range(len(self.Actors)):
      if self.Actors[i].ActorData[2] == AreaX and self.Actors[i].ActorData[3] == AreaY and self.Actors[i].ActorData[4] == 1 and self.Actors[i].ActorType == ActorType:
        Result.append(self.Actors[i])
    return Result
