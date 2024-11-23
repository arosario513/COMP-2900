#!venv/bin/python3
'''Organizes the results and saves them as CSVs'''

import pandas as pd

sdf: pd.DataFrame = pd.read_csv("./selection_results.csv") \
    .pivot_table(index=["Input Size"], columns=["Case"], values=["Time"])

bdf: pd.DataFrame = pd.read_csv("./bubble_results.csv") \
    .pivot_table(index=["Input Size"], columns=["Case"], values=["Time"])


sdf.to_csv("selection_table.csv")
bdf.to_csv("bubble_table.csv")
