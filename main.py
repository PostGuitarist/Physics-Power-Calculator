#Mass = pounds / 2.2
def mass_solver():
	pounds = float(input("What is your weight (lbs)?\n"))
	mass = pounds / 2.2
	print(f"Your weight in kg is {mass}kg.")

#Force = mass * acceleration
def force_solver():
	mass = float(input("What is your mass (kg)?\n"))
	acceleration = float(input("What is the acceleration?\n"))
	force = mass * acceleration
	print(f"The force is {force} Newtons.")

#Work = force * distance
def work_solver():
	force = float(input("What is the force?\n"))
	distance = float(input("What is the distance (m)?\n"))
	work = force * distance
	print(f"The work done is {work} Joules.")

#Power = work / time
def power_solver():
	force = float(input("What is the force?\n"))
	distance = float(input("What is the distance (m)?\n"))
	time = float(input("What is the time (sec)?\n"))
	work = force * distance
	power = work / time
	print(f"The power output is {power}Watts.")

#760W = 1 hp
def watt_horsepower():
	power = float(input("What is the power (w)?\n"))
	hp = power / 760
	print(f"The output is {hp}Hp")

#User selection
print("1 - Mass Solver | 2 - Force Solver | 3 - Work Solver | 4 - Power Solver | 5 - Watts to Horsepower")
user_selection = int(input("Please type the number of what equation you want to use: "))
if user_selection == 1:
	mass_solver()
elif user_selection == 2:
	force_solver()
elif user_selection == 3:
	work_solver()
elif user_selection == 4:
	power_solver()
elif user_selection == 5:
	watt_horsepower()
else:
	print("Not an available selection.")
