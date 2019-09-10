import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basicforms.settings')

import django
django.setup()

## FAKE POP SCRIPT

import random
from basicapp.models import User
from faker import Faker

fakegen = Faker()

def add_user(N=5):
    for entry in range(N):
        # create fake data for the entry

        fake_name = fakegen.name().split()
        fake_email = fakegen.email()

        # Create the new user entry
        user = User.objects.get_or_create(first_name=fake_name[0],
                                        last_name=fake_name[1],
                                        email=fake_email)

if __name__ == '__main__':
    print("populating script!")
    add_user(20)
    print("populating complete!")
