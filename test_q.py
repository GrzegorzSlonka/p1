import unittest
import time
import csv


def check_time(f):
    def meas(*args, **kwargs):
        start = time.time()
        c = f(*args, **kwargs)
        end = time.time()
        print()
        print("We've found a car for you in", round(end - start, 7), "s")
        return c
    return meas


@check_time
def get_data(av=None):
    with open('cars.csv', 'r') as data:
        rdr = csv.DictReader(data, delimiter=';')
        if av is not None:
            cars = [r for r in rdr if r['available'] == 'yes']
        else:
            cars = [r for r in rdr]
    return sorted(cars, key=lambda d: float(d['price']))[:3]


class GetDataTest(unittest.TestCase):
    def test_data_retr(self):
        self.car_lst = get_data()
        assert len(self.car_lst) > 0


if __name__ == '__main__':
    unittest.main()
