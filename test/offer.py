

class Offer_Page():
    def __init__(self):
        self.first_name = "Похуй"
        self.last_name = "Нахуй"


class Offer:
    def __init__(self):
        self.id = 15
        self.name = f"{self.id} {Offer_Page().first_name} {Offer_Page().last_name}"


offer = Offer()
print(offer.name)