#!/usr/bin/env python
from faker import Faker
import pandas


class DataGen(object):

    fake = Faker('zh_TW')

    def genDF(self, num=1):

        fake = self.fake
        cols = ['name', 'email', 'bs', 'address', 'city',
                'date_time', 'paragraph', 'Conrad']
        data = [(fake.name(),
                 fake.email(),
                 fake.bs(),
                 fake.address(),
                 fake.city(),
                 fake.date_time(),
                 fake.paragraph(),
                 fake.catch_phrase()) for x in range(num)]
        return pandas.DataFrame(data=data, columns=cols)


if __name__ == '__main__':

    t1 = DataGen()
    df = t1.genDF(num=100)
    print(df.shape)
