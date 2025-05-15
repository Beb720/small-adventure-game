from random import choices
istrue = 0
isfalse = 0
noanswer = 0
for i in range(100):
    weights = 25, 75
    blue = bool(choices(range(2), weights=weights)[0])
    if blue == True:
        istrue += 1
    elif blue == False:
        isfalse += 1
    else:
        noanswer += 1

print(f"True: {istrue}, False: {isfalse}, No Answer: {noanswer}")