#!venv/bin/python3
'''Organizes the results and graphs them'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

colors = {
    "asc": "green",
    "dec": "red",
    "rand": "blue",
}

sdf: pd.DataFrame = pd.read_csv("./selection_results.csv") \
    .set_index("Input Size") \
    .pivot_table(index=["Input Size"], columns=["Case"], values=["Time"])

bdf: pd.DataFrame = pd.read_csv("./bubble_results.csv") \
    .set_index("Input Size") \
    .pivot_table(index=["Input Size"], columns=["Case"], values=["Time"])


def forecast(df: pd.DataFrame, fp: list[int]) -> dict:
    '''
    Linear Forecasting
    Args:
        df (DataFrame): dataset used
        fp (list[int]): input sizes used
    Returns: dict
    '''
    fc = {}
    for i in df.columns:
        x = df.index.values.reshape(-1, 1)
        y = df[i].values

        model = make_pipeline(PolynomialFeatures(2), LinearRegression())
        model.fit(x, y)

        fx = np.array(fp).reshape(-1, 1)
        fy = model.predict(fx)

        fc[i] = (fx.flatten(), fy)
    return fc


fp: list[int] = list(range(100_000, 201_000, 10_000))

plt.style.use("seaborn-v0_8")

sdff = forecast(sdf, fp)
bdff = forecast(bdf, fp)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, sharey=True)
for i, j in zip(sdf.columns, ["green", "red", "blue"]):
    ax1.plot(sdf.index, sdf[i], color=j)
    fk = ("Time", i)

for fk, (fx, fy) in sdff.items():
    ax1.plot(fx, fy, ':', color=colors[fk[1]])

for i, j in zip(bdf.columns, ["green", "red", "blue"]):
    ax2.plot(bdf.index, bdf[i], color=j)
    fk = ("Time", i)

for fk, (fx, fy) in bdff.items():
    ax2.plot(fx, fy, ':', color=colors[fk[1]])

ax1.set_title("Selection Sort")
ax1.axvline(100_000, color="black", ls="--")
ax2.axvline(100_000, color="black", ls="--")
ax2.set_title("Bubble Sort")

fig.suptitle("Algorithm Analysis", fontsize=20)
fig.supxlabel("Input Size")
fig.supylabel("Time (Seconds)")
fig.tight_layout()


plt.xlim(10_000, 200_000)
plt.xticks(rotation=45)
plt.legend(["Best", "Worst", "Random", "Proj. Best",
           "Proj. Worst", "Proj. Random"])
plt.show()
