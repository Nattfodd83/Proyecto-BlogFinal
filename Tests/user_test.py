import email
import pytest

from django.test import TestCase
from app_accounts.views import UserCreationForm

def test_user_cration():
    user = UserCreationForm.objects.create_user(
        username="asddsa",
        email="asddsa@gmail.com",
        password1="1234567",
        password2="1234567"
    )
    assert user.username == "asddsa"