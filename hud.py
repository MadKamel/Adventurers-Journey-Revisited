import os
def Refresh(PlayerActor):
  os.system('clear')
  DispPosLen = 4
  DispX = [abs(len(str(PlayerActor.PosX)) - DispPosLen), str(PlayerActor.PosX)]
  DispY = [abs(len(str(PlayerActor.PosY)) - DispPosLen), str(PlayerActor.PosY)]
  DispHP = [abs(len(str(PlayerActor.HitPoints)) - DispPosLen), str(PlayerActor.HitPoints)]
  DispARM = [abs(len(str(PlayerActor.ArmourValue)) - DispPosLen), str(PlayerActor.ArmourValue)]


  print('\033[91m| X: ' + DispX[1] + ' '*DispX[0] + ' | Y: ' + DispY[1] + ' '*DispY[0] + ' | HP: ' + DispHP[1] + ' '*DispHP[0] + ' | ARMOUR:' + DispARM[1] + ' '*DispARM[0] + ' |')
  print('|_________|_________|__________|_____________|')
  print('\033[92m')
