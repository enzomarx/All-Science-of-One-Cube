import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

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

# Função para configurar o background
def setup_background():
    glClearColor(0.0, 0.0, 0.2, 1.0)  # Azul tech

# Função para desenhar os eixos
def draw_axes():
    glBegin(GL_LINES)
    # Eixo X (vermelho)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(5, 0, 0)
    # Eixo Y (verde)
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 5, 0)
    # Eixo Z (azul)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 5)
    glEnd()

# Função para desenhar a sombra de encaixe
def draw_shadow(position):
    glPushMatrix()
    glTranslatef(*position)
    glColor4f(0, 0, 0, 0.5)  # Sombra preta semi-transparente
    glScalef(1.1, 1.1, 1.1)  # Aumenta ligeiramente para dar a ideia de encaixe
    draw_cube()
    glPopMatrix()

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

    angle_x = 0  # Ângulo de rotação inicial em torno do eixo X
    angle_y = 0  # Ângulo de rotação inicial em torno do eixo Y
    angle_z = 0  # Ângulo de rotação inicial em torno do eixo Z
    rotation_speed_x = 1  # Velocidade de rotação em torno do eixo X
    rotation_speed_y = 1  # Velocidade de rotação em torno do eixo Y
    rotation_speed_z = 1  # Velocidade de rotação em torno do eixo Z
    move_speed = 0.1  # Velocidade de movimento
    scale = 1.0  # Escala inicial do cubo
    position = np.array([0.0, 0.0, 0.0])  # Posição do cubo
    shadow_position = np.array([2.0, 0.0, 0.0])  # Posição inicial da sombra

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    position[1] += move_speed
                elif event.key == pygame.K_s:
                    position[1] -= move_speed
                elif event.key == pygame.K_a:
                    position[0] -= move_speed
                elif event.key == pygame.K_d:
                    position[0] += move_speed
                elif event.key == pygame.K_q:
                    position[2] += move_speed
                elif event.key == pygame.K_e:
                    position[2] -= move_speed
                elif event.key == pygame.K_i:
                    rotation_speed_x += 0.1
                elif event.key == pygame.K_k:
                    rotation_speed_x -= 0.1
                elif event.key == pygame.K_j:
                    rotation_speed_y += 0.1
                elif event.key == pygame.K_l:
                    rotation_speed_y -= 0.1
                elif event.key == pygame.K_u:
                    rotation_speed_z += 0.1
                elif event.key == pygame.K_o:
                    rotation_speed_z -= 0.1
                elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    scale += 0.1
                elif event.key == pygame.K_MINUS:
                    scale -= 0.1

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glPushMatrix()
        glTranslatef(*position)
        glScalef(scale, scale, scale)
        glRotatef(angle_x, 1, 0, 0)  # Rotaciona o cubo em torno do eixo X
        glRotatef(angle_y, 0, 1, 0)  # Rotaciona o cubo em torno do eixo Y
        glRotatef(angle_z, 0, 0, 1)  # Rotaciona o cubo em torno do eixo Z
        draw_cube()
        glPopMatrix()

        draw_axes()  # Desenha os eixos
        draw_shadow(shadow_position)  # Desenha a sombra de encaixe

        # Verifica se o cubo está alinhado com a sombra
        if np.allclose(position, shadow_position, atol=0.1):
            print("Encaixe perfeito! Próximo nível...")

        pygame.display.flip()
        
        angle_x += rotation_speed_x  # Incrementa o ângulo de rotação em torno do eixo X
        if angle_x >= 360:
            angle_x -= 360
        
        angle_y += rotation_speed_y  # Incrementa o ângulo de rotação em torno do eixo Y
        if angle_y >= 360:
            angle_y -= 360

        angle_z += rotation_speed_z  # Incrementa o ângulo de rotação em torno do eixo Z
        if angle_z >= 360:
            angle_z -= 360
        
        clock.tick(60)

if __name__ == "__main__":
    main()
