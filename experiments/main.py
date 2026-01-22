from extract import fetch_cards
from transform import parse_card
from load import save_to_csv

def main():
    records = []

    for page in range(1, 7):
        cards = fetch_cards(page)
        for card in cards:
            records.append(parse_card(card))

    save_to_csv(records, "beer_recipes.csv")


if __name__ == "__main__":
    main()
