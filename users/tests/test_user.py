from django.test import TestCase
from model_bakery import baker

from users.models import User


class TestUserModels(TestCase):
    """Test User Model"""

    def setUp(self) -> None:
        if isinstance(User, type):
            self.user = baker.make(User)

    def test_using_user(self):
        """Test function using baked model."""
        self.assertIsInstance(self.user, User)

    def test_models_fields(self):

        person = baker.make(
            User,
            username="smkang",
            first_name="Sungmuk",
            last_name="Kang",
            email="smkang@test.com",
        )
        assert person.username == "smkang"
        assert person.first_name == "Sungmuk"
        assert person.last_name == "Kang"
        assert person.email == "smkang@test.com"
