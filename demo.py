from fpu import MultiplicativeDivider, CustomFloat

x = CustomFloat.from_float(2.1992187)
y = CustomFloat.from_float(1.5390625)

divider = MultiplicativeDivider(x, y, k=5)

print(
    'x:\t{x:f}\t{x}\n'
    'y:\t{y:f}\t{y}\n'
    'yk:\t{yk:f}\t{yk}\n'
    't:\t{t:f}\t{t}\n'
    'F1:\t{f1:f}\t{f1}\n'
    'F2:\t{f2:f}\t{f2}\n'
    'F3:\t{f3:f}\t{f3}\n'
    'F4:\t{f4:f}\t{f4}\n'
    'Result:\t{result:f}\t{result}'.format(x=divider.x,
                                           y=y,
                                           yk=divider.yk,
                                           t=divider.t,
                                           f1=divider.f1,
                                           f2=divider.f2,
                                           f3=divider.f3,
                                           f4=divider.f4,
                                           result=divider.divide())
)
