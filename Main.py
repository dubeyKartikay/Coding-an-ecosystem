import pygame
from engine import objects
import os


def main(food, n_animal):
    file_name = create_working_file()
    data = open(file_name, "a")
    print("created")
    pygame.init()
    surface_sz = 500
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    main_surface.fill((0, 255, 0))
    list_of_food = []
    list_of_animals = []
    for i in range(food):
        o = objects("f")
        list_of_food.append(o)
    for i in range(n_animal):
        o = objects("a")
        list_of_animals.append(o)
    master_list = list_of_animals + list_of_food
    for i in master_list:
        i.draw(main_surface)
    frame_count = 0
    gen = 1
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break  # Leave game loop

        if frame_count % 1000 == 0:
            if frame_count == 250 * 1000:
                break

            gen += 1
            data.write("\n" + "-" + str(gen) + "-" + "\n")
            for i in list_of_animals:
                i.gen_change(list_of_animals, data)
            list_of_food = []
            master_list = []
            for i in range(food):
                o = objects("f")
                list_of_food.append(o)
            master_list = list_of_animals + list_of_food
        if len(list_of_animals) == 0:
            break
        main_surface = pygame.display.set_mode((surface_sz, surface_sz))
        main_surface.fill((0, 255, 0))
        for i in master_list:
            i.update(list_of_food, list_of_animals, master_list)
        for i in master_list:
            i.draw(main_surface)

        pygame.display.flip()
        frame_count += 1
    pygame.quit()

    data.write("\n" + "-" + str(gen) + "-" + str(len(list_of_animals)) + "-" + str(food) + "-" + "\n")
    data.close()


def sim_asap(to, food, n_animal):
    file_name = create_working_file()
    data = open(file_name, "a")
    print("created")
    surface_sz = 500
    list_of_food = []
    list_of_animals = []
    for i in range(food):
        o = objects("f")
        list_of_food.append(o)
    for i in range(n_animal):
        o = objects("a")
        list_of_animals.append(o)
    master_list = list_of_animals + list_of_food
    frame_count = 0
    gen = 1
    while True:
        if frame_count % 1000 == 0:
            if frame_count == to * 1000:
                break

            gen += 1
            data.write("\n" + "-" + str(gen) + "-" + "\n")
            for i in list_of_animals:
                i.gen_change(list_of_animals, data)
            list_of_food = []
            master_list = []
            for i in range(food):
                o = objects("f")
                list_of_food.append(o)
            master_list = list_of_animals + list_of_food
        if len(list_of_animals) == 0:
            break
        for i in master_list:
            i.update(list_of_food, list_of_animals, master_list)

        frame_count += 1
    data.close()
    print("done")
    return gen, list_of_animals, food


def sim_from(food, list_of_animals):
    pygame.init()
    surface_sz = 500
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    main_surface.fill((0, 255, 0))
    list_of_food = []
    for i in range(food):
        o = objects("f")
        list_of_food.append(o)
    master_list = list_of_animals + list_of_food
    gen = 1
    frame_count = 0
    for i in master_list:
        i.draw(main_surface)
    while True:

        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break  # Leave game loop

        if frame_count % 1000 == 0:
            if frame_count == 250 * 1000:
                pass
            gen += 1
            for i in list_of_animals:
                i.gen_change(list_of_animals)
            list_of_food = []
            master_list = []
            for i in range(food):
                o = objects("f")
                list_of_food.append(o)
            master_list = list_of_animals + list_of_food
        if len(list_of_animals) == 0:
            break
        main_surface = pygame.display.set_mode((surface_sz, surface_sz))
        main_surface.fill((0, 255, 0))
        for i in master_list:
            i.update(list_of_food, list_of_animals, master_list)
        for i in master_list:
            i.draw(main_surface)

        pygame.display.flip()
        frame_count += 1
    pygame.quit()


def generate_game(food, filename):
    with open(filename, "r") as file:
        c = file.readlines()
        a = c[-2].split(" ")
        a = a[:len(a) - 1]
    list_of_animals = []
    for i in a:
        attr = list(map(float, i.split(",")))
        o = objects("a", attr[0], attr[1])
        list_of_animals.append(o)
    sim_from(food, list_of_animals)




def create_working_file():
    no = len(os.listdir()) + 1
    with open("data" + str(no) + ".txt", "a") as file:
        pass
    return "data" + str(no) + ".txt"
