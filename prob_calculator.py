import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball in balls:
            for j in range(balls[ball]):
                self.contents.append(ball)

    def set_contents(self, contents):
        self.contents = contents

    def draw(self, num_of_balls):
        removed_balls = []
        if num_of_balls >= len(self.contents):
            return self.contents
        else:
            for i in range(num_of_balls):
                r = random.randint(0, len(self.contents)-1)
                removed_balls.append(self.contents[r])
                self.contents.remove(self.contents[r])
        return removed_balls


def experiment(**params):
    M = 0
    d = params['num_balls_drawn']
    e = params['expected_balls']
    N = params['num_experiments']
    h = params['hat']
    duplicate = copy.copy(h.contents)
    exp = copy.copy(e)

    for i in range(N):
        drawn = h.draw(d)

        for ball in drawn:
            if ball in e.keys():
                e[ball] -= 1
            else:
                continue

        good = True
        for value in e.values():
            if value > 0:
                good = False

        if good:
            M += 1

        e = copy.copy(exp)
        h.set_contents(copy.copy(duplicate))
    return M / N


hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat,
                  expected_balls={"red": 2, "green": 1},
                  num_balls_drawn=4,
                  num_experiments=20000)
print(probability)