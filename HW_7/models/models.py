from HW_7.models.model_abc import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Employee(Model):
    file = "employee.json"

    def __init__(self, name, email, plant_id):
        self.name = name
        self.email = email
        self.plant_id = plant_id
