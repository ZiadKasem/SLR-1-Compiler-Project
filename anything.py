inputString = ['1','b']
buffer = inputString + ['$']

print((int(inputString[0])))
print(inputString.__len__()-2)
inputString.pop(inputString.__len__() - 1)
inputString.pop(inputString.__len__() - 1)
inputString.append('hello')
print(inputString)
