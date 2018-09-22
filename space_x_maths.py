# SPACE X MATHS

# Importation des modules
from random import *
import pygame
from pygame.locals import *
import time

# Initialisation
pygame.init()
# Création de la fenêtre et de son titre
fenetre = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Space X Maths')
# Non affichage de la souris
pygame.mouse.set_visible(0)
# Repertoire pour ressources
import os

os.chdir("data")
# Chargement de l'image d'intro
intro = pygame.image.load("intro.jpg")
# Chargement de l'image de fond
fond = pygame.image.load("background.jpg").convert()
# Chargement de la musique de fond
pygame.mixer.music.load("backmusic.mp3")
# Chargement des effets sonores
explosion = pygame.mixer.Sound("explosion.wav")
explosionf = pygame.mixer.Sound("explosion finale.wav")
# Chargement du sprite
sprite = pygame.image.load("spaceship.png").convert_alpha()
sprite_x = 20
sprite_y = randrange(3, 350)
# Chargement de la météorite
met1 = pygame.image.load("meteore (1).png").convert_alpha()
met2 = pygame.image.load("meteore (2).png").convert_alpha()
met3 = pygame.image.load("meteore (3).png").convert_alpha()
met1_x = 640
met1_y = randrange(0, 134)
met2_x = 640
met2_y = randrange(134, 268)
met3_x = 640
met3_y = randrange(268, 402)
fenetre.blit(met1, (met1_x, met1_y))
fenetre.blit(met2, (met2_x, met2_y))
fenetre.blit(met3, (met3_x, met3_y))
# Chargement des fonds de calcul mental et de fin de jeu
fin = pygame.image.load("end.jpg").convert()
# Rafraîchissement
pygame.display.flip()


# Fonctions pour actualiser les éléments de la fenêtre
def refresh():
    fenetre.blit(fond, (0, 0))
    fenetre.blit(sprite, (sprite_x, sprite_y))
    fenetre.blit(met1, (met1_x, met1_y))
    fenetre.blit(met2, (met2_x, met2_y))
    fenetre.blit(met3, (met3_x, met3_y))
    fenetre.blit(score_display, (590, 10))
    pygame.display.flip()


# Maintien de la touche
pygame.key.set_repeat(1, 20)

# Différentes variables du jeu
mvt = -1  # Pour la fenêtre d'intro
duree = 15
z = 5  # Pour la vitesse du vaisseau spatial
d_chute1 = 0.5  # Vitesses d'arrivée des météorites
d_chute2 = 0.75
d_chute3 = 1
s = 0  # Pour le score
m = 0  # Nombre de météorites tombées
me = 0  # Nombre de météorites évitées
mp = 0  # Nombre de météorites percutées
tcalc = 20  # Temps avant la venue du calcul
length = 15
cp_calc = 0  # Nombre de calculs mentaux survenus
calc_p = 0  # Nombre de calculs mentaux ratés
aff = []
victory = True

# Maintien de la touche
pygame.key.set_repeat(1, 20)

# FENETRE D'INTRODUCTION/MENU
fenetre.blit(intro, (0, 0))
pygame.display.flip()
intro_aff = 1
while intro_aff > 0:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                intro_aff = -1
                mvt = 5
                victory = True
    import generateur
while mvt == 5:
    fenetre.blit(fond, (0, 0))
    fenetre.blit(sprite, (sprite_x, sprite_y))
    pygame.display.flip()
    pygame.mixer.music.play(10)
    # Le décompte commence au collage des éléments
    start = time.time()
    # BOUCLE PRINCIPALE

    while mvt > 0:
        # Affichage score
        font = pygame.font.SysFont(None, 60)
        score_display = font.render(str(s), 1, (255, 255, 0))
        fenetre.blit(score_display, (590, 10))
        pygame.display.flip()

        for event in pygame.event.get():
            # Déplacement du vaisseau spatial
            if event.type == KEYDOWN:
                # Vers le haut
                if event.key == K_UP:
                    if sprite_y >= 3:
                        sprite_y -= 4
                        refresh()
                # Vers le bas
                if event.key == K_DOWN:
                    if sprite_y <= 344:
                        sprite_y += 4
                        refresh()
                # Vers la gauche
                if event.key == K_LEFT:
                    if sprite_x >= 3:
                        sprite_x -= 4
                        refresh()
                # Vers la droite
                if event.key == K_RIGHT:
                    if sprite_x <= 437:
                        sprite_x += 4
                        refresh()

        # Arrivée des météorites
        met1_x -= d_chute1
        refresh()
        if met1_x < -76:
            d_chute1 += 0.01
            s += 1
            met1_x = 590
            met1_y = randrange(0, 143)
            refresh()
        met2_x -= d_chute2
        refresh()
        if met2_x < -76:
            d_chute2 += 0.01
            s += 1
            met2_x = 590
            met2_y = randrange(143, 286)
            refresh()
        met3_x -= d_chute3
        if met3_x < -76:
            d_chute3 += 0.01
            s += 1
            met3_x = 590
            met3_y = randrange(286, 429)
            refresh()

        # Collisions
        if sprite_x - 52 <= met1_x <= sprite_x + 160 and sprite_y - 50 <= met1_y <= sprite_y + 106:
            explosion.play()
            mp += 1
            met1_x = -76
            s -= 1
        if sprite_x - 50 <= met2_x <= sprite_x + 160 and sprite_y - 50 <= met2_y <= sprite_y + 106:
            explosion.play()
            mp += 1
            met2_x = -76
            s -= 1
        if sprite_x - 67 <= met3_x <= sprite_x + 160 and sprite_y - 50 <= met3_y <= sprite_y + 106:
            explosion.play()
            mp += 1
            met3_x = -76
            s -= 1

        # Calcul mental
        if time.time() - start >= tcalc:
            time.sleep(1)
            print("probleme detect dans les circuits internes du vaisseau")
            aff = generateur.calcul(generateur.type(), generateur.niveau(generateur.cp_calc))
            print(aff[0], aff[1], aff[2], ' = ')
            compteur = time.time()
            rep = input()
            if time.time() - compteur < length:
                continuer = True
            else:
                continuer = False
            if continuer == True:
                victory = generateur.verification(rep, aff[3])
            else:
                victory = False
            if victory == True:
                cp_calc += 1
                print("Probleme resolu")
                time.sleep(2)
                start = time.time()
            else:
                calc_p += 1
                if calc_p == 1:
                    print("Le vaisseau subit de legers dommages")
                elif calc_p == 2:
                    print("Le vaisseau subit de lourds degats")
                else:
                    print("Le vaisseau n'est plus en mesure de voler")
                time.sleep(2)
                start = time.time()
        # Boucles de fin de jeu
        if (mp >= 10) or (calc_p >= 3):
            refresh
            mvt = 0
            z = 0
            d_chute1 = 0
            d_chute2 = 0
            d_chute3 = 0
            pygame.mixer.music.stop()
            explosionf.play()
            fenetre.blit(fin, (0, 0))
            pygame.display.flip()
            # AFFICHAGE DU SCORE
            # Boucle nécessaire à l'affichage du score
            font = pygame.font.Font(None, 32)
            # Texte
            text = font.render("Pour vous la partie s'arrete ici, votre score final est de " + str(s) + ".", 1,
                               (255, 255, 255))
            # Texte centré en haut de l'image
            textpos = text.get_rect(centerx=fond.get_width() / 2)
            fenetre.blit(text, textpos)

    # Raffraichissement final
    pygame.display.flip()
