from multiplicative_divider import MultiplicativeDivider, CustomFloat

input_x = 2
input_y = 1.99

x = CustomFloat.from_float(input_x)
y = CustomFloat.from_float(input_y)

divider = MultiplicativeDivider(x, y, k=5)
result = divider.divide()

print(divider)
print('Divider result:\t{:f}'.format(result))
print('Real result:\t{:f}'.format(input_x / input_y))
