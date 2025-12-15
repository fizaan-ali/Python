#int, float, complex
num1 = 2 + 3j
print(num1)
num2 = complex(2,5) # 2 is real part 3 is imaginary part
print(num2.real," ",  num2.imag) # returned as floats
print(type(num2))



print(abs(-5.5)) # absolute value
print(round(5.5)); print(round(5.49, 1)) # first is 6 second is 5 

#ENUMS: -> used to define fixed constatnt literals!
from enum import Enum
class Status(Enum):
    ACTIVE = 1
    INACTIVE = 0

print(Status.ACTIVE)
print(Status.INACTIVE.value)
print(Status['ACTIVE'].value)
print(Status['INACTIVE'])