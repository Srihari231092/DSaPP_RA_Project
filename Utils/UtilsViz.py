"""
@author: Srihari
@date: 12/10/2018
@desc: Contains utility functions for visualisation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Define some useful functions here
def print_df_cols(df):
    print("Columns : ")
    for c in df.columns:
        print("\t", c, "  -->  ", df[c].dtype)
    print()


def plot_corr_heatmap(corrmat, annotate=False, annot_size=15):
    # plt.imshow(xcorr, cmap='hot')
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corrmat, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    cutsomcmap = sns.diverging_palette(250, 0, as_cmap=True)
    a4_dims = (11.7, 8.27)
    fig, ax = plt.subplots(figsize=a4_dims)
    corrheatmap = \
        sns.heatmap(ax=ax, data=corrmat, mask=mask, annot=annotate,
                    linewidths=0.5, cmap=cutsomcmap, annot_kws={"size": annot_size})
    plt.show()


def plot_pie(data, col_name, ax):
    col_cnt = data[col_name].value_counts()
    g = col_cnt.plot.pie(startangle=90, autopct='%.2f', ax=ax)


def plot_bar_timegraph(x, y, data, ax, highlight_max_min=False,
                       point_plot=True, annot=True,
                       title="", xlabel="", ylabel=""):
    if highlight_max_min:
        clrs = []
        for v in data[y].values:
            if v < data[y].max():
                if v > data[y].min():
                    clrs.append('lightblue')
                else:
                    clrs.append('darksalmon')
            else:
                clrs.append('lightgreen')
        g1 = sns.barplot(x=x, y=y, data=data, ax=ax, palette=clrs)
    else:
        g1 = sns.barplot(x=x, y=y, data=data, ax=ax, color="lightblue")
    if point_plot:
        g1 = sns.pointplot(x=x, y=y, data=data, ax=ax, color="darkblue")
    if annot:
        # Add labels to the plot
        style = dict(size=12, color='darkblue')
        s1 = np.round(data[y].pct_change().values, 2)
        s1[0] = 0
        for idx, row in data.iterrows():
            rx, ry = row[x], row[y]
            ax.text(idx*0.99, ry, str(s1[idx]), **style, va="bottom", ha='right')
    g1.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.set_ylim([0, data[y].max() * 1.2])
    ax.legend(handles=ax.lines[::len(data) + 1], labels=[y, y + " % change"])


def plot_box_timegraph(x, y, data, agg_rule, ax, point_plot=True, annot=False,
                       title="", xlabel="", ylabel=""):
    # Get the median value at each year
    agg_data = data[[y, x]].groupby(by=[x], as_index=False).agg(agg_rule)
    g = sns.boxplot(x=x, y=y, data=data[[y, x]], ax=ax)
    if point_plot:
        g = sns.pointplot(x=x, y=y, data=agg_data, ax=ax, color="k")
    if annot:
        # Add labels to the plot
        style = dict(size=12, color='darkblue')
        s1 = np.round(agg_data[y].values, 2)
        for idx, row in agg_data.iterrows():
            rx, ry = row[x], row[y]
            ax.text(idx, ry, str(s1[idx]), **style, va="bottom", ha='center')

    g.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.set_ylim([0, data[y].max() * 1.2])
    ax.legend(handles=ax.lines[::len(data)], labels=[y + " " + agg_rule])


def plot_bubblehist(x, y, s, data, show_max_min=True, title="", xlabel="", ylabel="", ax=None):
    if ax is None:
        fig_size = (16, 9)
        f, ax = plt.subplots(1, 1, figsize=fig_size)
    else:
        fig_size = ax.figure.get_size_inches()
    bubble_scale = 1 - min(fig_size) / max(fig_size)
    g = sns.scatterplot(x=data[x].values,
                        y=data[y].values,
                        s=data[s] * bubble_scale,
                        alpha=0.4, ax=ax)
    if show_max_min:
        max_x_coords, max_y_coords, max_s_val = [], [], []
        min_x_coords, min_y_coords, min_s_val = [], [], []
        for x1 in data[x].unique():
            for y1 in data[y].unique():
                val = data[(data[x] == x1) & (data[y] == y1)][s].values
                if val < data[data[x] == x1][s].max():
                    if val > data[data[x] == x1][s].min():
                        continue
                    else:
                        sval = data[(data["year"] == x1) & (data[y] == y1)][s].values
                        min_x_coords.append(x1)
                        min_y_coords.append(y1)
                        min_s_val.append(sval * bubble_scale)
                else:
                    sval = data[(data["year"] == x1) & (data[y] == y1)][s].values
                    max_x_coords.append(x1)
                    max_y_coords.append(y1)
                    max_s_val.append(sval * bubble_scale)
        plt.scatter(x=max_x_coords, y=max_y_coords, s=max_s_val, c="green", alpha=0.5)
        plt.plot(max_x_coords, max_y_coords, 'g-.')
        plt.scatter(x=min_x_coords, y=min_y_coords, s=min_s_val, c="red", alpha=0.5)
        plt.plot(min_x_coords, min_y_coords, 'r-.')
        # What is the overall maximum?
        max_idx = max_s_val.index(max(max_s_val))
        min_idx = min_s_val.index(min(min_s_val))
        plt.scatter(x=max_x_coords[max_idx], y=max_y_coords[max_idx],
                    s=max_s_val[max_idx],
                    c="green", alpha=1)
        plt.scatter(x=min_x_coords[min_idx], y=min_y_coords[min_idx],
                    s=min_s_val[min_idx],
                    c="red", alpha=1)
    g.set(xlabel=xlabel, ylabel=ylabel, title=title)


def plot_bar(data, x, y, ax, title="", xlabel="", ylabel="",
             xrot=0, yrot=0, point_plot=False, annot=True, legend=False):
    g = sns.barplot(x=x, y=y, data=data, ax=ax)
    if point_plot:
        g1 = sns.pointplot(x=x, y=y, data=data, ax=ax, color="darkblue")
    if xrot != 0:
        g.set_xticklabels(rotation=xrot, labels=g.get_xticklabels())
    if yrot != 0:
        g.set_yticklabels(rotation=yrot, labels=g.get_yticklabels())
    if annot:
        # Add labels to the plot
        style = dict(size=12, color='darkblue')
        s1 = np.round(data[y].values, 2)
        for idx, row in data.iterrows():
            rx, ry = row[x], row[y]
            ax.text(idx*0.99, ry, str(s1[idx]), **style, va="bottom", ha='right')
    g.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.set_ylim([0, data[y].max() * 1.2])
    if legend:
        ax.legend(handles=ax.lines[::len(data) + 1], labels=[y])


def plot_line(data, x, y, ax, title="", xrot=0, yrot=0, sort_x=False, markers="o"):
    g = sns.lineplot(x=x, y=y, data=data, sort=sort_x, markers=markers, ax=ax)
    if xrot != 0:
        g.set_xticklabels(rotation=xrot, labels=data[x])
    if yrot != 0:
        g.set_yticklabels(rotation=yrot, labels=y)
    plt.title(title)
    plt.show()


def group_and_sort(dataframe, dummycol, groupbycol):
    dataframe = dataframe.join(pd.get_dummies(dataframe[dummycol], dummy_na=False))
    data_grp = dataframe.groupby(by=[groupbycol]).sum()
    data_grp["total"] = data_grp.sum(axis=1)
    data_grp.sort_values(by="total", inplace=True, ascending=False)
    return data_grp.drop("total", axis=1)


def find_common_cols(list_of_cols):
    result = set(list_of_cols[0])
    for s in list_of_cols[1:]:
        result.intersection_update(s)
    return result

