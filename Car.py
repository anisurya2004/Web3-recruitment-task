import math


class Car:
    def __init__(self, make, model, year, speed_x, speed_y, x=0, y=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = x
        self.y = y

    def accelerate(self, speed_increment):
        speed_increment_x = math.sin(math.atan((self.speed_x / self.speed_y))) * speed_increment
        speed_increment_y = math.cos(math.atan((self.speed_x / self.speed_y))) * speed_increment
        self.speed_x += speed_increment_x
        self.speed_y += speed_increment_y

    def brake(self, speed_decrement):
        speed_decrement_x = math.sin(math.atan((self.speed_x / self.speed_y))) * speed_decrement
        speed_decrement_y = math.cos(math.atan((self.speed_x / self.speed_y))) * speed_decrement
        self.speed_x -= speed_decrement_x
        self.speed_y -= speed_decrement_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def detect_collision(self, car2):
        if self.x == car2.x and self.y == car2.y:
            return True
        else:
            return False

    def time_to_collision(self, car2):
        time = 0
        speedrel_x = self.speed_x - car2.speed_x
        speedrel_y = self.speed_y - car2.speed_y
        xrel = self.x - car2.x
        yrel = self.y - car2.y
        is_Collide = False
        if xrel == 0 and yrel == 0:
            return 0
        elif yrel == 0 and xrel != 0:
            if speedrel_x / xrel < 0:
                is_Collide = True
                time = abs(xrel / speedrel_x)
        elif xrel == 0 and yrel != 0:
            if speedrel_y / yrel < 0:
                is_Collide = True
                time = abs(yrel / speedrel_y)
        elif speedrel_x / xrel < 0 and speedrel_y / yrel < 0:
            is_Collide = True
            time = abs(yrel / speedrel_y)
        else:
            is_Collide = False
            return -1
        return time
