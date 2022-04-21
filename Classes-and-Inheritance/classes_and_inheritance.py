import csv
import os.path


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        allowable_file_extensions = ['.jpg',
                                     '.jpeg',
                                     '.png',
                                     '.gif']
        ext = os.path.splitext(self.photo_file_name)[1]  # get an extension of file
        try:
            if not ext in allowable_file_extensions:
                raise NameError("unacceptable extension")
        except NameError as err:
            print(err.args[0])
            return ''
        else:
            return ext



class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = "car"
        super().__init__(brand=brand,
                         photo_file_name=photo_file_name,
                         carrying=carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_lwh):
        self.car_type = "truck"
        super().__init__(brand=brand,
                         photo_file_name=photo_file_name,
                         carrying=carrying)
        self.body_lwh = body_lwh

        length = float(body_lwh.split("x")[0])
        self.body_length = length
        length = property()

        @length.setter
        def set_length(self, length):
            if not isinstance(length, float):
                self.body_length = 0
            else:
                self.body_length = length

        width = float(body_lwh.split("x")[1])
        self.body_width = width
        width = property()

        @width.setter
        def set_width(self, width):
            if not isinstance(width, float):
                self.body_width = 0
            else:
                self.body_width = width

        height = float(body_lwh.split("x")[2])
        self.body_height = height
        height = property()

        @height.setter
        def set_height(self, height):
            if not isinstance(height, float):
                self.body_height = 0
            else:
                self.body_height = height

    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height


class SpecMachine(CarBase):

    def __init__(self, brand, photo_file_name, carrying, extra):
        self.car_type = "spec_machine"
        super().__init__(brand=brand,
                         photo_file_name=photo_file_name,
                         carrying=carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # skip the title
        for row in reader:
            car_list.append(row)

    return car_list
