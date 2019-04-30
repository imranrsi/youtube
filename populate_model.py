import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dhaka.settings')
import django
django.setup()



#Fake pop script
import random
from faker import Faker
from google.models import Topic,Webpage,AccessRecord

fakegen= Faker()

topics=['Search','Social','Marketplace','Games','News']

def add_topic():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
#
    return t

def populate(n=5):          #5 for randomly check
        for entry in range(n):
            top=add_topic()
            fake_name=fakegen.company()
            fake_url=fakegen.url()
            fake_date=fakegen.date()

            webp=Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

            acc_rec=AccessRecord.objects.get_or_create(name=webp,date=fake_date)[0]


if __name__=='__main__':
    print("populating script !")

    populate(50)      # 50 for dandomly check
    print("populate complete !")
