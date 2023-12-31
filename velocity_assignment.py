import math
print("welcome to the velocity calculator. please enter the following: ")
mass = float(input("mass (in kg): "))
gravity = float(input('gravity(in m/s^2, 9.8 for earth, 24 for jupiter): '))
time = float(input('time (in sounds): '))
denstity = float(input('density of the fluid (in kg/m^3, 1.3 for air, 1000 for water: '))
cross = float(input('cross sectional area (in m^2): '))
drag = float(input('Drag constant(0.5 for sphere, 1.1 for cylinder): '))
c = (1/2) *denstity * cross * drag
velocity = math.sqrt(mass * gravity / c) * (1 - math.exp(-math.srq(mass * gravity * c)/ mass * time))
print(f'the inner value of c is: {c:.3f}')
print(f'the velocity after 10.0 seconds is: {velocity:.3f} m/s')
print()
velocity_jupiter = math.sqrt(mass * 24 / c ) * (1 - math.exp(-math.sqrt(mass * gravity * c) / mass * time))
print(f'did you know due to the fact that the gravity in jupiter is 24 therefor the velocity is {velocity_jupiter:.3f} m/s!')
print()
radious_bowling = float (input('fun fact give me the radius of a bowling ball! '))
area__bowling = math.pi * radious_bowling ** 2
c2 = (1/2) * denstity * area__bowling * drag 
velocity_bowling = math.sqrt(mass * gravity / c2) * (1 - math.exp(-math.sqrt(mass * gravity * c2) / mass * time)) 
print(f'A bowling ball falls at the speed of:{velocity_bowling:.3f} m/s')
print()
velocity_terminal = math.sqrt(mass * gravity / c2)
print(f'its max velocity is: {velocity_terminal:.3f} m/s')
print()
