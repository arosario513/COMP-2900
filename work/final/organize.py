#!venv/bin/python3
'''Organizes the results and graphs them'''

import pandas as pd
import matplotlib.pyplot as plt

sdf: pd.DataFrame = pd.read_csv("./selection_results.csv") \
    .set_index("Input Size") \
    .pivot_table(index=["Input Size"], columns=["Case"], values=["Time"])

bdf: pd.DataFrame = pd.read_csv("./bubble_results.csv") \
    .set_index("Input Size") \
    .pivot_table(index=["Input Size"], columns=["Case"], values=["Time"])


plt.style.use("seaborn-v0_8")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, sharey=True)
for i, j in zip(sdf.columns, ["green", "red", "blue"]):
    ax1.plot(sdf.index, sdf[i], color=j)

for i, j in zip(bdf.columns, ["green", "red", "blue"]):
    ax2.plot(bdf.index, bdf[i], color=j)


ax1.set_title("Selection Sort")
ax2.set_title("Bubble Sort")

fig.suptitle("Algorithm Analysis", fontsize=20)
fig.supxlabel("Input Size")
fig.supylabel("Time (Seconds)")
fig.tight_layout()

plt.xlim(10_000, 100_000)
plt.xticks(rotation=45)
plt.legend(["Best", "Worst", "Random"])
plt.show()
