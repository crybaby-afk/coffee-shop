class Coffee:
    def __init__(self, name):
        self._name = self.validate_name(name)

    @staticmethod
    def validate_name(name):
        """Validates the coffee name."""
        if isinstance(name, str) and len(name) >= 3:
            return name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    @property
    def name(self):
        """Returns the coffee's name."""
        return self._name


coffee=Coffee("mocha")
coffee.name = ("sambusa")
print (coffee.name)