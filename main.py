import dash
import pandas as pd
from typing import Optional


def read_test_files(prefix: str, school: Optional[str] = "Great Neck") -> pd.DataFrame:
    rolls = [
        "Achievement Roll",
        "Honor Roll",
        "Dist Honor Roll"
    ]

    dfs = []
    for roll in rolls:
        df = pd.read_csv(f"/home/nwind/PycharmProjects/AmcMathRanking/data/{prefix}_{roll}.csv",
                         skiprows=[0, 1, 2])
        df["Type"] = roll
        dfs.append(df)

    df = pd.concat(dfs).drop_duplicates(subset=["score", "First_initial", "lastname", "grade"], keep="last")\
        .sort_values(by=["score", "grade"], ascending=[False, True])

    if school is not None:
        df = df[df["SchoolName"].str.contains(school)]

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

    print("done")
    # gender analysis

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
