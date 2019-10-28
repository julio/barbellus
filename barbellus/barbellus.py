class Barbellus:
    def __init__(self, plates_available, weight_to_lift, bar_weight=45):
        self.plates_available = plates_available
        self.bar_weight = bar_weight
        self.weight_to_lift = weight_to_lift
        self.plates_used = [0]*(self.weight_to_lift+1)

    def build_rack(self):
        min_plates = [0]*(self.weight_to_lift+1)

        for pounds in range(self.weight_to_lift-self.bar_weight+1):
            count_of_plates = pounds
            new_plate = 1
            for j in [c*2 for c in self.plates_available if c <= pounds]:
                if min_plates[pounds-j] + 1 < count_of_plates:
                    count_of_plates = min_plates[pounds-j]+1
                    new_plate = j
            min_plates[pounds] = count_of_plates
            self.plates_used[pounds] = new_plate

        print(self.plates_used)
        print(count_of_plates)

        # return min_plates[self.weight_to_lift-self.bar_weight]
        return self

    def select_plates(self):
        plates = []
        weight = self.weight_to_lift-self.bar_weight
        while weight > 0:
            this_plate = self.plates_used[weight]
            plates.append(int(this_plate/2))
            weight -= this_plate
        return plates

if __name__ == "__main__":
    weight_to_lift = 65
    plates_available = [1, 5, 10, 25, 35, 45]

    barbellus = Barbellus(plates_available, weight_to_lift)
    plates = barbellus.build_rack().select_plates()

    print("Lifting", weight_to_lift, "lb requires", plates, "on each side")
