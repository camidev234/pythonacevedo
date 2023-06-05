import pygame

run = True
width = 400
height = 100
#usa funcion init para inicializar una nueva app con pygame
pygame.init()
#usa display set mode para configurar la ventanna donde va a correr la aplicacon
screen = pygame.display.set_mode((width, height))
# usa sysfont para crear una fuente y tiene como parametros el tipo y tamaño de letra
font = pygame.font.SysFont(None, 15)
# renderiza el texto con el color
text = font.render("Bienvenido a pygame", True, (100,255,200))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# 
pygame.display.flip()
# mientras el programa corre
while run:
    # recorre los eventos 
    for event in pygame.event.get():
        #si el evento es salir  si el evnto es dar click en cualquier parte de la vetana o si se presiona la felcha hacia arriba
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False
        # el run es false