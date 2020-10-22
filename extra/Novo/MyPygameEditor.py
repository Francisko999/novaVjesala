from pygameExtra import *

pygame.init()
#screen = pygame.display.set_mode((200,200), pygame.RESIZABLE)
programIcon = pygame.image.load("media/missle.png")
pygame.display.set_icon(programIcon)



def blitAll():
    pgSquare.povrsine[0].blitMe()
    pgSquare.povrsine[1].blitMe()


ucitajObjekte()
while varijable.MainLoop:
    """for event in pygame.event.get():
        if event.type==pygame.QUIT:
            varijable.MainLoop=False"""
    for event in pygame.event.get():
        izvrsiEditorEvente(event)
    
    varijable.screen.fill((0,0,0))
    
    blitAll()
    pygame.display.flip()
    print(varijable.eventsQuery[6].__name__)