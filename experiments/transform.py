import re

NP_RE = re.compile(r"НП:\s*([\d.]+)\s*\(([\d,]+)°P\)")
ABV_RE = re.compile(r"ABV:\s*([\d,]+)")
IBU_RE = re.compile(r"IBU:\s*(\d+)")

def parse_card(card) -> dict:
    data = {"category": card.select_one("h5.card-title").text.strip(),
            "style": card.select_one("small.text-muted").text.strip(),
            "name": card.select_one("p.card-title strong").text.strip(), "og_sg": None, "og_plato": None, "abv": None,
            "ibu": None}

    for small in card.select("small.d-block"):
        text = small.text.strip()

        if m := NP_RE.search(text):
            data["og_sg"] = float(m.group(1))
            data["og_plato"] = float(m.group(2).replace(",", "."))

        if m := ABV_RE.search(text):
            data["abv"] = float(m.group(1).replace(",", "."))

        if m := IBU_RE.search(text):
            data["ibu"] = int(m.group(1))

    return data
