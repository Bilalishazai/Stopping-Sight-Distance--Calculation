# Stopping Sight distance analysis

print("calculating stopping sight distance")

# 1. User Inputs

speed = float(input("Enter vehicle speed (km/h)"))
# we should also enter slope of the surface as a percentage 
Slope = float(input("enter the percentage "))

# 2. Convert speed from km/h to m/s (v = V / 3.6)
speed2 = speed / 3.6

# 3. AASHTO Standard Parameters
t = 2.5       # Perception-reaction time (2.5 seconds)
g = 9.81      # Acceleration due to gravity 

f = 0.35      #  friction (wet pavement standard)

# Convert grade percentage or slope to a decimal fraction
G = Slope/100

# 4. SSD Calculations


react_dist = speed2 * t
brak_dist = (speed2 ** 2) / (2 * g * (f + G))
total = react_dist+ brak_dist
# 5. Engineering Safety Evaluation (Using IF Conditions)
# If we face a danger, the warning will be added to this list
warnings = []

# Check for steep downgrades (Dangerous downhill conditions)
# 
if Slope <= -5:
    warnings.append(" downhill grade increases braking distance significantly!!!")

# Check for high speed risks
if speed > 100:
    warnings.append("  recommended to install (reduce speed) sign")

# Check if braking distance takes up too much of the stopping distance

if brak_dist > (total * 0.6):
    warnings.append(" Road friction  is critical. Consider anti-skid pavement.")

# 6. the result
# n means new line 
# f is used to create a format here f-string

print("\n Highway analysis ")
print(f"reaction distance: {react_dist} meters")
print(f"braking distance : {brak_dist} meters")
print(f"stopping sight distance  : {total} meters")


# Print safety engineering recommendations if any exist
if warnings:
    print("\n[ engineering recommendations]")
    for warn in warnings:
        print(warn)

    
 
import matplotlib.pyplot as plt
import numpy as np
# Numerical python
Speed = np.linspace(20, 140, 100)
# physical dynamic equations require SI units
speed2 = Speed/ 3.6

# To calculate reaction distance, we say r=v*t
reaction = speed2 * t
# to calculate braking distance, we say v**2/ 2g(friction+ Gravity)
Braking_distance = (speed2 ** 2) / (2 * g * (f + G))
Total_ssd= reaction+ Braking_distance

# to specify the size of the diagram
#width=10inch and height=6inch
plt.figure(figsize=(10, 6))

# xaxis=v_speeds_kph, yaxis=total
# Reaction-distance
# Braking distance 
plt.plot(Speed, Total_ssd, label='Total SSD (AASHTO)', color='red', linewidth=2)
plt.plot(Speed, Braking_distance, label='Braking Distance', color='blue', linestyle='--')
plt.plot(Speed, reaction, label='Reaction Distance', color='green', linestyle=':')

# draws a vertical line on the diagram and it shows the speed.
plt.axvline(x=Speed, color='black', linestyle='-.', alpha=0.7, label=f'Your Input Speed ({Speed} km/h)')

# adding title, xlabel and ylabel
plt.title(f'Stopping Sight Distance (SSD) Analysis at {Slope}% Grade', fontsize=14)
plt.xlabel('Vehicle Speed (km/h)', fontsize=12)
plt.ylabel('Distance (meters)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6) 
plt.legend(fontsize=11)  
# Legend explains the colors and lines
plt.show()
