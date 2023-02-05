import os

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from config.settings import BASE_DIR
from images.models import Image


@pytest.fixture()
def user(db, django_user_model):
    return django_user_model.objects.create_user(
        username="testuser",
        password="testPass123"
    )


@pytest.fixture()
def image_handler(db, user):
    image = Image.objects.create(
        author=user,
        url=SimpleUploadedFile(
            name='test_file.jpg',
            content=open(os.path.join('tests', 'test_image.jpg'), 'rb').read())
    )

    yield image
    os.remove(os.path.join(BASE_DIR, 'media', 'images', 'test_file.jpg'))


@pytest.mark.models
def test_image_creation(image_handler):
    assert isinstance(image_handler, Image)
    assert image_handler.author.username == 'testuser'
    assert image_handler.url.url == '/media/images/test_file.jpg'
    assert image_handler.name == 'test_file.jpg'
    assert str(image_handler) == 'test_file.jpg'


@pytest.mark.models
def test_image_fields(image_handler):
    assert [*vars(image_handler)] == ['_state', 'id', 'author_id', 'name', 'url', 'created_at', 'modified_at']
