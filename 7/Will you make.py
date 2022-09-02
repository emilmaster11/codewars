###Mein Code

def zero_fuel(distance_to_pump, mpg, fuel_left):
    i_can_drive = mpg * fuel_left

    if i_can_drive == distance_to_pump or i_can_drive > distance_to_pump:
        return True
    
    else:
        return False


print(zero_fuel(100,25,2))


###Besserer Code
def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left