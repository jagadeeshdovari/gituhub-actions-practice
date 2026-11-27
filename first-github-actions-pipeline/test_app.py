
import pytest
from app import StudentManagement

def test_add_student():
    system = StudentManagement()

    student = system.add_student("Rahul", 85)

    assert student["name"] == "Rahul"
    assert student["marks"] == 85

def test_get_students():
    system = StudentManagement()

    system.add_student("Rahul", 85)

    assert len(system.get_students()) == 1

def test_calculate_grade():
    system = StudentManagement()

    assert system.calculate_grade(95) == "A"
    assert system.calculate_grade(80) == "B"
    assert system.calculate_grade(60) == "C"
    assert system.calculate_grade(30) == "Fail"

def test_invalid_marks():
    system = StudentManagement()

    with pytest.raises(ValueError):
        system.add_student("Rahul", 150)

def test_empty_name():
    system = StudentManagement()

    with pytest.raises(ValueError):
        system.add_student("", 80)
