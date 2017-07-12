"""This module is used to make simple Bertrand games focused on airlines"""

import numpy as np
from matplotlib import pyplot as plt

class Airline:
    """Class for Airline. Getter and setter for capacity and price"""

    def __init__(self, capacity=0, price=0):
        self.capacity = capacity
        self.price = price

    def set_capacity(self, new_capacity):
        """Sets capacity"""
        self.capacity = new_capacity

    def set_price(self, new_price):
        """Sets price"""
        self.price = new_price

    def get_capacity(self):
        """Returns capacity"""
        return self.capacity

    def get_price(self):
        """Returns price"""
        return self.price

class DemandFunction:
    """Class that generates a demand function"""

    def __init__(self, N=100):
        self.no_consumers = N
        self.demand = np.ones(N) * 100

    def generate_uniform(self, min_price, max_price):
        """Generates uniformly distributed demand function"""
        self.demand = np.random.uniform(min_price, max_price, self.no_consumers)

    def generate_normal(self, mean, standard_deviation):
        """Generates normal distributed demand function"""
        self.demand = np.random.normal(mean, standard_deviation, self.no_consumers)

    def get_demand(self):
        """Returns demand function"""
        return self.demand

    def plot_demand(self):
        """Cummulates demand function and plots"""
   
        # Preparing
        max_price = int(np.max(self.demand))
        min_price = int(np.min(self.demand))

        cummulative_demand = np.zeros(max_price - min_price)

        # Aggregating
        i = 0
        for price in range(min_price, max_price):

            cummulative_demand[i] = sum(price <= bid for bid in self.demand)
            i += 1

        # Plotting
        plt.plot(cummulative_demand, range(min_price, max_price))
        plt.xlabel("Q")
        plt.ylabel("P")
        plt.title("Demand")
        plt.show()
    

if __name__ == "__main__":

    # Test

    BA = Airline()

    BA.set_capacity(100)

    print(BA.get_capacity())