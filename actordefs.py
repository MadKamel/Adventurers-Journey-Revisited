def Find(ActorType, Request):
  
  # Get health for actor
  if Request == 0:
    if ActorType < 2: # Objects/Decor
      return -1
    elif ActorType == 2: # Goblin
      return 10
    elif ActorType == 3: # Orc
      return 15

  # Get armour for actor
  elif Request == 1:
    if ActorType < 2: # Objects/Decor
      return -1
    elif ActorType == 2: # Goblin
      return 5
    elif ActorType == 3: # Orc
      return 8

  # Get max damage for actor
  elif Request == 2:
    if ActorType < 2: # Objects/Decor
      return -1
    elif ActorType == 2: # Goblin
      return 2
    elif ActorType == 3: # Orc
      return 4

  elif Request == 3:
    if ActorType < 2:
      return 3
    else:
      return 1
