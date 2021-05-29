import json


class vehicle_list(object):
    """
    A list of vehicles owned
    """
    def __init__(self, list_name=None, owner=None, email=None):
        self.list_name = list_name
        self.owner = owner
        self.vehicleList = []
        self.vehicledictList = []
        self.email = email

    def __str__(self):
        return("List Name : {}, Owner : {} \n Vehicles {}".format(self.list_name, self.owner, str(self.vehicleList)))

class vehicle(object):
    """
    A base class for a type of vehicle.
    """
    def __init__(self, registration=None, vehicle_type=None, model=None, manufacturer=None):
        self.registration = registration
        self.vehicle_type = vehicle_type
        self.model = model
        self.manufacturer = manufacturer
        self.full_name = "{} {}".format(self.manufacturer, self.model)

    def __str__(self):
        return "Registration: {}\n\tType: {}\n\tModel: {}\n\tManufacturer: {}\n".format(
            self.registration, self.vehicle_type,self.model, self.manufacturer)


class dailycar(vehicle):
    """
    Daily vehicles used for general activities.
    """
    def __init__(self, registration=None, vehicle_type="Sports Car", model=None, manufacturer=None):
        super().__init__(registration, vehicle_type, model, manufacturer)
        self.vehicle_type = vehicle_type
        self.practicality = "tbc"

    def __str__(self):
        return "Registration: {}\n\tType: {}\n\tModel: {}\n\tManufacturer: {}\n\t\tPracticality: {}".format(
            self.registration, self.vehicle_type,self.model, self.manufacturer, self.practicality)


class sportscar(vehicle):
    """
    A sports car class
    """
    def __init__(self, registration=None, vehicle_type="Sports Car", model=None, manufacturer=None):
        super().__init__(registration, vehicle_type, model, manufacturer)
        self.vehicle_type = vehicle_type
        self.fun_factor = self.calculate_fun()

    def calculate_fun(self):
        fun = 50
        return fun

    def __str__(self):
        return "Registration: {}\n\tType: {}\n\tModel: {}\n\tManufacturer: {}\n\t\tFun Factor {}\n".format(
            self.registration, self.vehicle_type,self.model, self.manufacturer, self.fun_factor)


def main():
    carRegistry = {}
    myCars = vehicle_list(list_name="Rodman Household", owner="Mark Rodman", email="mark@mrodman.com")
    myCars.vehicleList.append(sportscar(
        registration="YXP 134R",
        model="Seven 620R S3",
        manufacturer="Caterham"))

    myCars.vehicleList.append(vehicle(
        registration="MX19 43C",
        model="Seven 420R S3",
        manufacturer="Caterham"))

    myCars.vehicleList.append(dailycar(registration="unknown", model="V90 Cross Country", manufacturer="Volvo"))

    for car in myCars.vehicleList:
        dict = (car.__dict__)
        myCars.vehicledictList.append(dict)

    carRegContainer = {}
    carRegistry = []
    carRegContainer[myCars.list_name] = {
        'List Name': myCars.list_name,
        'List Owner': myCars.owner,
        'Vehicle Count': len(myCars.vehicledictList),
        'Registry': myCars.vehicledictList
    }
    carRegistry.append(carRegContainer)

    Registry = {}
    Registry['Vehicle Registry'] = carRegistry
    print(json.dumps(Registry, indent=4))
    return



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
