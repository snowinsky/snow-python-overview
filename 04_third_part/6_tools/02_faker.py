from faker import Faker
fake = Faker()

print(fake.profile())

for idx in range(10):
    print(fake.safe_color_name())