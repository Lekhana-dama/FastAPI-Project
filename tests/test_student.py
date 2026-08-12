import pytest
from fastapi.testclient import TestClient

from main import app
from database import get_db
from tests.database import TestSessionLocal
from services.user_service import create_user


def override_get_db():
    db = TestSessionLocal()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def db():
    db = TestSessionLocal()

    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def test_user(db):
    return create_user(
        username="testuser",
        email="test@gmail.com",
        password="testpassword",
        role="user",
        db=db
    )