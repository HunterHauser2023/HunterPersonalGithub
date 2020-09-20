import math
import random 

chips = ["doritos"]
print(chips)
#append
chips.append("bbq")
print(chips)
#extend
#+=
chips.extend(["salt&vinegar", "cheetos"])
print(chips)
chips.sort()
print(chips)
#pop (remove by index)
chip_popped = chips.pop(0)
print("popped", chip_popped, "from", chips)
cool_ranch = ["c", "o", "ol", " ", "ranch"]
cool_ranch_string = "".join(cool_ranch)
print(cool_ranch_string)
#make a list from a string
cool_ranch_list_of_chars = list(cool_ranch_string)
print(cool_ranch_list_of_chars)
#another way to make a list from a string...seperate on delimiter
chip_string2= "cheetos, bbq, doritos" #delimeter,
chip_list2 = chip_string2.split(",")
print(chip_list2)

#TODO: list aliasing
#TODO: 2D list practice problem 

x = 5 + 12 // 5
print(x)