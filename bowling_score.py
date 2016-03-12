def bowling_score(rolls):
  "Compute the total score for a player's game of bowling."
  frame_count = {}
  count = 1
  i = 0
  j = 1
  score = 0

  while i < len(rolls) and count <= 11:
      if count <= 10:
          if rolls[i] != 10:                        
             frame_count[count] = [rolls[i]]
             frame_count[count].append(rolls[i+1])
             count = count + 1
             i = i + 2
          else:
             frame_count[count] = [rolls[i]]
             count = count + 1
             i = i + 1
      else:
          if sum(frame_count[10]) == 10:
              if len(frame_count[10]) == 1:
                  frame_count[count] = [rolls[i]]
                  frame_count[count].append(rolls[i+1])
                  count = count + 1
                  i = i + 1
              else:
                  if sum(frame_count[10]) == 10:
                     frame_count[count] = [rolls[i]]
                     count = count + 1
                     i = i + 1
          else:
             i = i+1
             count = count +1
 
  while j <= 10:
      if j in frame_count:
          if sum(frame_count[j]) == 10 and len(frame_count[j]) == 1:
              if len(frame_count[j+1]) == 1:
                  score = score + sum(frame_count[j]) + frame_count[j+1][0] + frame_count[j+2][0]
              else:                 
                  score = score + sum(frame_count[j]) + sum(frame_count[j+1])
             
          elif sum(frame_count[j]) == 10:
              score = score + sum(frame_count[j]) + frame_count[j+1][0]
 
          else:
              score = score + sum(frame_count[j])
      j = j + 1

  return score

    
#print bowling_score([9,1] * 10 + [9])            
print ( 0 == bowling_score( [0]*20 ) )
print ( 190 == bowling_score([9,1] * 10 + [9]) )
print ( 300 == bowling_score( [10]*12 ) )
print ( 11 == bowling_score([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 10,1,0]) )
print ( 12 == bowling_score([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 10, 1,0]) )




  
##  score = 0
##  frame_count = 0
##  i = 0
##  while frame_count < 10:
##       for i in range(2):
##
##          # bowling score for strikes
##          if rolls[i] == 10:
##              score = score + rolls[i] + rolls[i+1] + rolls[i+2]
##              frame_count = frame_count + 1
##          
##          # bowling score for spares
##          elif rolls[i]+rolls[i+1] == 10: 
##              score = score + rolls[i] + rolls[i+1] + rolls[i+2]
##              frame_count = frame_count + 1
##              i = i + 2
##          
##          else:
##              score = score + rolls[i]
##              frame_count = frame_count + 0.5
##              i = i + 1          
##  return score

##def bowling_score(rolls):
##  "Compute the total score for a player's game of bowling."
##
##  score = 0
##  i = 0
##  # 2 balls = 1 frame
##  # if 1st ball of any frame is 10, then no next ball in the frame
##  # append 0 next to 10 in any given sequence
##
##  for i in range(len(rolls)):
##      if rolls[i] == 10:
##          rolls[i+1:i+1] = ["x"]
##          
## 
##  while i < len(dice)-2:
##      
##      # bowling score for strikes
##
##      if rolls[i] == 10:
##         if rolls[i+3] != "x":
##             score = score + rolls[i] + rolls[i+2] + rolls[i+3]
##             i = i + 2
##         else:
##             score = score + rolls[i] + rolls[i+2] + rolls[i+4]
##             
##        
##      # bowling score for spares
##      
##      elif rolls[i] + rolls[i+1] == 10: 
##         score = score + rolls[i] + rolls[i+1] + rolls[i+2]
##
##      else:
##         score = score + rolls[i] + rolls[i+1]
##   
##  return score


