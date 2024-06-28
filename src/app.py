import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Função para desenhar um cubo
def draw_cube():
    glBegin(GL_QUADS)
    
    glColor3fv((0.8, 0.2, 0.2))  # Face vermelha
    glVertex3fv((1, 1, -1))
    glVertex3fv((1, -1, -1))
    glVertex3fv((-1, -1, -1))
    glVertex3fv((-1, 1, -1))

    glColor3fv((0.2, 0.8, 0.2))  # Face verde
    glVertex3fv((1, 1, 1))
    glVertex3fv((1, -1, 1))
    glVertex3fv((1, -1, -1))
    glVertex3fv((1, 1, -1))

    glColor3fv((0.2, 0.2, 0.8))  # Face azul
    glVertex3fv((-1, 1, 1))
    glVertex3fv((-1, -1, 1))
    glVertex3fv((1, -1, 1))
    glVertex3fv((1, 1, 1))

    glColor3fv((0.8, 0.8, 0.2))  # Face amarela
    glVertex3fv((-1, 1, -1))
    glVertex3fv((-1, -1, -1))
    glVertex3fv((-1, -1, 1))
    glVertex3fv((-1, 1, 1))

    glColor3fv((0.8, 0.2, 0.8))  # Face rosa
    glVertex3fv((1, 1, -1))
    glVertex3fv((1, 1, 1))
    glVertex3fv((-1, 1, 1))
    glVertex3fv((-1, 1, -1))

    glColor3fv((0.2, 0.8, 0.8))  # Face ciano
    glVertex3fv((1, -1, -1))
    glVertex3fv((1, -1, 1))
    glVertex3fv((-1, -1, 1))
    glVertex3fv((-1, -1, -1))

    glEnd()

# Função para desenhar o texto "MARK"
def draw_mark_text():
    mark_text = "MARK"
    font = pygame.font.SysFont(None, 48)
    text_surface = font.render(mark_text, True, (1, 1, 1))
    text_width = text_surface.get_width()
    text_height = text_surface.get_height()
    
    # Calcula as coordenadas do texto para o centro da tela
    text_x = -text_width / 2
    text_y = -text_height / 2
    
    glRasterPos2d(text_x, text_y)
    glDrawPixels(text_width, text_height, GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tostring(text_surface, "RGBA", True))

# Função para configurar o background
def setup_background():
    glClearColor(0.0, 0.0, 0.2, 1.0)  # Azul tech

# Função principal
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption("MARK")

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    clock = pygame.time.Clock()

    setup_background()

    angle_x = 200  # Ângulo de rotação inicial em torno do eixo X
    angle_y = 0  # Ângulo de rotação inicial em torno do eixo Y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glPushMatrix()
        glRotatef(angle_x, 1, 0, 0)  # Rotaciona o cubo em torno do eixo X
        glRotatef(angle_y, 0, 1, 0)  # Rotaciona o cubo em torno do eixo Y
        draw_cube()
        glPopMatrix()
        
        draw_mark_text()  # Desenha o texto "MARK"
        
        pygame.display.flip()
        
        angle_x += 1  # Incrementa o ângulo de rotação em torno do eixo X
        if angle_x >= 360:
            angle_x -= 360
        
        angle_y += 1 # Incrementa o ângulo de rotação em torno do eixo Y
        if angle_y >= 360:
            angle_y -= 360
        
        clock.tick(60)

if __name__ == "__main__":
    main()
