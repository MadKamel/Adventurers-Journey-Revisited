import actor

class ActorManager:
  def __init__(self):
    self.Actors = []
  
  def AddActor(self, ActorType):
    self.Actors.append(actor.Actor(ActorType))
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

  def ScanObjects(self, ActorType):
    Result = []
    for i in range(len(self.Actors)):
      if self.Actors[i].ActorData[4] != 0 and self.Actors[i].ActorType == ActorType:
        Result.append(self.Actors[i])
    return Result
