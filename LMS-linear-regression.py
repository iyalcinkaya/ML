def Readtxt(filename):

    with open(filename, "r") as f:
        data = f.readlines()

    columns = []

    for line in data:
        if line.startswith("#"): continue   # skip lines that start with "#"
        parts = line.split()                # split the line into n parts
        temp = []
        for part in parts:
            temp.append(float(part))
        columns.append(temp)
    
    return columns


class LinearRegression:

    def __init__(self, training_set, alpha):
        self.training_set = training_set
        self.numWeights = len(training_set[0])
        self.weights = [0] * self.numWeights
        self.alpha = alpha
    
    def step(self):
        for i in range(len(training_set)):
            x = training_set[i][:-1]
            y = training_set[i][-1]
            y_hat = self.predict(x)
            error = y - y_hat
            for j in range(self.numWeights):
                self.weights[j] += self.alpha * error * x[j]

alpha = 0.1 # learning rate

training_set = Readtxt("area-room-price.txt")



