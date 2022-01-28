import pygame
import random


class objects:
    def __init__(self, category,speed=0.25,sense=50):
        self.type = category
        if self.type == "a":
            self.speed = speed
            self.size = (10, 10)
            self.posn = self.set_posn()
            self.foodcount = 0
            self.colour = (255, 255, 255)
            self.foodfound = False
            self.targetlocation = self.set_posn()
            self.sense = sense
            self.energy = 50000
        else:
            self.colour = (255, 255, 0)
            self.posn = self.set_posn()
            self.size = (10, 10)

    def set_posn(self):
        x = random.randint(10, 490)
        y = random.randint(10, 490)
        posn = (x, y)
        return posn

    def search(self, list_of_food):
        x, y = self.posn
        avail_food = []
        for i in list_of_food:
            x1, y1 = i.posn
            if x1 - self.sense <= x <= x1 + self.sense and y1 - self.sense <= y <= y1 + self.sense:
                avail_food.append(i)
        if len(avail_food) > 1:
            target = self.at_min_dis(avail_food)
            t_x, t_y = target.posn
            self.foodlocation = t_x, t_y
            self.foodfound = True
            return t_x, t_y, True
        elif len(avail_food) == 1:
            f = avail_food[0]
            t_x, t_y = f.posn
            self.foodlocation = t_x, t_y
            self.foodfound = True
            return t_x, t_y, True
        else:
            t_x = None
            t_y = None
            x, y = self.posn
            x1, y1 = self.targetlocation
            if x1 - self.speed <= x <= x1 + self.speed and y1 - self.speed <= y <= y1 + self.speed:
                t_x = random.randint(10, 490)
                t_y = random.randint(10, 490)
                self.targetlocation = t_x, t_y
            return t_x, t_y, False

    def at_min_dis(self, a_list):

        x, y = self.posn
        sm = 0
        for i in a_list:
            x1, y1 = i.posn
            if sm == 0:

                sm = (x - x1) ** 2 + (y - y1) ** 2
                o = i
            else:
                if (x - x1) ** 2 + (y - y1) ** 2 < sm:
                    sm = (x - x1) ** 2 + (y - y1) ** 2
                    o = i
        return o

    def gen_change(self, a_list, handler=None):

        energy_gained = self.foodcount * 50000
        self.foodcount = 0
        if energy_gained < self.energy:
            a_list.remove(self)
            if handler != None:
                handler.write(str(self.speed) + "," + str(self.sense) + " ")
            del self
        elif energy_gained > self.energy:
            self.reproduce(a_list)
            self.energy = 0
            if handler != None:
                handler.write(str(self.speed) + "," + str(self.sense) + " ")
        else:
            self.energy = 0
            if handler != None:
                handler.write(str(self.speed) + "," + str(self.sense) + " ")

    def reproduce(self, a_list):
        o = objects("a")
        o.speed = self.speed
        o.sense = self.sense
        m_chance = random.randint(0, 4)
        if m_chance == 4:
            r_chance = random.randint(0, 1)
            if r_chance == 0:
                o.speed += 0.1
            else:
                o.sense += 5
        ##            print("mutation")
        a_list.append(o)

    def update(self, list_of_food, list_of_animals, master_list):
        if self.type == "a":
            x, y, b = self.search(list_of_food)
            if not b:
                self.move(self.targetlocation)
            elif b:
                self.move((x, y))
            size, s = self.size
            self.energy = (self.speed) ** 3 + self.sense * 2 + self.energy
        else:
            boo1 = self.is_eaten(list_of_animals)
            if boo1:
                list_of_food.remove(self)
                master_list.remove(self)
                del self

    def is_eaten(self, list_of_animals):
        x, y = self.posn
        for i in list_of_animals:
            x1, y1 = i.posn
            if x1 - 5 <= x <= x1 + 5 and y1 - 5 <= y <= y1 + 5:
                i.foodcount += 1
                return True
        return False

    def move(self, posn):
        x1, y1 = posn
        x, y = self.posn
        if x1 - x > 0:
            x += self.speed
        elif x1 - x < 0:
            x -= self.speed
        if y1 - y > 0:
            y += self.speed
        elif y1 - y < 0:
            y -= self.speed
        self.posn = (x, y)

    def draw(self, target_surface):
        x, y = self.posn
        w, h = self.size
        rect = (x, y, w, h)
        pygame.draw.rect(target_surface, self.colour, rect)

    def __del__(self):
        pass
