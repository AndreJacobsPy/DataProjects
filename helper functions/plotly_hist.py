import plotly.graph_objects as go
import pandas as pd
import numpy as np

def flex_hist(df: pd.DataFrame):
    fig = go.Figure()

    for columns in df.columns:
            fig.add_trace(
                go.Histogram(x=df[columns], name=columns)
            )

    button_list = []
    

    for k, v in enumerate(df.columns):
        bool_list = np.full((1, len(df.columns)), False).tolist()[0]
        bool_list[k] = True

        button_list.append(dict(
            label=v,
            method="update",
            args=[{"visible": bool_list},
                {"title": f"distribution of {v}"}]
        ))

    fig.update_layout(title='title', bargap=0.15,
            updatemenus=[
                dict(buttons=list(button_list))])

    return fig