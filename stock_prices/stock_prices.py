#!/usr/bin/python

import argparse

def find_max_profit(prices):
  MainProfits = []  # total amount of profit after comparing the two numbers
  for i in prices:
    priceIndex = prices.index(i)  # retruns lowest index where (i) appears
    for j in range(priceIndex + 1, len(prices)):
      priceDifference = prices[j] - prices[priceIndex] # diff of smallest and largest price
      MainProfits.append(priceDifference) 
  return max(MainProfits)


print(find_max_profit([1050, 270, 1540, 3800, 2]))
print(find_max_profit([2000, 357, 80, 550, 20, 5]))

 



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

  