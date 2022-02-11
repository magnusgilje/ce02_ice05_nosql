import math
import logging
# import matplotlib.pyplot as plt

class Hailstone:
    def __init__(self, n: int):
        if (n <=0):
            logging.error('perimeter request for invalid starting value')
            raise ValueError("Invalid value for starting value")
        self.n = n
        logging.debug('Hailstone sequence created')
        
    def plot(self):
        seq_list = []
        while self.n>1:
            seq_list.append(int(self.n))
            if self.n % 2 ==1:
                self.n = int(self.n*3+1)
            else:
                self.n = int(self.n/2)
        seq_list.append(1)
        # plt.plot(range(len(seq_list)),seq_list)
        return seq_list
        return plt.show(),seq_list,len(seq_list)