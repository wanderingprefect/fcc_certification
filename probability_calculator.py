import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        #adds each colour k ball v times to the self.contents list
        self.contents = []
        for k,v in kwargs.items():
            self.contents += [k]*int(v)
    def draw(self, toDraw):
        ballsDrawn = []
        #checks if there is enough balls available to draw
        if toDraw > len(self.contents):
            return(self.contents)
        #selects random balls from self.contents, adds them to ballsDrawn and removes them from self.contents
        for i in range(toDraw):
            ball_drawn = random.choice(self.contents)
            ballsDrawn += [ball_drawn]
            self.contents.remove(ball_drawn)
        return(ballsDrawn)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        #makes a copy of hat so it does not get comprimised when drawing balls
        hatcopy = copy.deepcopy(hat)
        #creates a list with the balls that the probability of drawing has to be calculated for
        expBalls = []
        for k,v in expected_balls.items():
            expBalls += [k]*int(v)
        #creates a list of drawn balls
        ballsDrawn = hatcopy.draw(num_balls_drawn)
        #compares expected balls to drawn balls and removes them if it's a match
        for ball in ballsDrawn:
            if ball in expBalls:
                expBalls.remove(ball)
        #if expBalls is empty, meaning all expected balls have been drawn. Add 1 to M
        if not expBalls:
            M += 1
    #returns probability
    return(M/num_experiments)