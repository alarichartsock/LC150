import re

with open("input.txt", 'r',encoding="utf-8") as file:
  f = file.read().split('\n')

  ret = 0

  for line in f:
    first = None
    last = None

    pattern = re.compile(r'(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine)')

    for num, word in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
      line = re.sub(word, word + str(num+1) + word, line)    

    for char in pattern.findall(line):
      if char in ['0','1','2','3','4','5','6','7','8','9']:
        if first:
          last = char
        else:
          first = char
          last = char

    ret += int(first + last)
  
  print(ret)
    
  
