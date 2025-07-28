import pytest
from password_checker import check_character_types

def test_strong_password(capsys):
    check_character_types("StrongP@ss1")
    captured = capsys.readouterr()
    assert "Score: 4/4" in captured.out
    assert "Password strength: Strong" in captured.out

def test_missing_uppercase(capsys):
    check_character_types("weakp@ss1")
    captured = capsys.readouterr()
    assert "Score: 3/4" in captured.out
    assert "Include at least one uppercase letter." in captured.out

def test_very_weak_password(capsys):
    check_character_types("12345678")
    captured = capsys.readouterr()
    assert "Score: 1/4" in captured.out
    assert "Password strength: Weak" in captured.out