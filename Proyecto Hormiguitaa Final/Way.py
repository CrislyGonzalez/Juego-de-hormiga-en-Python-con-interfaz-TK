__author__ = 'Crisly'



class Way:

    """
    object the way keep the number of steps you had to take to reach the goal
    """

    def __init__(self, matrix):
        self.matrix = matrix
        self.steps = []


    def setMatrix(self, newMatrix):
        self.matrix = newMatrix

    def setSteps(self, newSteps):
        self.steps = newSteps

    def getMatrix(self):
        return self.matrix

    def getSteps(self):
        return self.steps

