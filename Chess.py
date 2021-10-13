#use of tags (i.e. can move as Pawn, cannot be King, can use Warp, etc.) that can be applied to any piece (i.e. if I want the Jester to move like a Pawn, I could simply write jester=movesLikePawn or whatever)
#M U L T I P L A Y E R            0_0

import math
import pygame
if __name__ == '__main__':
  pygame.init()
  beeperside = 8
  blockThiccness = 100
  borderperside = 2
  buttonAreaSpace = 200
  canvas_height = beeperside * blockThiccness + borderperside * 2
  canvas_weight = beeperside * blockThiccness + borderperside * 2 + buttonAreaSpace

  gameDisplay = pygame.display.set_mode((canvas_height, canvas_weight))

  def boardmaking():
    block_index = 0
    x = 4
    y = 4
    for a in range(beeperside):
      for b in range(beeperside):
        color = (0, 0, 0) if block_index % 2 == 0 else (255, 255, 255)
        r = pygame.Rect(x, y, blockThiccness, blockThiccness)
        pygame.draw.rect(gameDisplay, color, r)
        x += blockThiccness
        y += blockThiccness
        block_index += 1

  pygame.display.set_caption('Yes')
  clock = pygame.time.Clock()

  def event_handling(started, crashed):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        crashed = True
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          crashed = True
    return (started, crashed)

  def game_loop():
    crashed = False
    started = False
    while not crashed:
      started, crashed = event_handling(started, crashed)
      #poor phil gameDisplay.fill((20, 20, 20))
      pygame.display.update()
      clock.tick()

  boardmaking()
  game_loop()
  pygame.quit()
  quit()
