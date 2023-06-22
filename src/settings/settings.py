from pathlib import Path

print(Path(__file__))

SRC = f"{Path(__file__).parent.parent.parent}/src"
DATA = f"{SRC}/data"
INPUT_DATA = f"{DATA}/input"
OUTPUT_DATA = f"{DATA}/output"
GRAPHIC_RESOURCES = f"{SRC}/graphics"

DOMAINS = f"{INPUT_DATA}/domain.json"
DOMAIN_RENOVATION_DATES = f"{INPUT_DATA}/renovation-dates.json"
DELAYED_DOMAINS = f"{OUTPUT_DATA}/delayed-domains.txt"
TOAST_ICON = f"{SRC}/graphics/icon.ico"

API_URL = "https://rdap.registro.br/"