def select_plates(available_plates, weight_to_lift, min_plates, plates_used):
    for pounds in range(weight_to_lift+1):
        count_of_plates = pounds
        new_plate = 1
        for j in [c for c in available_plates if c <= pounds]:
            if min_plates[pounds-j] + 1 < count_of_plates:
                count_of_plates = min_plates[pounds-j]+1
                new_plate = j
        min_plates[pounds] = count_of_plates
        plates_used[pounds] = new_plate
    return min_plates[weight_to_lift]

def print_plates(plates_used, weight_to_lift):
    plate = weight_to_lift
    while plate > 0:
        this_plate = plates_used[plate]
        print(this_plate)
        plate -= this_plate

if __name__ == "__main__":
    weight_to_lift = 320
    bar_weight = 45
    available_plates = [2*1, 2*5, 2*10, 2*25, 2*45]
    plates_used = [0]*(weight_to_lift-bar_weight+1)
    count_of_plates = [0]*(weight_to_lift-bar_weight+1)

    print("Lifting [", weight_to_lift, "lb ] requires")
    print(select_plates(available_plates, weight_to_lift-bar_weight, count_of_plates, plates_used), "plates")
    print_plates(plates_used, weight_to_lift-bar_weight)
