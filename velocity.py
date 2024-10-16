mass = float(input("Enter the mass (in kg): "))  
force = float(input("Enter the force (in Newtons): ")) 
time = float(input("Enter the time (in seconds): ")) 
acceleration = force / mass  
velocity = acceleration * time  
print("The velocity is:", velocity, "m/s")  
