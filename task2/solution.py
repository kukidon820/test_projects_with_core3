import requests
from bs4 import BeautifulSoup
import csv


def get_info_from_pages(url, pages):
    next_pages = []
    current_url = url
    while pages > 0:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, "html.parser")

        next_page_link = soup.find("a", string="Следующая страница")
        if next_page_link:
            next_pages.append(soup)
            current_url = "https://ru.wikipedia.org" + next_page_link["href"]
        else:
            break

        pages -= 1
    return next_pages


def count_animals_by_letters(pages):
    counts = {}

    for page in pages:
        links = page.select("div.mw-category-group ul li a")
        for link in links:
            title = link.text.strip()
            if title:
                first_letter = title[0].upper()
                if first_letter.isalpha():
                    counts[first_letter] = counts.get(first_letter, 0) + 1

    return counts


def write_csv_file_for_counts_animals_by_letters(counts, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Letter", "Count"])
        for letter, count in sorted(counts.items()):
            writer.writerow([letter, count])


def main():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    pages = 100
    pages = get_info_from_pages(url, pages=pages)

    letter_counts = count_animals_by_letters(pages)

    write_csv_file_for_counts_animals_by_letters(letter_counts, "count_animals_by_letters.csv")
    print(f"Результат записан в файл count_animals_by_letters.csv")


if __name__ == "__main__":
    main()
