from calendar import generate_month


def test_generate_month(capsys):
    generate_month(2025, 4)
    captured = capsys.readouterr()
    assert "Tuesday, April 01, 2025" in captured.out
