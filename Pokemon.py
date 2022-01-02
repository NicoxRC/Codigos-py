import os
import readchar
import random
import time

obstacle_definition = """\
#### ######################
#### ########### ##########
# ## #####         ########
#           ###### ########
################## ########
################## ##### ##
#################        ##
## ##############   #######
##                  #######
############ ##############
# ########## ##############
#               ###########
############### ###########
############### ######### #
###########               #
#           ###############
# #########################\
"""
pos_x = 0
pos_y = 1
my_position = [4, 0]
map_objects = [[1, 2]]
end_game = False
died = False
finish = True
enemy = 0

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
map_width = len(obstacle_definition[0])
map_height = len(obstacle_definition)

os.system("cls")
print("Eres pikachu derrota a todos los pokemons(*) que hay en el mapa!!\n"
      "(Presiona 'w''a''s''d' para moverte y 'q' dentro del mapa para salir)")
input("Presiona enter para continuar...")

while finish:
    while not end_game:
        os.system("cls")

        print("+" + "-" * map_width * 3 + "+")

        for coordinate_y in range(map_height):

            print("|", end="")

            for coordinate_x in range(map_width):

                char_to_draw = "   "

                trainers = None

                for map_object in map_objects:

                    if map_object[pos_x] == coordinate_x and map_object[pos_y] == coordinate_y:
                        char_to_draw = " * "
                        trainers = map_object

                if my_position[pos_x] == coordinate_x and my_position[pos_y] == coordinate_y:

                    char_to_draw = " @ "

                    if trainers:
                        end_game = True

                if obstacle_definition[coordinate_y][coordinate_x] == "#":
                    char_to_draw = "###"

                print("{}".format(char_to_draw), end="")

            print("|")

        print("+" + "-" * map_width * 3 + "+")

        direction = readchar.readchar().decode()
        new_position = None

        if direction == "w":
            new_position = [my_position[pos_x], (my_position[pos_y] - 1) % map_height]
        elif direction == "s":
            new_position = [my_position[pos_x], (my_position[pos_y] + 1) % map_height]
        elif direction == "a":
            new_position = [(my_position[pos_x] - 1) % map_width, my_position[pos_y]]
        elif direction == "d":
            new_position = [(my_position[pos_x] + 1) % map_width, my_position[pos_y]]
        elif direction == "q":
            finish = False
            end_game = True
        if new_position:
            if obstacle_definition[new_position[pos_y]][new_position[pos_x]] != "#":
                my_position = new_position

    if enemy == 0:
        os.system("cls")
        vida_inicial_pikachu = 100
        vida_inicial_charmander = 80
        vida_pikachu = vida_inicial_pikachu
        vida_charmander = vida_inicial_charmander
        barras = 10

        print("\nEl combate comienza!!")

        barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
        print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                  " " * (barras - barras_de_vida_pikachu),
                                                  vida_pikachu, vida_inicial_pikachu))

        barras_de_vida_charmander = int(vida_charmander * barras / vida_inicial_charmander)
        print("Charmander: [{}{}] ({}/{})".format("*" * barras_de_vida_charmander,
                                                  " " * (barras - barras_de_vida_charmander),
                                                  vida_charmander, vida_inicial_charmander))
        input("Presiona enter...\n")
        os.system("cls")

        while vida_pikachu > 0 and vida_charmander > 0:

            print("\nEs el turno de charmander!!")

            ataque_charmanader = random.randint(1, 2)
            if ataque_charmanader == 1:
                print("Charmander ataca con Arañazo!!\n")
                vida_pikachu -= 20
                print("El daño recibido fue -20!")
            else:
                print("Charmander ataca con Colmillo igneo!!\n")
                vida_pikachu -= 15
                print("El daño recibido fue -15!")

            if vida_pikachu < 0:
                vida_pikachu = 0
            elif vida_charmander < 0:
                vida_charmander = 0

            barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
            print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                      " " * (barras - barras_de_vida_pikachu),
                                                      vida_pikachu, vida_inicial_pikachu))

            barras_de_vida_charmander = int(vida_charmander * barras / vida_inicial_charmander)
            print("Charmander: [{}{}] ({}/{})".format("*" * barras_de_vida_charmander,
                                                      " " * (barras - barras_de_vida_charmander),
                                                      vida_charmander, vida_inicial_charmander))
            input("\nPresione enter para continuar...\n")
            os.system("cls")

            if vida_pikachu > 0:

                print("\nEs el turno de pikachu!!")
                ataque_pikachu = None
                while ataque_pikachu != "q" and ataque_pikachu != "w" and ataque_pikachu != "e" \
                        and ataque_pikachu != "r":
                    ataque_pikachu = input("\nQue ataque deseas realizar? [q]Impactrueno, [w]Embestida, "
                                           "[e]Ataque rapido: ")

                    if ataque_pikachu == "q":
                        print("pikachu ataca con impactrueno!!\n")
                        v = random.randint(30, 40)
                        vida_charmander -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "w":
                        print("pikachu ataca con embestida!!\n")
                        v = random.randint(20, 30)
                        vida_charmander -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "e":
                        print("pikachu ataca con ataque rapido!!\n")
                        vida_charmander -= 15
                        print("El daño hecho fue -15!!")

                if vida_pikachu < 0:
                    vida_pikachu = 0
                elif vida_charmander < 0:
                    vida_charmander = 0

                barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
                print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                          " " * (barras - barras_de_vida_pikachu),
                                                          vida_pikachu, vida_inicial_pikachu))

                barras_de_vida_charmander = int(vida_charmander * barras / vida_inicial_charmander)
                print("Charmander: [{}{}] ({}/{})".format("*" * barras_de_vida_charmander,
                                                          " " * (barras - barras_de_vida_charmander),
                                                          vida_charmander, vida_inicial_charmander))
                input("\nPresione enter para continuar...\n")
                os.system("cls")

        if vida_pikachu > vida_charmander:
            print("Pikachu es el ganador!!")
            print("Pikachu a subido de nivel ahora tiene mas vida, daño, y aprendio un nuevo movimiento!!")
            end_game = False
            enemy += 1
            map_objects.pop(0)
            map_objects.append([16, 1])
            time.sleep(4)
        else:
            print("\nCharmander es el ganador!!")
            finish = False
            died = True
            time.sleep(2.5)
    elif enemy == 1:
        os.system("cls")
        vida_inicial_pikachu = 125
        vida_inicial_bulbasaur = 100
        vida_pikachu = vida_inicial_pikachu
        vida_bulbasaur = vida_inicial_bulbasaur
        barras = 10

        print("\nEl combate comienza!!")

        barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
        print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                  " " * (barras - barras_de_vida_pikachu),
                                                  vida_pikachu, vida_inicial_pikachu))

        barras_de_vida_bulbasaur = int(vida_bulbasaur * barras / vida_inicial_bulbasaur)
        print("Bulbasaur:  [{}{}] ({}/{})".format("*" * barras_de_vida_bulbasaur,
                                                  " " * (barras - barras_de_vida_bulbasaur),
                                                  vida_bulbasaur, vida_inicial_bulbasaur))
        input("Presiona enter...\n")
        os.system("cls")

        while vida_pikachu > 0 and vida_bulbasaur > 0:

            print("\nEs el turno de Bulbasaur!!")

            ataque_bulbasaur = random.randint(1, 3)
            if ataque_bulbasaur == 1:
                print("Bulbasaur ataca con Latigo cepa!!\n")
                vida_pikachu -= 30
                print("El daño recibido fue -30!!")
            elif ataque_bulbasaur == 2:
                print("Bulbasaur ataca con Hoja afilada!!\n")
                vida_pikachu -= 25
                print("El daño recibido fue -25!!")
            elif ataque_bulbasaur == 3:
                print("Bulbasaur ataca con Rayo solar!!\n")
                vida_pikachu -= 20
                print("El daño recibido fue -20!!")

            if vida_pikachu < 0:
                vida_pikachu = 0
            elif vida_bulbasaur < 0:
                vida_bulbasaur = 0

            barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
            print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                      " " * (barras - barras_de_vida_pikachu),
                                                      vida_pikachu, vida_inicial_pikachu))

            barras_de_vida_bulbasaur = int(vida_bulbasaur * barras / vida_inicial_bulbasaur)
            print("Bulbasaur:  [{}{}] ({}/{})".format("*" * barras_de_vida_bulbasaur,
                                                      " " * (barras - barras_de_vida_bulbasaur),
                                                      vida_bulbasaur, vida_inicial_bulbasaur))
            input("\nPresione enter para continuar...\n")
            os.system("cls")

            if vida_pikachu > 0:

                print("\nEs el turno de pikachu!!")
                ataque_pikachu = None
                while ataque_pikachu != "q" and ataque_pikachu != "w" and ataque_pikachu != "e" \
                        and ataque_pikachu != "r":
                    ataque_pikachu = input("\nQue ataque deseas realizar? [q]Impactrueno, [w]Onda trueno, "
                                           "[e]Embestida, [r]Ataque rapido:")

                    if ataque_pikachu == "q":
                        print("pikachu ataca con impactrueno!!\n")
                        v = random.randint(35, 45)
                        vida_bulbasaur -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "w":
                        print("pikachu ataca con Onda trueno!!\n")
                        v = random.randint(25, 35)
                        vida_bulbasaur -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "e":
                        print("pikachu ataca con embestida!!\n")
                        v = random.randint(20, 30)
                        vida_bulbasaur -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "r":
                        print("pikachu ataca con ataque rapido!!\n")
                        vida_bulbasaur -= 20
                        print("El deño hecho fue -20!!")

                if vida_pikachu < 0:
                    vida_pikachu = 0
                elif vida_bulbasaur < 0:
                    vida_bulbasaur = 0

                barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
                print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                          " " * (barras - barras_de_vida_pikachu),
                                                          vida_pikachu, vida_inicial_pikachu))

                barras_de_vida_bulbasaur = int(vida_bulbasaur * barras / vida_inicial_bulbasaur)
                print("Bulbasaur:  [{}{}] ({}/{})".format("*" * barras_de_vida_bulbasaur,
                                                          " " * (barras - barras_de_vida_bulbasaur),
                                                          vida_bulbasaur, vida_inicial_bulbasaur))
                input("\nPresione enter para continuar...\n")
                os.system("cls")

        if vida_pikachu > vida_bulbasaur:
            print("Pikachu es el ganador!!")
            print("Pikachu a subido de nivel ahora tiene mas vida, daño, y aprendio un nuevo movimiento!!")
            end_game = False
            enemy += 1
            map_objects.pop(0)
            map_objects.append([24, 5])
            time.sleep(4)
        else:
            print("\nBulbasaur es el ganador!!")
            finish = False
            died = True
            time.sleep(2.5)
    elif enemy == 2:
        os.system("cls")
        vida_inicial_pikachu = 150
        vida_inicial_squirtle = 120
        vida_pikachu = vida_inicial_pikachu
        vida_squirtle = vida_inicial_squirtle
        barras = 10

        print("\nEl combate comienza!!")

        barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
        print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                  " " * (barras - barras_de_vida_pikachu),
                                                  vida_pikachu, vida_inicial_pikachu))

        barras_de_vida_squirtle = int(vida_squirtle * barras / vida_inicial_squirtle)
        print("Squirtle:   [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle,
                                                  " " * (barras - barras_de_vida_squirtle),
                                                  vida_squirtle, vida_inicial_squirtle))
        input("Presiona enter...\n")
        os.system("cls")

        while vida_pikachu > 0 and vida_squirtle > 0:

            print("\nEs el turno de Squirtle!!")

            ataque_squirtle = random.randint(1, 4)
            if ataque_squirtle == 1:
                print("Squirtle ataca con Pistola de agua!!\n")
                vida_pikachu -= 35
                print("El daño recibido fue -35!!")
            elif ataque_squirtle == 2:
                print("Squirtle ataca con Hidrobomba!!\n")
                vida_pikachu -= 30
                print("El daño recibido fue -30!!")
            elif ataque_squirtle == 3:
                print("Squirtle ataca con Burbuja!!\n")
                vida_pikachu -= 25
                print("El daño recibido fue -25!!")
            elif ataque_squirtle == 4:
                print("Squirtle ataca con Cabezazo!!\n")
                vida_pikachu -= 20
                print("El daño recibido fue -20!!")

            if vida_pikachu < 0:
                vida_pikachu = 0
            elif vida_squirtle < 0:
                vida_squirtle = 0

            barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
            print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                      " " * (barras - barras_de_vida_pikachu),
                                                      vida_pikachu, vida_inicial_pikachu))

            barras_de_vida_squirtle = int(vida_squirtle * barras / vida_inicial_squirtle)
            print("Squirtle:   [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle,
                                                      " " * (barras - barras_de_vida_squirtle),
                                                      vida_squirtle, vida_inicial_squirtle))
            input("\nPresione enter para continuar...\n")
            os.system("cls")

            if vida_pikachu > 0:

                print("\nEs el turno de pikachu!!")
                ataque_pikachu = None
                while ataque_pikachu != "q" and ataque_pikachu != "w" and ataque_pikachu != "e" \
                        and ataque_pikachu != "r" and ataque_pikachu != "t":
                    ataque_pikachu = input("\nQue ataque deseas realizar? [q]Impactrueno, [w]Onda trueno, "
                                           "[e]Embestida, [r]Ataque rapido, [t]Cola ferrea:")

                    if ataque_pikachu == "q":
                        print("pikachu ataca con impactrueno!!\n")
                        v = random.randint(40, 50)
                        vida_squirtle -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "w":
                        print("pikachu ataca con Onda trueno!!\n")
                        v = random.randint(30, 40)
                        vida_squirtle -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "e":
                        print("pikachu ataca con embestida!!\n")
                        v = random.randint(25, 35)
                        vida_squirtle -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "t":
                        print("pikachu ataca con cola ferrea!!\n")
                        v = random.randint(20, 30)
                        vida_squirtle -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "r":
                        print("pikachu ataca con ataque rapido!!\n")
                        vida_squirtle -= 25
                        print("El deño hecho fue -25!!")

                if vida_pikachu < 0:
                    vida_pikachu = 0
                elif vida_squirtle < 0:
                    vida_squirtle = 0

                barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
                print("Pikachu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                          " " * (barras - barras_de_vida_pikachu),
                                                          vida_pikachu, vida_inicial_pikachu))

                barras_de_vida_squirtle = int(vida_squirtle * barras / vida_inicial_squirtle)
                print("Squirtle:   [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle,
                                                          " " * (barras - barras_de_vida_squirtle),
                                                          vida_squirtle, vida_inicial_squirtle))
                input("\nPresione enter para continuar...\n")
                os.system("cls")

        if vida_pikachu > vida_squirtle:
            print("Pikachu es el ganador!!")
            print("Pikachu a evolucionado a Raichu, ahora tiene nuevas habilidades y mas vida!!")
            end_game = False
            enemy += 1
            map_objects.pop(0)
            map_objects.append([2, 7])
            time.sleep(4)
        else:
            print("\nSquirtle es el ganador!!")
            finish = False
            died = True
            time.sleep(2.5)
    elif enemy == 3:
        os.system("cls")
        vida_inicial_pikachu = 175
        vida_inicial_charizard = 140
        vida_pikachu = vida_inicial_pikachu
        vida_charizard = vida_inicial_charizard
        barras = 10

        print("\nEl combate comienza!!")

        barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
        print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                 " " * (barras - barras_de_vida_pikachu),
                                                 vida_pikachu, vida_inicial_pikachu))

        barras_de_vida_charizard = int(vida_charizard * barras / vida_inicial_charizard)
        print("Charizard: [{}{}] ({}/{})".format("*" * barras_de_vida_charizard,
                                                 " " * (barras - barras_de_vida_charizard),
                                                 vida_charizard, vida_inicial_charizard))
        input("Presiona enter...\n")
        os.system("cls")

        while vida_pikachu > 0 and vida_charizard > 0:

            print("\nEs el turno de Charizard!!")

            ataque_charizard = random.randint(1, 4)
            if ataque_charizard == 1:
                print("Charizard ataca con Lanzallamas!!\n")
                vida_pikachu -= 40
                print("El daño recibido fue -40!!")
            elif ataque_charizard == 2:
                print("Charizard ataca con Giro fuego!!\n")
                vida_pikachu -= 35
                print("El daño recibido fue -35!!")
            elif ataque_charizard == 3:
                print("Charizard ataca con Cola dragon!!\n")
                vida_pikachu -= 30
                print("El daño recibido fue -30!!")
            elif ataque_charizard == 4:
                print("Charizard ataca con Ataque ala!!\n")
                vida_pikachu -= 25
                print("El daño recibido fue -25!!")

            if vida_pikachu < 0:
                vida_pikachu = 0
            elif vida_charizard < 0:
                vida_charizard = 0

            barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
            print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                     " " * (barras - barras_de_vida_pikachu),
                                                     vida_pikachu, vida_inicial_pikachu))

            barras_de_vida_charizard = int(vida_charizard * barras / vida_inicial_charizard)
            print("Charizard: [{}{}] ({}/{})".format("*" * barras_de_vida_charizard,
                                                     " " * (barras - barras_de_vida_charizard),
                                                     vida_charizard, vida_inicial_charizard))
            input("\nPresione enter para continuar...\n")
            os.system("cls")

            if vida_pikachu > 0:

                print("\nEs el turno de raichu!!")
                ataque_pikachu = None
                while ataque_pikachu != "q" and ataque_pikachu != "w" and ataque_pikachu != "e" \
                        and ataque_pikachu != "r" and ataque_pikachu != "t":
                    ataque_pikachu = input("\nQue ataque deseas realizar? [q]Impactrueno, [w]Onda trueno, "
                                           "[e]Latigo, [r]Ataque rapido, [t]Rayo:")

                    if ataque_pikachu == "q":
                        print("Raichu ataca con impactrueno!!\n")
                        v = random.randint(45, 55)
                        vida_charizard -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "w":
                        print("Raichu ataca con Onda trueno!!\n")
                        v = random.randint(35, 45)
                        vida_charizard -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "e":
                        print("Raichu ataca con Latigo!!\n")
                        v = random.randint(30, 40)
                        vida_charizard -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "t":
                        print("Raichu ataca con cola Rayo!!\n")
                        v = random.randint(25, 35)
                        vida_charizard -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "r":
                        print("Raichu ataca con ataque rapido!!\n")
                        vida_charizard -= 30
                        print("El daño hecho fue -30!!")

                if vida_pikachu < 0:
                    vida_pikachu = 0
                elif vida_charizard < 0:
                    vida_charizard = 0

                barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
                print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                         " " * (barras - barras_de_vida_pikachu),
                                                         vida_pikachu, vida_inicial_pikachu))

                barras_de_vida_charizard = int(vida_charizard * barras / vida_inicial_charizard)
                print("Charizard: [{}{}] ({}/{})".format("*" * barras_de_vida_charizard,
                                                         " " * (barras - barras_de_vida_charizard),
                                                         vida_charizard, vida_inicial_charizard))
                input("\nPresione enter para continuar...\n")
                os.system("cls")

        if vida_pikachu > vida_charizard:
            print("Raichu es el ganador!!")
            print("Raichu a subido de nivel ahora tiene mas vida y daño!!")
            end_game = False
            enemy += 1
            map_objects.pop(0)
            map_objects.append([1, 10])
            time.sleep(4)
        else:
            print("\nCharizard es el ganador!!")
            finish = False
            died = True
            time.sleep(2.5)
    elif enemy == 4:
        os.system("cls")
        vida_inicial_pikachu = 200
        vida_inicial_venusaur = 160
        vida_pikachu = vida_inicial_pikachu
        vida_venusaur = vida_inicial_venusaur
        barras = 20

        print("\nEl combate comienza!!")

        barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
        print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                 " " * (barras - barras_de_vida_pikachu),
                                                 vida_pikachu, vida_inicial_pikachu))

        barras_de_vida_venusaur = int(vida_venusaur * barras / vida_inicial_venusaur)
        print("Venusaur:  [{}{}] ({}/{})".format("*" * barras_de_vida_venusaur,
                                                 " " * (barras - barras_de_vida_venusaur),
                                                 vida_venusaur, vida_inicial_venusaur))
        input("Presiona enter...\n")
        os.system("cls")

        while vida_pikachu > 0 and vida_venusaur > 0:

            print("\nEs el turno de Venusaur!!")

            ataque_venusaur = random.randint(1, 4)
            if ataque_venusaur == 1:
                print("Venusaur ataca con Danza petalo!!\n")
                vida_pikachu -= 45
                print("El daño recibido fue -45!!")
            elif ataque_venusaur == 2:
                print("Venusaur ataca con Placaje!!\n")
                vida_pikachu -= 40
                print("El daño recibido fue -40!!")
            elif ataque_venusaur == 3:
                print("Venusaur ataca con Latigo cepa!!\n")
                vida_pikachu -= 35
                print("El daño recibido fue -35!!")
            elif ataque_venusaur == 4:
                print("Venusaur ataca con Polvo veneno!!\n")
                vida_pikachu -= 30
                print("El daño recibido fue -30!!")

            if vida_pikachu < 0:
                vida_pikachu = 0
            elif vida_venusaur < 0:
                vida_venusaur = 0

            barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
            print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                     " " * (barras - barras_de_vida_pikachu),
                                                     vida_pikachu, vida_inicial_pikachu))

            barras_de_vida_venusaur = int(vida_venusaur * barras / vida_inicial_venusaur)
            print("Venusaur:  [{}{}] ({}/{})".format("*" * barras_de_vida_venusaur,
                                                     " " * (barras - barras_de_vida_venusaur),
                                                     vida_venusaur, vida_inicial_venusaur))
            input("\nPresione enter para continuar...\n")
            os.system("cls")

            if vida_pikachu > 0:

                print("\nEs el turno de raichu!!")
                ataque_pikachu = None
                while ataque_pikachu != "q" and ataque_pikachu != "w" and ataque_pikachu != "e" \
                        and ataque_pikachu != "r" and ataque_pikachu != "t":
                    ataque_pikachu = input("\nQue ataque deseas realizar? [q]Impactrueno, [w]Onda trueno, "
                                           "[e]Latigo, [r]Ataque rapido, [t]Rayo:")

                    if ataque_pikachu == "q":
                        print("Raichu ataca con impactrueno!!\n")
                        v = random.randint(50, 60)
                        vida_venusaur -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "w":
                        print("Raichu ataca con Onda trueno!!\n")
                        v = random.randint(40, 50)
                        vida_venusaur -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "e":
                        print("Raichu ataca con Latigo!!\n")
                        v = random.randint(35, 45)
                        vida_venusaur -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "t":
                        print("Raichu ataca con cola Rayo!!\n")
                        v = random.randint(30, 40)
                        vida_venusaur -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "r":
                        print("Raichu ataca con ataque rapido!!\n")
                        vida_venusaur -= 35
                        print("El daño hecho fue -35!!")

                if vida_pikachu < 0:
                    vida_pikachu = 0
                elif vida_venusaur < 0:
                    vida_venusaur = 0

                barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
                print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                         " " * (barras - barras_de_vida_pikachu),
                                                         vida_pikachu, vida_inicial_pikachu))

                barras_de_vida_venusaur = int(vida_venusaur * barras / vida_inicial_venusaur)
                print("Venusaur:  [{}{}] ({}/{})".format("*" * barras_de_vida_venusaur,
                                                         " " * (barras - barras_de_vida_venusaur),
                                                         vida_venusaur, vida_inicial_venusaur))
                input("\nPresione enter para continuar...\n")
                os.system("cls")

        if vida_pikachu > vida_venusaur:
            print("Raichu es el ganador!!")
            print("Raichu a subido de nivel ahora tiene mas vida y daño!!")
            end_game = False
            enemy += 1
            map_objects.pop(0)
            map_objects.append([25, 13])
            time.sleep(4)
        else:
            print("\nVenusaur es el ganador!!")
            finish = False
            died = True
            time.sleep(2.5)
    elif enemy == 5:
        os.system("cls")
        vida_inicial_pikachu = 225
        vida_inicial_blastoise = 180
        vida_pikachu = vida_inicial_pikachu
        vida_blastoise = vida_inicial_blastoise
        barras = 20

        print("\nEl combate comienza!!")

        barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
        print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                 " " * (barras - barras_de_vida_pikachu),
                                                 vida_pikachu, vida_inicial_pikachu))

        barras_de_vida_blastoise = int(vida_blastoise * barras / vida_inicial_blastoise)
        print("Blastoise: [{}{}] ({}/{})".format("*" * barras_de_vida_blastoise,
                                                 " " * (barras - barras_de_vida_blastoise),
                                                 vida_blastoise, vida_inicial_blastoise))
        input("Presiona enter...\n")
        os.system("cls")

        while vida_pikachu > 0 and vida_blastoise > 0:

            print("\nEs el turno de Blastoise!!")

            ataque_blastoise = random.randint(1, 4)
            if ataque_blastoise == 1:
                print("Blastoise ataca con Foco resplandor!!\n")
                vida_pikachu -= 50
                print("El daño recibido fue -50!!")
            elif ataque_blastoise == 2:
                print("Blastoise ataca con Pistola agua!!\n")
                vida_pikachu -= 45
                print("El daño recibido fue -45!!")
            elif ataque_blastoise == 3:
                print("Blastoise ataca con Placaje!!\n")
                vida_pikachu -= 40
                print("El daño recibido fue -40!!")
            elif ataque_blastoise == 4:
                print("Blastoise ataca con Burbuja!!\n")
                vida_pikachu -= 35
                print("El daño recibido fue -35!!")

            if vida_pikachu < 0:
                vida_pikachu = 0
            elif vida_blastoise < 0:
                vida_blastoise = 0

            barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
            print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                     " " * (barras - barras_de_vida_pikachu),
                                                     vida_pikachu, vida_inicial_pikachu))

            barras_de_vida_blastoise = int(vida_blastoise * barras / vida_inicial_blastoise)
            print("Blastoise: [{}{}] ({}/{})".format("*" * barras_de_vida_blastoise,
                                                     " " * (barras - barras_de_vida_blastoise),
                                                     vida_blastoise, vida_inicial_blastoise))
            input("\nPresione enter para continuar...\n")
            os.system("cls")

            if vida_pikachu > 0:

                print("\nEs el turno de raichu!!")
                ataque_pikachu = None
                while ataque_pikachu != "q" and ataque_pikachu != "w" and ataque_pikachu != "e" \
                        and ataque_pikachu != "r" and ataque_pikachu != "t":
                    ataque_pikachu = input("\nQue ataque deseas realizar? [q]Impactrueno, [w]Onda trueno, "
                                           "[e]Latigo, [r]Ataque rapido, [t]Rayo:")

                    if ataque_pikachu == "q":
                        print("Raichu ataca con impactrueno!!\n")
                        v = random.randint(60, 70)
                        vida_blastoise -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "w":
                        print("Raichu ataca con Onda trueno!!\n")
                        v = random.randint(50, 60)
                        vida_blastoise -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "e":
                        print("Raichu ataca con Latigo!!\n")
                        v = random.randint(45, 55)
                        vida_blastoise -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "t":
                        print("Raichu ataca con cola Rayo!!\n")
                        v = random.randint(40, 50)
                        vida_blastoise -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "r":
                        print("Raichu ataca con ataque rapido!!\n")
                        vida_blastoise -= 45
                        print("El daño hecho fue -45!!")

                if vida_pikachu < 0:
                    vida_pikachu = 0
                elif vida_blastoise < 0:
                    vida_blastoise = 0

                barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
                print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                         " " * (barras - barras_de_vida_pikachu),
                                                         vida_pikachu, vida_inicial_pikachu))

                barras_de_vida_blastoise = int(vida_blastoise * barras / vida_inicial_blastoise)
                print("Blastoise: [{}{}] ({}/{})".format("*" * barras_de_vida_blastoise,
                                                         " " * (barras - barras_de_vida_blastoise),
                                                         vida_blastoise, vida_inicial_blastoise))
                input("\nPresione enter para continuar...\n")
                os.system("cls")

        if vida_pikachu > vida_blastoise:
            print("Raichu es el ganador!!")
            print("Raichu a subido de nivel ahora tiene mas vida y daño!!")
            end_game = False
            enemy += 1
            map_objects.pop(0)
            map_objects.append([1, 16])
            time.sleep(4)
        else:
            print("\nBlastoise es el ganador!!")
            finish = False
            died = True
            time.sleep(2.5)
    elif enemy == 6:
        os.system("cls")
        vida_inicial_pikachu = 250
        vida_inicial_moltres = 200
        vida_pikachu = vida_inicial_pikachu
        vida_moltres = vida_inicial_moltres
        barras = 30

        print("\nEl combate comienza!!")

        barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
        print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                 " " * (barras - barras_de_vida_pikachu),
                                                 vida_pikachu, vida_inicial_pikachu))

        barras_de_vida_moltres = int(vida_moltres * barras / vida_inicial_moltres)
        print("Moltres:   [{}{}] ({}/{})".format("*" * barras_de_vida_moltres,
                                                 " " * (barras - barras_de_vida_moltres),
                                                 vida_moltres, vida_inicial_moltres))
        input("Presiona enter...\n")
        os.system("cls")

        while vida_pikachu > 0 and vida_moltres > 0:

            print("\nEs el turno de Moltres!!")

            ataque_moltres = random.randint(1, 4)
            if ataque_moltres == 1:
                print("Moltres ataca con Onda ignea!!\n")
                vida_pikachu -= 60
                print("El daño recibido fue -50!!")
            elif ataque_moltres == 2:
                print("Moltres ataca con Giro fuego!!\n")
                vida_pikachu -= 55
                print("El daño recibido fue -55!!")
            elif ataque_moltres == 3:
                print("Moltres ataca con Picotazo!!\n")
                vida_pikachu -= 50
                print("El daño recibido fue -50!!")
            elif ataque_moltres == 4:
                print("Moltres ataca con Vendaval!!\n")
                vida_pikachu -= 45
                print("El daño recibido fue -45!!")

            if vida_pikachu < 0:
                vida_pikachu = 0
            elif vida_moltres < 0:
                vida_moltres = 0

            barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
            print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                     " " * (barras - barras_de_vida_pikachu),
                                                     vida_pikachu, vida_inicial_pikachu))

            barras_de_vida_moltres = int(vida_moltres * barras / vida_inicial_moltres)
            print("Moltres:   [{}{}] ({}/{})".format("*" * barras_de_vida_moltres,
                                                     " " * (barras - barras_de_vida_moltres),
                                                     vida_moltres, vida_inicial_moltres))
            input("\nPresione enter para continuar...\n")
            os.system("cls")

            if vida_pikachu > 0:

                print("\nEs el turno de raichu!!")
                ataque_pikachu = None
                while ataque_pikachu != "q" and ataque_pikachu != "w" and ataque_pikachu != "e" \
                        and ataque_pikachu != "r" and ataque_pikachu != "t":
                    ataque_pikachu = input("\nQue ataque deseas realizar? [q]Impactrueno, [w]Onda trueno, "
                                           "[e]Latigo, [r]Ataque rapido, [t]Rayo:")

                    if ataque_pikachu == "q":
                        print("Raichu ataca con impactrueno!!\n")
                        v = random.randint(70, 80)
                        vida_moltres -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "w":
                        print("Raichu ataca con Onda trueno!!\n")
                        v = random.randint(60, 70)
                        vida_moltres -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "e":
                        print("Raichu ataca con Latigo!!\n")
                        v = random.randint(55, 65)
                        vida_moltres -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "t":
                        print("Raichu ataca con cola Rayo!!\n")
                        v = random.randint(50, 60)
                        vida_moltres -= v
                        print("El daño hecho fue {}!!".format(v))
                    elif ataque_pikachu == "r":
                        print("Raichu ataca con ataque rapido!!\n")
                        vida_moltres -= 55
                        print("El daño hecho fue -55!!")

                if vida_pikachu < 0:
                    vida_pikachu = 0
                elif vida_moltres < 0:
                    vida_moltres = 0

                barras_de_vida_pikachu = int(vida_pikachu * barras / vida_inicial_pikachu)
                print("Raichu:    [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu,
                                                         " " * (barras - barras_de_vida_pikachu),
                                                         vida_pikachu, vida_inicial_pikachu))

                barras_de_vida_moltres = int(vida_moltres * barras / vida_inicial_moltres)
                print("Moltres:   [{}{}] ({}/{})".format("*" * barras_de_vida_moltres,
                                                         " " * (barras - barras_de_vida_moltres),
                                                         vida_moltres, vida_inicial_moltres))
                input("\nPresione enter para continuar...\n")
                os.system("cls")

        if vida_pikachu > vida_moltres:
            print("Raichu es el ganador!!")
            print("Has completado esta arena!!")
            finish = False
            time.sleep(4)
        else:
            print("\nMoltres es el ganador!!")
            finish = False
            died = True
            time.sleep(2.5)
if died:
    os.system("cls")
    gameover = """\
    
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼\
    """
    print(gameover)
else:
    os.system("cls")
    gamecompleted = """\
    
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░█▀▀▀░█▀▀▀░░█▀▀░▀▀█░░█░░░░
    ░░░░█░▀█░█░▀█░░█▀▀░▄▀░░░▀░░░░
    ░░░░▀▀▀▀░▀▀▀▀░░▀▀▀░▀▀▀░░▀░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\
    """
    print(gamecompleted)
