from p2 import *
from p4 import *

pygame.init()
screen = pygame.display.set_mode((100,100), pygame.RESIZABLE)
t=tkinter.Tk()
run=True

p1obj=p1class()
p1class.x=20
def p1fun(self):
    return self.x
p1class.y=p1fun

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False
    
    screen.fill((0,0,0))
    pygame.display.flip()
    t.update()
    #print(screen.get_size())
    print(p1obj.y())