import factory
from blog.models.topics import Topics
from faker import Faker

fake = Faker()

class TopicFactory(factory.Factory):
    class Meta:
        model = Topics

    title = factory.Faker('sentence',nb_words=4)
    type = factory.Iterator(['News','Opinion','Mail'])
    created_on = fake.date_of_birth(minimum_age=18, maximum_age=65)