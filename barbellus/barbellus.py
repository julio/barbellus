from barbellus.exceptions import InvalidWeight

class Barbellus(object):
    def __init__(self, plates_available, weight_to_lift, bar_weight=45):
        if weight_to_lift < bar_weight:
            raise InvalidWeight('The bar already weighs more than {} pounds'.format(weight_to_lift))

        self.plates_available = plates_available       # plates available
        self.bar_weight = bar_weight                   # how much to take off the total
        self.weight_to_lift = weight_to_lift           # total weight being lifted
        self.plates_used = [0]*(self.weight_to_lift+1) # number of plates for each number of pounds
        self.min_plates = [0]*(self.weight_to_lift+1)

    def build_plate_rack(self):
        for pounds in range(self.weight_to_lift-self.bar_weight+1):
            count_of_plates = pounds
            new_plate = 1
            for j in [c*2 for c in self.plates_available if c <= pounds]:
                if self.min_plates[pounds-j] + 1 < count_of_plates:
                    count_of_plates = self.min_plates[pounds-j]+1
                    new_plate = j
            self.min_plates[pounds] = count_of_plates
            self.plates_used[pounds] = new_plate

        # return min_plates[self.weight_to_lift-self.bar_weight]
        return self

    def select_plates(self):
        plates = []
        weight = self.weight_to_lift-self.bar_weight
        while weight > 0:
            this_plate = self.plates_used[weight]
            plates.append(int(this_plate/2))
            weight -= this_plate
        return sorted(plates, reverse=True)

    def debug(self):
        for index, plate in enumerate(self.min_plates):
            print("For", index, "pounds, use", plate, "plates")
        # print(count_of_plates)
