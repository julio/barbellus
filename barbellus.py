class Barbellus:
    def __init__(self, plates_available, bar_weight):
        self.plates_available = plates_available
        self.bar_weight = bar_weight

    def select_plates(self, weight_to_lift, plates_used):
        min_plates = [0]*(weight_to_lift+1)

        for pounds in range(weight_to_lift-self.bar_weight+1):
            count_of_plates = pounds
            new_plate = 1
            for j in [c*2 for c in self.plates_available if c <= pounds]:
                if min_plates[pounds-j] + 1 < count_of_plates:
                    count_of_plates = min_plates[pounds-j]+1
                    new_plate = j
            min_plates[pounds] = count_of_plates
            plates_used[pounds] = new_plate

        print(plates_used)
        print(count_of_plates)

        return min_plates[weight_to_lift-self.bar_weight]

    def plates(self, plates_used, weight_to_lift):
        plates = []
        weight = weight_to_lift-self.bar_weight
        while weight > 0:
            this_plate = plates_used[weight]
            plates.append(int(this_plate/2))
            weight -= this_plate
        return plates

if __name__ == "__main__":
    weight_to_lift = 65
    bar_weight = 45
    plates_used = [0]*(weight_to_lift+1)

    plates_available = [1, 5, 10, 25, 35, 45]

    barbellus = Barbellus(plates_available, bar_weight)
    plates_to_use = barbellus.select_plates(weight_to_lift, plates_used)
    plates = barbellus.plates(plates_used, weight_to_lift)

    print("Lifting [", weight_to_lift, "lb ] requires", plates_to_use, "plates on each side: ", plates)
