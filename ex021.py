import pygame

pygame.init()
pygame.mixer.init()

musica = "ex021.mp3"

pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

pause = False

while True:
    print("Digite 'S' para sair ou 'P' para pausar/despausar.")
    query = str(input(" ")).strip()[0]

    if query in "Ss":
        break

    elif query in "Pp":
        if pause == False:
            pygame.mixer.music.pause()
            pause = True

        else:
            pygame.mixer.music.unpause()
            pause = False

    else:
        print("Comando inválido, (Digite 'S' para sair ou 'P' para pausar/despausar.)")
