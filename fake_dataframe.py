from faker import Faker
import pandas as pd
import random
fake = Faker('zh_TW')  # 'en_US', 'zh_TW'
def create_rows(num=1):
    output = [{"name":fake.name(),
               "address":fake.address(),
               "name":fake.name(),
               "email":fake.email(),
               "bs":fake.bs(),
               "address":fake.address(),
               "city":fake.city(),
               # "state":fake.state(),
               "date_time":fake.date_time(),
               "paragraph":fake.paragraph(),
               "Conrad":fake.catch_phrase(),
               "randomdata":random.randint(1000,2000)} for x in range(num)]
    return output

%%time
df = pd.DataFrame(create_rows(5000))
# Wall time: 5.55 s
