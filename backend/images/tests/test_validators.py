import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.exceptions import ValidationError

from config import settings
from images.tests.test_models_image import image
from images.validators import validate_file_type


def test_valid_image(image):
    assert not validate_file_type(image)


def test_not_valid_image_with_correct_extension():
    image = SimpleUploadedFile(name='test_image.jpg', content=b'test not valid type')

    with pytest.raises(ValidationError) as excinfo:
        validate_file_type(image)
        print('*|'*20)
        print(excinfo.value.args[0])
        print('*|'*20)
    assert excinfo.value.args[0] == f'File type not supported. Use: *.{", *.".join(settings.IMAGES_TYPES)}.'

