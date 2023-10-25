import pytest

from django.test import TestCase
from blog.models.topics import Topics
from blog.factories import TopicFactory


@pytest.fixture
def topics_made():
    return TopicFactory('nome base')

@pytest.mark.django_db
def test_create_topics(topics_made):
    assert topics_made.title == 'nome base'