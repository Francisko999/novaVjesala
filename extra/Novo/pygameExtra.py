from dependencies import *

def randomColor():
    return random.randrange(255) ,random.randrange(255),random.randrange(255)

class varijable:
    events=[
        pygame.QUIT,
        pygame.ACTIVEEVENT,
        pygame.KEYDOWN,
        pygame.KEYUP,
        pygame.MOUSEMOTION,
        pygame.MOUSEBUTTONUP,
        pygame.MOUSEBUTTONDOWN,
        pygame.JOYAXISMOTION,
        pygame.JOYBALLMOTION,
        pygame.JOYHATMOTION,
        pygame.JOYBUTTONUP,
        pygame.JOYBUTTONDOWN,
        pygame.VIDEORESIZE,
        pygame.VIDEOEXPOSE,
        pygame.USEREVENT
    ]
    eventsQuery={
        pygame.QUIT:{},
        pygame.ACTIVEEVENT:{},
        pygame.KEYDOWN:{},
        pygame.KEYUP:{},
        pygame.MOUSEMOTION:{},
        pygame.MOUSEBUTTONUP:{},
        pygame.MOUSEBUTTONDOWN:{},
        pygame.JOYAXISMOTION:{},
        pygame.JOYBALLMOTION:{},
        pygame.JOYHATMOTION:{},
        pygame.JOYBUTTONUP:{},
        pygame.JOYBUTTONDOWN:{},
        pygame.VIDEORESIZE:{},
        pygame.VIDEOEXPOSE:{},
        pygame.USEREVENT:{}
    }
    def showEventsQuery():
        for key, value in varijable.eventsQuery.items():
            print(key, ' : ', value)
    #screenGame=None
    EditorZoom=1
    GameZoom=1
    GamePan =(0,0)
    screenSize=1200,700
    screenReSized=False
    screenGameSize=1080,640
    screenGameCurentSize=screenGameSize
    MainLoop=True
    GrupaEditor=[]
    koordinateProzoraX=50
    koordinateProzoraY=50
    #"""
    screen = pygame.display.set_mode((300,300), pygame.RESIZABLE)
    #"""

class eventInterakcija:
    def __init__(self,ime=""):
        if ime=="":
            self.ime= str(random.getrandbits(128))
            #print("nasumično ime:",self.ime)
        else:
            self.ime=ime        
        try:varijable.eventsQuery[pygame.QUIT           ].update ({self.ime:self.QUIT           })
        except:pass
        try:varijable.eventsQuery[pygame.KEYDOWN        ].update ({self.ime:self.KEYDOWN        })
        except:pass
        try:varijable.eventsQuery[pygame.ACTIVEEVENT    ].update ({self.ime:self.ACTIVEEVENT    })
        except:pass
        try:varijable.eventsQuery[pygame.KEYUP          ].update ({self.ime:self.KEYUP          })
        except:pass
        try:varijable.eventsQuery[pygame.MOUSEMOTION    ].update ({self.ime:self.MOUSEMOTION    })
        except:pass
        try:varijable.eventsQuery[pygame.MOUSEBUTTONUP  ].update ({self.ime:self.MOUSEBUTTONUP  })
        except:pass
        try:varijable.eventsQuery[pygame.MOUSEBUTTONDOWN].update ({self.ime:self.MOUSEBUTTONDOWN})
        except:pass
        try:varijable.eventsQuery[pygame.JOYAXISMOTION  ].update ({self.ime:self.JOYAXISMOTION  })
        except:pass
        try:varijable.eventsQuery[pygame.JOYBALLMOTION  ].update ({self.ime:self.JOYBALLMOTION  })
        except:pass
        try:varijable.eventsQuery[pygame.JOYHATMOTION   ].update ({self.ime:self.JOYHATMOTION   })
        except:pass
        try:varijable.eventsQuery[pygame.JOYBUTTONUP    ].update ({self.ime:self.JOYBUTTONUP    })
        except:pass
        try:varijable.eventsQuery[pygame.JOYBUTTONDOWN  ].update ({self.ime:self.JOYBUTTONDOWN  })
        except:pass
        try:varijable.eventsQuery[pygame.VIDEORESIZE    ].update ({self.ime:self.VIDEORESIZE    })
        except:pass
        try:varijable.eventsQuery[pygame.VIDEOEXPOSE    ].update ({self.ime:self.VIDEOEXPOSE    })
        except:pass
        try:varijable.eventsQuery[pygame.USEREVENT      ].update ({self.ime:self.USEREVENT      })
        except:pass



class objekt0(eventInterakcija):
    def QUIT(self,ev):
        varijable.MainLoop=False
    #def ACTIVEEVENT(self,ev):pass
    def KEYDOWN(self,ev):
        if ev.key == pygame.K_ESCAPE:
            varijable.MainLoop=False
    #def KEYUP(self,ev):pass
    def MOUSEMOTION(self,ev):
        pass
        """inp=pygame.mouse
        mx,my=inp.get_pos()
        ex, ey = win32api.GetCursorPos()
        pgwX=ex-mx
        pgwY=ey-my
        if(varijable.koordinateProzoraX!=pgwX or varijable.koordinateProzoraY!=pgwX):
            #global sucelja
            if(len(varijable.sucelja)):
                #pass
                varijable.koordinateProzoraX=pgwX
                varijable.koordinateProzoraY=pgwY
                varijable.sucelja[0].geometry('%dx%d+%d+%d' % (200, 400, varijable.sucelja[0].getX(), varijable.sucelja[0].getY()))#varijable.koordinateProzoraX, varijable.koordinateProzoraY
                print(varijable.sucelja[0].getX(), varijable.sucelja[0].getY())"""
        
    #def MOUSEBUTTONUP(self,ev):pass
    #def MOUSEBUTTONDOWN(self,ev):pass
    #def JOYAXISMOTION(self,ev):pass
    #def JOYBALLMOTION(self,ev):pass
    #def JOYHATMOTION(self,ev):pass
    #def JOYBUTTONUP(self,ev):pass
    #def JOYBUTTONDOWN(self,ev):pass
    def VIDEORESIZE(self,ev):pass
    #def VIDEOEXPOSE(self,ev):pass
    #def USEREVENT(self,ev):pass 

class pgSquare(eventInterakcija):
    povrsine=[]
    def __init__(self,surf,ime="",x=0,y=0,w=0,h=0,color=(0,0,0),alpha=255,image=""):
        super().__init__(ime)
        self.Surface=pygame.Surface((w,h))
        self.Surface.fill(color)
        self.Surface.set_alpha(alpha)
        self.x=x
        self.y=y
        self.rect=pygame.Rect((self.gX,self.gY,w,h))
        self.w=w
        self.h=h
        self.color=color
        self.alpha=alpha
        self.surf=surf
        self.gX,self.gY=self.getGlobalXY()
        print(self.ime,self.getGlobalXY())

        self.mousePropagate=True


        pgSquare.povrsine.append(self)
        self.markBox()
    def blitMe(self):
        try:
            self.surf.Surface.blit(self.Surface,(self.x,self.y))
        except:
            self.surf.blit(self.Surface,(self.x,self.y))

    def MOUSEBUTTONDOWN(self,ev):
        x,y=ev.pos
        xx,yy=self.gX,self.gY
        print(self.ime,self.rect.collidepoint(x, y))
        wx,hy=self.w+xx,self.h+yy
        """if(
            x>=xx and
            x<=wx and
            y>=yy and
            y<=hy
            ):
            
            print("stisnuo si ",self.ime)"""
        
        #print(x,y,xx,yy,wx,hy)

    def getGlobalXY(self):
        print(self.ime,"try",self.surf)
        """try:
            print(self.ime,"try",self.surf)
            #mx,my=self.surf.getGlobalXY()
        except:
            #mx,my=self.x,self.y
            print(self.ime,"exc")"""
        #UkupniX,UkupniY=mx+self.x,my+self.y
        #return UkupniX,UkupniY
        return 0,0
    def markBox(self):
        pygame.draw.rect(varijable.screen,(255,0,0),[5,5,30,30])

def izvrsiEditorEvente(event):
    #za svaki unos funkcije za događaj dotičnog tipa ... izvrši je
    #for ObjIme in varijable.eventsQuery[event.type]:
    brojac=0
    
    while (brojac<len(varijable.eventsQuery[event.type])):
        ObjIme=list(varijable.eventsQuery[event.type])[brojac]#varijable.eventsQuery[event.type][brojac]

        varijable.eventsQuery[event.type][ObjIme](event)

        brojac+=1

def ucitajObjekte():
    o0=objekt0()
    s1=pgSquare(varijable.screen,"veliki",100,30,100,100,randomColor())
    s2=pgSquare(s1,"mali",5,10,50,50,randomColor())