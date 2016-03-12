def solution(roman):
  """complete the solution by transforming the roman numeral into an integer"""
  result = 0
  roman_dic = {"M": 1000, "D": 500, "C" : 100, "L" : 50, "X" : 10, "V": 5, "I" : 1}
  for i in range(0, len(roman)):
      if i != len(roman)-1:
         if roman_dic[roman[i]] < roman_dic[roman[i+1]]:
             result = result - roman_dic[roman[i]]
         else:
             result = result + roman_dic[roman[i]]
      else:
          result = result + roman_dic[roman[i]]        
  return result

print solution("XLIX")
