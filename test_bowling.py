def bowling_score(rolls):
  "Compute the total score for a player's game of bowling."
  score = 0
  index = 0
  for frame in xrange(10):
      if rolls[index] == 10:
          score += 10 + rolls[index+1] + rolls[index+2]
          index += 1
      elif rolls[index] + rolls[index+1] == 10:
          score += 10 + rolls[index+2]
          index += 2
      else:
          score += rolls[index] + rolls[index+1]
          index += 2
  return score

print ( 0 == bowling_score( [0]*20 ) )
print ( 190 == bowling_score([9,1] * 10 + [9]) )
print ( 300 == bowling_score( [10]*12 ) )
print ( 11 == bowling_score([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 10,1,0]) )
print ( 12 == bowling_score([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 10, 1,0]) )
