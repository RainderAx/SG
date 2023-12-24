class Snake:
    def __init__(self, x, y, game_map):
        self.x = 0
        self.y = 0
        self.length = 1
        self.body = [(x, y)]
        self.map = game_map

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy

        if not self.map.is_collision(new_x, new_y):
            self.x = new_x
            self.y = new_y
            self.body.insert(0, (self.x, self.y))
            if len(self.body) > self.length:
                self.body.pop()

    def increase_length(self):
        self.length += 1

    def get_head_position(self):
        return self.x, self.y

    def get_body(self):
        return self.body
