import actormanager

ActorManager = actormanager.ActorManager()


ActorManager.SpawnActor(2, 0, 0)
ActorManager.SpawnActor(3, 0, 0)

EnemiesInRoom = ActorManager.ScanAreaForEnemies(0, 0)
while EnemiesInRoom != []:
  for i in range(len(EnemiesInRoom)):
    EnemiesInRoom[i].Hurt(1)
    print('Attacked enemy ' + str(i))

  for i in range(len(EnemiesInRoom)):
    pass
