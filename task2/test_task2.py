import pytest
from solution import count_animals_by_letters, write_csv_file_for_counts_animals_by_letters
import os
from bs4 import BeautifulSoup


@pytest.fixture
def mock_page():
    file_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()
    soup = BeautifulSoup(html, "html.parser")
    return soup


def test_count_animals_by_letters(mock_page):
    pages = [mock_page]
    counts = count_animals_by_letters(pages)
    assert counts == {'А': 1, 'Б': 1, 'В': 1}


def test_write_csv_file_for_counts_animals_by_letters(tmp_path):
    counts = {'A': 10, 'B': 5}
    filename = tmp_path / "test.csv"
    write_csv_file_for_counts_animals_by_letters(counts, filename)

    assert os.path.exists(filename)
    with open(filename, 'r') as f:
        content = f.read()
        assert "Letter,Count" in content
        assert "A,10" in content
        assert "B,5" in content
