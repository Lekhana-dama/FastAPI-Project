from unittest.mock import Mock

from services import student_service
from exceptions.custom_exceptions import StudentNotFoundException


def test_student_by_id():
    db = Mock()

    fake_student = Mock()
    fake_student.id = 1
    fake_student.name = "Lekhana"
    fake_student.branch = "CSD"
    fake_student.year = 4

    student_service.student_repository.get_student_by_id = Mock(
        return_value=fake_student
    )

    result = student_service.get_student_by_id(1, db)

    assert result == fake_student


def test_get_student_by_id_not_found():
    db = Mock()

    student_service.student_repository.get_student_by_id = Mock(
        return_value=None
    )

    try:
        student_service.get_student_by_id(1, db)
        assert False
    except StudentNotFoundException:
        assert True