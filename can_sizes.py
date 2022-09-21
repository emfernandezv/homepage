import math 

def main():

    #tab information
    name_can = ["#1 Picnic","#1 Tall","#2","#2.5","#3 Cylinder","#5","#6Z","#8Z short","#10","#211","#300","#303"]
    radius_can = [6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10]
    height_can = [10.16,11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27,11.11]
    cost_can = [0.28,0.43,0.45,0.61,0.86,0.83,0.22,0.26,1.53,0.34,0.38,0.42]
    x = 0
    index_e_max = 0
    index_s_best = 0
    index_e_best = 0
    
    while x < len(name_can):
        
        name = str(name_can[x])
        rad = float(radius_can[x])
        hei = float(height_can[x])
        cost = float(cost_can[x])
        
        volume = compute_volume(rad,hei)
        area = compute_surface_area(rad,hei)
        storage = storage_efficiency(volume,area)
        cost = compute_cost_efficiency(volume,cost)

        #evaluation the highest cost of efficiency
        if x == 0:
            cost_e_max = cost
        else:
            if cost_e_max <= cost:
                cost_e_max = cost
                index_e_max = name_can.index(name)

        #evaluation the best storage of efficiency
        if x == 0:
            storage_e_max = storage
        else:
            if storage_e_max > storage:
                storage_e_max = storage
                index_s_best = name_can.index(name)
        
        #evaluation the best cost of efficiency
        if x == 0:
            cost_e_best = cost
        else:
            if cost_e_best > cost:
                cost_e_best = cost
                index_e_best = name_can.index(name)

        print(f"{name_can[x]} \tStorage Efficiency: {round(storage,2)} \tCost Efficiency: {round(cost,2)}")
        
        x = x + 1
    
    print(f"The can with the highest cost of efficiency is: {name_can[index_e_max]}")
    print(f"The can with the best storage efficiency is: {name_can[index_s_best]}")
    print(f"The can with the best cost of efficiency is: {name_can[index_e_best]}")

def compute_volume(radius,height):
    return math.pi * (radius ** 2) * height

def compute_surface_area(radius,height):
    return 2 * math.pi * radius * (radius + height)

def storage_efficiency(volume,area):
    return volume / area

def compute_cost_efficiency(volume,cost):
    return volume / cost


main()