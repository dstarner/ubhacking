import os
from django.conf import settings

CLASS_STANDING_CHOICES = (
    (0, 'High School'),
    (1, 'Freshman'),
    (2, 'Sophomore'),
    (3, 'Junior'),
    (4, 'Senior'),
    (5, 'Super Senior'),
    (6, 'Other')
)

SHIRT_SIZE_CHOICES = (
    (0, 'Extra Small'),
    (1, 'Small'),
    (2, 'Medium'),
    (3, 'Large'),
    (4, 'Extra Large'),
    (5, 'XX Large')
)

STATUS_CHOICES = (
    (0, 'Pending'),
    (1, 'Denied'),
    (2, 'Accepted'),
    (3, 'Attending'),
    (4, 'Declined'),
    (5, 'Other')
)

def generate_school_names():

    with open(os.path.join(settings.BASE_DIR, 'data/schools.csv')) as schools_file:
        schools = [(index, school.strip().replace('"', '')) for index, school in enumerate(schools_file.readlines())]

    schools.append((-1, 'Other'))
    return schools

SCHOOL_NAME_CHOICES = generate_school_names()
