'''Create a function that returns the thickenss(in meters) of a piece of paper
    after folding it n number of times. The paper starts off with thickness of 
    0.5mm'''


def num_layers(n):
    return 0.0005 * 2 ** n
    
print(num_layers(1))
print(num_layers(4))
print(num_layers(21))