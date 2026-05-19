import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2, 3, figsize=(8, 4))

# Splits range of 0 to 10 into 1000 intervals, so the graph looks smooth
nums = np.linspace(0, 10, 1000)

sin_raw = np.sin(nums)
cos_raw = np.cos(nums)
tan_raw = np.tan(nums)

# Detects the asymptodes of the graphs suc as in the tan and the reciprocal graphs
# By filtering out the values where magnitude is greater than 10, with np.nan which
# gets ignored during graph creation in matplotlib
tan_formatted = np.where(abs(tan_raw) > 10, np.nan, tan_raw)
sec_formatted = 1 / np.where(abs(cos_raw) < 0.1, np.nan, cos_raw)
csc_formatted = 1 / np.where(abs(sin_raw) < 0.1, np.nan, sin_raw)
cot_formatted = 1 / np.where(tan_formatted < 0.1, np.nan, tan_formatted)

graphs0 = {
    "labels": ["sin", "cos", "tan"],
    "values": [sin_raw, cos_raw, tan_formatted],
    "colors": ["red", "orange", "#BA8E23"],
}

graphs1 = {
    "labels": ["sec", "csc", "cot"],
    "values": [sec_formatted, csc_formatted, cot_formatted],
    "colors": ["#006400", "blue", "purple"],
}

# Plotting of sin, cos, tan graphs by looping through and applying attributes
for i in range(len(graphs0["labels"])):
    ax[0, i].plot(
        nums,
        graphs0["values"][i],
        label=f"{graphs0["labels"][i]}",
        color=graphs0["colors"][i],
    )
    ax[0, i].grid()
    ax[0, i].set_title(f"{graphs0["labels"][i]}(x) Graph", fontsize=12)
    ax[0, i].tick_params(axis="both", labelsize=10)

# Plotting of reciprocal graphs by looping through and applying attributes
for i in range(len(graphs1["labels"])):
    ax[1, i].plot(
        nums,
        graphs1["values"][i],
        label=f"{graphs1["labels"][i]}",
        color=graphs1["colors"][i],
    )
    ax[1, i].grid()
    ax[1, i].set_title(f"{graphs1["labels"][i]}(x) Graph", fontsize=12)
    ax[1, i].tick_params(axis="both", labelsize=10)

fig.suptitle("Trigonometry Graphs", fontsize=22)
fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(1, 1))


def display_graph(dpi=200, name="Trig Graphs.png", show=False):
    """
    Parameters:
        dpi: resolution of graph on print, default is 200
        name: name of png saved as, default is Trig Graphs.png
        show: whether to show the graph in thr console, default is False
    """
    plt.savefig(fname=name, dpi=dpi, bbox_inches="tight")
    if show:
        plt.show()
    plt.close(fig)

display_graph(name="custom name", show=False)
