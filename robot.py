import rg

class Robot:

    def attack(self):
        pass

    def converge(self):
        pass


    def friendly_locations(self, locations):
        return filter(locations, lambda x: x.get('robot_id'))

    def enemy_locations(self, locations):
        return filter(locations, lambda x: not x.get('robot_id'))

    def get_moves(self, locations):
        pass


    def act(self, game):
        all_locations = [x["location"] for x in game["robots"]]

        our_locations = self.friendly_locations(all_locations)

        avg_robot_x = 0
        avg_robot_y = 0
        n_robots = 0
        for x,y in our_locations:
            avg_robot_x += x
            avg_robot_y += y
            n_robots += 1
        avg_robot_x = avg_robot_x / n_robots
        avg_robot_y = avg_robot_y / n_robots
        my_x, my_y = self.location
        delta_x = avg_robot_x - my_x
        delta_y = avg_robot_y - my_y
        if abs(delta_x) > abs(delta_y):
            return ['move', (my_x + (1 if delta_x > 0 else -1) , my_y)]
        else:
            return ['move', (my_x, my_y+(1 if delta_y > 0 else -1))]
