def better_than_average(class_points, your_points):
    klassenpunkte = class_points
    länge_des_arrays = len(klassenpunkte)
    durschnitt = 0
    int = 0

    while int < länge_des_arrays:
     durschnitt += klassenpunkte[int]
     
     print (durschnitt)
     int += 1
    
    durschnitt /= länge_des_arrays
    
    if durschnitt > your_points:
        return False
    
    else:
        return True