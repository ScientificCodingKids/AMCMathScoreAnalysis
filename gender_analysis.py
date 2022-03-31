from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from typing import Optional


def read_gender_file(prefix: str, cutoff: Optional[int] = 80) -> pd.DataFrame:
    fn =  __file__ + "/../data/" + "{prefix}_Contest Score Gender Report with Percentile.csv"

    df = pd.read_csv(fn, skiprows=[0, 1, 2])

    df = df[df["score"] > cutoff]
    df = df.sort_values(["score"], ascending=[True])

    return df


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pd.set_option("display.max_rows", 20)
    pd.set_option("display.max_columns", 100)
    pd.set_option("display.width", 1000)

    tests = ["2021Fall_AMC10A", "2021Fall_AMC10B", "2021_AMC10A", "2021_AMC10B"]

    dfs = [read_gender_file(t) for t in tests]
    #
    # df_2021f_10a = read_gender_file("2021Fall_AMC10A")
    # df_2021f_10b = read_gender_file("2021Fall_AMC10B")
    # df_2021_10a = read_gender_file("2021_AMC10A")
    # df_2021_10b = read_gender_file("2021_AMC10B")

    app = Dash("Girls in AMC")

    chs = []

    for t, gender_df in zip(tests, dfs):
        chs.append(html.H1(children=t))
        chs.append(dcc.Graph(id=t, figure=px.bar(gender_df, x="score", y="Females")))

    app.layout = html.Div(
        children=chs
    )

    app.run_server(debug=True)