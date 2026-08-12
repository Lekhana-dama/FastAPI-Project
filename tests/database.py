from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import TEST_DATABASE_URL

from database_models.student_models import Base
from database_models.course_models import CourseDB
from database_models.enrollment_models import EnrollmentDB
from database_models.user_models import UserDB

from config import TEST_DATABASE_URL

test_engine = create_engine(TEST_DATABASE_URL)

TestSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine
)
Base.metadata.create_all(bind=test_engine)