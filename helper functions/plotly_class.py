import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

class InteractivePlot:
    
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def histogram(self):
        fig = go.Figure()

        for columns in self.df.columns:
            fig.add_trace(
                go.Histogram(x=self.df[columns], name=columns)
            )

        button_list = []

        button_list.append(dict(
            label='all columns',
            method="update",
            args=[{"visible": np.full((1, len(self.df.columns)), True).tolist()[0]},
                {"title": f"all columns",
                'xaxis': {'title': 'all columns'},
                    'yaxis': {'title': 'count'}}
                ]
        ))

        for k, v in enumerate(self.df.columns):
            bool_list = np.full((1, len(self.df.columns)), False).tolist()[0]
            bool_list[k] = True

            button_list.append(dict(
                label=v,
                method="update",
                args=[{"visible": bool_list},
                    {"title": f"distribution of {v}",
                    'xaxis': {'title': v},
                    'yaxis': {'title': 'count'}}
                    ]
            ))

        fig.update_layout(title='all columns', xaxis=dict(title='all columns'), 
                yaxis=dict(title='count'), bargap=0.15,
                updatemenus=[
                    dict(buttons=list(button_list))])

        return fig

    def scatterplot_one(self, target):
        assert target in self.df.columns

        columns = [column for column in self.df.columns if column != target]
        
        fig = go.Figure()

        for column in columns:
            fig.add_trace(
                go.Scatter(x=self.df[column], y=self.df[target], name=column, mode='markers')
            )

        button_list = []

        button_list.append(dict(
            label='all columns',
            method="update",
            args=[{"visible": np.full((1, len(columns)), True).tolist()[0]},
                {"title": f"all columns vs {target}",
                'xaxis': {'title': 'all columns except target'},
                'yaxis': {'title': target}}
            ]
        ))

        for k, v in enumerate(columns):
            bool_list = np.full((1, len(columns)), False).tolist()[0]
            bool_list[k] = True

            button_list.append(dict(
                label=v,
                method="update",
                args=[{"visible": bool_list},
                    {"title": f"{v} vs {target}",
                    'xaxis': {'title': v},
                    'yaxis': {'title': target}}
                ]
            ))

        fig.update_layout(title=f'all columns vs {target}', bargap=0.15,
                xaxis=dict(title='all columns except target'),
                yaxis=dict(title=target),
                updatemenus=[
                    dict(buttons=list(button_list))])

        return fig

        