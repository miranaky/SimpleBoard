from collections import OrderedDict

import pytest

from users.serializers import UserSerializer

pytestmark = pytest.mark.django_db


class TestUserSerializer:
    def setup(self):
        self.serializer = UserSerializer

    @pytestmark
    def test_valid_serializer(self):
        _data = {
            "username": "test_user",
            "email": "test_user@test.com",
            "password": "P@$$w0rd321",
        }
        serializer = self.serializer(data=_data)
        assert serializer.is_valid()
        assert serializer.validated_data == OrderedDict(_data)
        assert serializer.data == {
            "username": "test_user",
            "email": "test_user@test.com",
        }
        assert serializer.errors == {}

    @pytestmark
    def test_invalid_serializer(self):
        _idata = {
            "username": "smkang",
            "email": "test_user@test.com",
        }
        serializer = self.serializer(data=_idata)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert serializer.data == {"username": "smkang", "email": "test_user@test.com"}
        assert serializer.errors == {"password": ["This field is required."]}

    @pytestmark
    def test_invalid_email(self):
        _idata = {
            "username": "test_user",
            "email": "test_user",
            "password": "P@$$w0rd321",
        }
        serializer = self.serializer(data=_idata)
        assert not serializer.is_valid()
        assert serializer.validated_data == {}
        assert serializer.errors == {"email": ["Enter a valid email address."]}
