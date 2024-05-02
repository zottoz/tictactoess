import pygame

# pygame setup
pygame.init()

#tamanho
largura = 600
altura  = 700

# Cores
branco      = (255, 255, 255)
preto       = (0, 0, 0)
vermelho    = (255, 0, 0)
verde       = (0, 255, 0)
azul        = (0, 0, 255)

#configuracoes
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Velha")

fundo = pygame.image.load('img/fundo3.jpg').convert_alpha()
fundo = pygame.transform.scale(fundo, (largura, altura))

screen.blit(fundo, (0,0))
clock = pygame.time.Clock()
running = True
vez = True
vencedor = None
empate = False

# -----------------------------------------------------
matriz = [
    [None, None, None],
    [None, None, None],
    [None, None, None]    
]



# -----------------------------------------------------
# Desenha os retangulos clicaveis
# -----------------------------------------------------
surface_size = (140, 100)
surface1 = pygame.Surface(surface_size, pygame.SRCALPHA)

area1 = surface1.get_rect(topleft=(40, 140))
area2 = surface1.get_rect(topleft=(220, 140))
area3 = surface1.get_rect(topleft=(400, 140))

area4 = surface1.get_rect(topleft=(40, 260))
area5 = surface1.get_rect(topleft=(220, 260))
area6 = surface1.get_rect(topleft=(400, 260))

area7 = surface1.get_rect(topleft=(40, 380))
area8 = surface1.get_rect(topleft=(220, 380))
area9 = surface1.get_rect(topleft=(400, 380))

#surface1.fill(branco)

screen.blit(surface1, area1)
screen.blit(surface1, area2)
screen.blit(surface1, area3)
screen.blit(surface1, area4)
screen.blit(surface1, area5)
screen.blit(surface1, area6)
screen.blit(surface1, area7)
screen.blit(surface1, area8)
screen.blit(surface1, area9)


# -----------------------------------------------------
#     Funcoes apoio
# -----------------------------------------------------
def alerta(msg: str):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(msg, True, branco, vermelho)
    textRect = text.get_rect()
    textRect.center = (200, altura-50)
    screen.blit(text, textRect)

def verificaQuemGanhou():
    pass

def verificaSeEmpatou() -> bool:
    empate = True
    for linha in matriz:
        for elemento in linha:
            if elemento==None:
                empate=False
    return empate

                



# -----------------------------------------------------
# LOOP principal                                      #
#------------------------------------------------------   
while running and vencedor == None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Obter as coordenadas do clique do mouse
            posicao_mouse = pygame.mouse.get_pos()
            x, y = posicao_mouse

            if area1.collidepoint(event.pos) and matriz[0][0] == None:                
                if vez==True:
                    vez=False
                    matriz[0][0] = 1
                    pygame.draw.line(screen, preto, (area1.centerx-50, area1.centery-50),(area1.centerx+50,area1.centery+50), 10)
                    pygame.draw.line(screen, preto, (area1.centerx+50, area1.centery-50),(area1.centerx-50,area1.centery+50), 10)                 
                else:
                    vez=True
                    matriz[0][0] = 2
                    pygame.draw.circle(screen, vermelho, area1.center, 50, 10)

            if area2.collidepoint(event.pos) and matriz[0][1] == None:
                if vez==True:
                    vez=False
                    matriz[0][1] = 1
                    pygame.draw.line(screen, preto, (area2.centerx-50, area2.centery-50),(area2.centerx+50,area2.centery+50), 10)
                    pygame.draw.line(screen, preto, (area2.centerx+50, area2.centery-50),(area2.centerx-50,area2.centery+50), 10)                 
                else:
                    vez=True
                    matriz[0][1] = 2
                    pygame.draw.circle(screen, vermelho, area2.center, 50, 10)

            if area3.collidepoint(event.pos) and matriz[0][2] == None:
                if vez==True:
                    vez=False
                    matriz[0][2] = 1
                    pygame.draw.line(screen, preto, (area3.centerx-50, area3.centery-50),(area3.centerx+50,area3.centery+50), 10)
                    pygame.draw.line(screen, preto, (area3.centerx+50, area3.centery-50),(area3.centerx-50,area3.centery+50), 10)                 
                else:
                    vez=True
                    matriz[0][2] = 2
                    pygame.draw.circle(screen, vermelho, area3.center, 50, 10)

            if area4.collidepoint(event.pos) and matriz[1][0] == None:
                if vez==True:
                    vez=False
                    matriz[1][0] = 1
                    pygame.draw.line(screen, preto, (area4.centerx-50, area4.centery-50),(area4.centerx+50,area4.centery+50), 10)
                    pygame.draw.line(screen, preto, (area4.centerx+50, area4.centery-50),(area4.centerx-50,area4.centery+50), 10)                 
                else:
                    vez=True
                    matriz[1][0] = 2
                    pygame.draw.circle(screen, vermelho, area4.center, 50, 10)

            if area5.collidepoint(event.pos) and matriz[1][1] == None:
                if vez==True:
                    vez=False
                    matriz[1][1] = 1
                    pygame.draw.line(screen, preto, (area5.centerx-50, area5.centery-50),(area5.centerx+50,area5.centery+50), 10)
                    pygame.draw.line(screen, preto, (area5.centerx+50, area5.centery-50),(area5.centerx-50,area5.centery+50), 10)                 
                else:
                    vez=True
                    matriz[1][1] = 2
                    pygame.draw.circle(screen, vermelho, area5.center, 50, 10)

            if area6.collidepoint(event.pos) and matriz[1][2] == None:
                if vez==True:
                    vez=False
                    matriz[1][2] = 1
                    pygame.draw.line(screen, preto, (area6.centerx-50, area6.centery-50),(area6.centerx+50,area6.centery+50), 10)
                    pygame.draw.line(screen, preto, (area6.centerx+50, area6.centery-50),(area6.centerx-50,area6.centery+50), 10)                 
                else:
                    vez=True
                    matriz[1][2] = 2
                    pygame.draw.circle(screen, vermelho, area6.center, 50, 10)

            if area7.collidepoint(event.pos) and matriz[2][0] == None:
                if vez==True:
                    vez=False
                    matriz[2][0] = 1
                    pygame.draw.line(screen, preto, (area7.centerx-50, area7.centery-50),(area7.centerx+50,area7.centery+50), 10)
                    pygame.draw.line(screen, preto, (area7.centerx+50, area7.centery-50),(area7.centerx-50,area7.centery+50), 10)                 
                else:
                    vez=True
                    matriz[2][0] = 2
                    pygame.draw.circle(screen, vermelho, area7.center, 50, 10)

            if area8.collidepoint(event.pos) and matriz[2][1] == None:
                if vez==True:
                    vez=False
                    matriz[2][1] = 1
                    pygame.draw.line(screen, preto, (area8.centerx-50, area8.centery-50),(area8.centerx+50,area8.centery+50), 10)
                    pygame.draw.line(screen, preto, (area8.centerx+50, area8.centery-50),(area8.centerx-50,area8.centery+50), 10)                 
                else:
                    vez=True
                    matriz[2][1] = 2
                    pygame.draw.circle(screen, vermelho, area8.center, 50, 10)

            if area9.collidepoint(event.pos) and matriz[2][2] == None:
                if vez==True:
                    vez=False
                    matriz[2][2] = 1
                    pygame.draw.line(screen, preto, (area9.centerx-50, area9.centery-50),(area9.centerx+50,area9.centery+50), 10)
                    pygame.draw.line(screen, preto, (area9.centerx+50, area9.centery-50),(area9.centerx-50,area9.centery+50), 10)                 
                else:
                    vez=True
                    matriz[2][2] = 2
                    pygame.draw.circle(screen, vermelho, area9.center, 50, 10)

            # ---- atualiza a tela
            pygame.display.update()



    # RENDER YOUR GAME HERE
    if verificaSeEmpatou()==True:
        alerta("O jogo empatou")
    
    # ----------------------------------------------
    # flip() the display to put your work on screen    
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

# ----------------------------------------------
# FIM
pygame.quit()


