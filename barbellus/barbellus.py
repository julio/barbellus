from barbellus.exceptions import InvalidWeight

class Barbellus(object):
    def __init__(self, plates_available, total_weight_to_lift, bar_weight=45):
        if total_weight_to_lift < bar_weight:
            raise InvalidWeight('The bar already weighs more than {} pounds'.format(total_weight_to_lift))

        self.plates_available = plates_available
        self.bar_weight = bar_weight
        self.weight_to_lift = int((total_weight_to_lift-bar_weight) / 2) # weight on each side
        self.min_plates = [0]*(self.weight_to_lift+1)
        self.plates_used = {}

    def build_plate_rack(self):
        for pounds in range(self.weight_to_lift+1):
            count_of_plates = pounds
            new_plate = 1
            for weight in [plate for plate in self.plates_available if plate <= pounds]:
                if self.min_plates[pounds-weight] + 1 < count_of_plates:
                    count_of_plates = self.min_plates[pounds-weight]+1
                    new_plate = weight
            self.min_plates[pounds] = count_of_plates
            self.plates_used[pounds] = new_plate
        return self

    def select_plates(self):
        plates = []
        weight = self.weight_to_lift
        while weight > 0:
            this_plate = self.plates_used[weight]
            plates.append(int(this_plate))
            weight -= this_plate
        return sorted(plates, reverse=True)
