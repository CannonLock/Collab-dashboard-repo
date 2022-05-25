import pandas as pd
import json
import csv
from collections import defaultdict

# Points to csv snapshot of google sheets
CE_FILE_PATH = "./files/IGWN_sites-CE.csv"
INSTITUTES_PATH = "./files/IGWN_sites-Institutions.csv"


def parse_ces():
    """Parses cs csv into json objects by institution"""

    df = pd.read_csv(CE_FILE_PATH)

    def f(x):
        d = {}
        d["ce"] = list(x["COMPUTE ENTRY POINT (CE)"].unique())
        d["latitude"] = x["Latitude"].unique()[0]
        d["longitude"] = x["Longtitude"].unique()[0]
        d["hosted_ce"] = x["Hosted CE"].unique()[0]
        d["ce_location"] = x["CE location"].unique()[0]

        return pd.Series(d)

    df = df.groupby("Institute Site").apply(f)

    d = df.to_dict(orient="index")

    with open("data/ces.json", "w") as fp:
        json.dump(d, fp)


def parse_institutes():
    """Parse institutions"""  # TODO - This should be merged with the one above ( Update data )

    df = pd.read_csv(INSTITUTES_PATH, index_col="Member Institution")

    d = df.to_dict(orient="index")

    with open("data/institutions.json", "w") as fp:
        json.dump(d, fp)


def main():
    parse_institutes()
    parse_ces()


if "__main__" == __name__:
    main()