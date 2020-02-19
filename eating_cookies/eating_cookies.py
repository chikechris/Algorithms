#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(num_cookies, cache={}):
  if num_cookies in cache:
    return cache[num_cookies]
  if num_cookies == 0:  # base case
    value = 1
  elif num_cookies > 0:
    print('num of cookies: ', num_cookies)
    value = eating_cookies(
        num_cookies - 1) + eating_cookies(num_cookies-2) + eating_cookies(num_cookies-3)
  elif num_cookies < 0:
    value = 0
  cache[num_cookies] = value
  return value


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
