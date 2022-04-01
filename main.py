#import dash
import pandas as pd
from typing import Optional
import sys
import os


def read_test_files(prefix: str, school: Optional[str] = "Great Neck") -> pd.DataFrame:
    rolls = [
        "Achievement Roll",
        "Honor Roll",
        "Dist Honor Roll"
    ]

    dfs = []
    for roll in rolls:
        fn = os.path.dirname(__file__) + "/data/" + f"{prefix}_{roll}.csv"
        df = pd.read_csv(fn, skiprows=[0, 1, 2])

        df["Type"] = roll
        dfs.append(df)

    df = pd.concat(dfs)

    if school is not None:
        df = df[df["SchoolName"].str.contains(school)]

    df = df.drop_duplicates(subset=["score", "First_initial", "lastname", "grade"], keep="last")\
        .sort_values(by=["score", "grade"], ascending=[False, True])

    return df


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pd.set_option("display.max_rows", 20)
    pd.set_option("display.max_columns", 100)
    pd.set_option("display.width", 1000)

    df_2021f_10a = read_test_files("2021Fall_AMC10A", "Great Neck")
    df_2021f_10b = read_test_files("2021Fall_AMC10B", "Great Neck")
    df_2021_10a = read_test_files("2021_AMC10A", "Great Neck")
    df_2021_10b = read_test_files("2021_AMC10B", "Great Neck")

    df_2022_8 = read_test_files("2022_AMC8", "Great Neck")

    print(df_2022_8)
    print("done")
