# pcost.py
#
# Exercise 1.27
def purchase(filename):
    infile = open(filename, 'rt')
    headers = next(infile).split(',')
    total_cost = 0
    for line in infile:
        row = line.split(',')
        shares= int(row[1])
        prices = float(row[2])
        total_cost += shares*prices
    print(total_cost)
