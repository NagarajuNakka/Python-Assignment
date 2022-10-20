class car:
    def __init__(self):
        self._colour = 0

    # using property decorator
    # a getter function
    @property
    def colour(self):
        print("getter method called")
        return self._colour

    # a setter function
    @colour.setter
    def colour(self, a):
        if a in ['red','purple']:
            raise ValueError("Sorry you colour is below eligibility criteria")
        print("setter method called")
        self._colour = a


mark = car()

mark.colour = 'green'
print(mark.colour)