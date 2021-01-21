import actormanager, time, dice, player, hud, keywords

ActorManager = actormanager.ActorManager()
PlayerActor = player.PlayerActor(10, 15, 2, 0, 0)


ActorManager.SpawnActor(2, 0, 1)
ActorManager.SpawnActor(2, 0, 1)
ActorManager.SpawnActor(3, 0, 1)

while True:
  EnemiesInRoom = ActorManager.ScanAreaForEnemies(PlayerActor.PosX, PlayerActor.PosY)
  GoblinCount = len(ActorManager.ScanAreaForActors(PlayerActor.PosX, PlayerActor.PosY, 2))
  OrcCount = len(ActorManager.ScanAreaForActors(PlayerActor.PosX, PlayerActor.PosY, 3))
  
  #ChestsInRoom = ActorManager.ScanAreaForObjects(PlayerActor.PosX, PlayerActor.PosY, 1)
  #LockedChestsInRoom = ActorManager.ScanAreaForObjects(PlayerActor.PosX, PlayerActor.PosY, 0)
  if EnemiesInRoom != []:
    hud.Refresh(PlayerActor)
    if len(EnemiesInRoom) == 1: # If there is only one actor
      if EnemiesInRoom[0].ActorType == 2: # If the only actor present is a goblin
        print('There is a goblin here.')
      elif EnemiesInRoom[0].ActorType == 3: # If the only actor present is an orc
        print('There is an orc here.')
    else: # If there are several actors
      Message = 'There ' # "There " is the beginning of the generated sentence
      if OrcCount == 1: # If there is only one orc in the room
        Message = Message + 'is an orc' # "There is an orc" is a generated sentence.
      elif OrcCount > 1: # If there are more than one orc in the room
        Message = Message + 'are ' + str(OrcCount) + ' orcs' # "There are * orcs"
      else: # If there are no orcs in the room.
        if GoblinCount == 1: # If there is only one goblin; in retrospect, impossible to achieve.
          Message = Message + 'is ' # "There is "
        else: # If several goblins
          Message = Message + 'are ' # "There are"
      
      if OrcCount != 0 and GoblinCount != 0: # If there are both goblins and orcs present
        Message = Message + ' and ' # "There are/is * orc(s) and"

      if GoblinCount == 1: # If there is one goblin
        Message = Message + 'a goblin' # "There are/is * orc(s) and a goblin"
      elif GoblinCount > 1: # If there are several goblins
        Message = Message + str(GoblinCount) + ' goblins' # "There are/is * orc(s) and * goblins"

      # This is the final output. As you can probably tell from the comment below, this script has a lot of outputs.
      print(Message + ' here.') # "There {are/is * orc(s)} {and} {are/is} {* goblin(s)} here"

    Command = input('\t=> ').split(' ')

    for i in range(len(Command)):
      if Command[i] in keywords.AttackEnemy:
        pass # Start attack sequence


  else:
    hud.Refresh(PlayerActor) # Refresh Hud
    Command = input('\t=> ').split(' ')

    # Iterate through every word to find keywords
    for i in range(len(Command)):
      if Command[i] in keywords.MoveNorth:
        PlayerActor.MoveTo(PlayerActor.PosX, PlayerActor.PosY + 1)
      
      elif Command[i] in keywords.MoveSouth:
        PlayerActor.MoveTo(PlayerActor.PosX, PlayerActor.PosY - 1)
      
      elif Command[i] in keywords.MoveEast:
        PlayerActor.MoveTo(PlayerActor.PosX + 1, PlayerActor.PosY)
      
      elif Command[i] in keywords.MoveWest:
        PlayerActor.MoveTo(PlayerActor.PosX - 1, PlayerActor.PosY)
