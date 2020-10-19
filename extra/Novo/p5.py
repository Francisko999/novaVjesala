import pygame

pygame.init()
screen = pygame.display.set_mode((200,200), pygame.RESIZABLE)

run=True

class pgSquare:
    povrsine=[]
    def __init__(self,surf,x=0,y=0,w=0,h=0,color=(0,0,0),alpha=255,image=""):
        self.Surface=pygame.Surface((w,h))
        self.Surface.fill(color)
        self.Surface.set_alpha(alpha)
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.color=color
        self.alpha=alpha
        self.surf=surf

        pgSquare.povrsine.append(self)
        
    def blitMe(self):
        self.surf.blit(self.Surface,(self.x,self.y))


def blitAll():
    pgSquare.povrsine[0].blitMe()
    pgSquare.povrsine[1].blitMe()

s1=pgSquare(screen,10,10,100,100,(0,255,0))
s2=pgSquare(s1.surf,10,10,10,10,(0,0,255))
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            run=False
    
    screen.fill((0,0,0))
    
    blitAll()
    pygame.display.flip()
    print(pgSquare.povrsine)