#!/usr/bin/python

import argparse

def find_max_profit(prices):
  TotalProfits = []  # total amount of profit after comparing the two numbers
  for i in prices:
    priceIndex = prices.index(i)  # gets price with lowest index 
    for j in range(priceIndex + 1, len(prices)): # get next price value in the list
      priceDifference = prices[j] - prices[priceIndex] 
      TotalProfits.append(priceDifference) 
  return max(TotalProfits)


print(find_max_profit([1050, 270, 1540, 3800, 2]))
print(find_max_profit([20, 357, 80, 100, 20, 5]))

 



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

  