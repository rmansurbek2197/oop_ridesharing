class Driver:
    def __init__(self, did, name):
        self.did = did
        self.name = name
        self.available = True


class Ride:
    def __init__(self, rid, user):
        self.rid = rid
        self.user = user
        self.status = "pending"


class RideSystem:
    def __init__(self):
        self.drivers = {}
        self.rides = {}

    def add_driver(self, driver):
        self.drivers[driver.did] = driver

    def request_ride(self, ride):
        for d in self.drivers.values():
            if d.available:
                d.available = False
                self.rides[ride.rid] = ride
                ride.status = "assigned"
                return d.did
        return None
