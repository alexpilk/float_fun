from fpu import MultiplicativeDivider

x = 2.19921875
y = 1.5390625

normal_result = x / y
fpu_result = MultiplicativeDivider(x, y).divide()
print(normal_result)
print(fpu_result)
