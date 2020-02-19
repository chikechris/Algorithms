#!/usr/bin/python

import sys

def rock_paper_scissors(roundsRemaining):
 
  moves =["rock", "paper", "scissors"] 

  outcomes =[]



  def helperfun(roundsRemaining,  result=[]):
    #  base case
      if roundsRemaining == 0: # ---> there are no more plays 
          return outcomes.append(result)
    

      for move in moves:
      
        # print("move", move)
        helperfun(roundsRemaining - 1, result + [move])
        # print("recursive call in for:", helperfun)

  helperfun(roundsRemaining)
  
  # print(outcomes)
  return outcomes


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')