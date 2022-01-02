import os
import readchar
import random
map_width = 23
map_height = 15
pos_x = 0
pos_y = 1
my_position = [0, 0]
map_objects = []
num_of_map_objects = 11
tail_lenght = 0
tail = []
end_game = False
died = False


while not end_game:
    os.system("cls")
    while len(map_objects) < num_of_map_objects:
        new_position = [random.randint(0, map_width), random.randint(0, map_height)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    print("+" + "-" * map_width * 3 + "+")

    for coordinate_y in range(map_height):

        print("|", end="")

        for coordinate_x in range(map_width):

            char_to_draw = " "
            objects_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:

                if map_object[pos_x] == coordinate_x and map_object[pos_y] == coordinate_y:

                    char_to_draw = "*"
                    objects_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[pos_x] == coordinate_x and tail_piece[pos_y] == coordinate_y:

                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[pos_x] == coordinate_x and my_position[pos_y] == coordinate_y:

                char_to_draw = "@"

                if objects_in_cell:
                    map_objects.remove(objects_in_cell)
                    tail_lenght += 1
                if tail_in_cell:
                    end_game = True
                    died = True

            print(" {} ".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * map_width * 3 + "+")

    direction = readchar.readchar().decode()
    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[pos_y] -= 1
        my_position[pos_y] %= map_height
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[pos_y] += 1
        my_position[pos_y] %= map_height
    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[pos_x] -= 1
        my_position[pos_x] %= map_width
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[pos_x] += 1
        my_position[pos_x] %= map_width
    elif direction == "q":
        end_game = True

    os.system("cls")
if died:
    print("Has muerto!")
