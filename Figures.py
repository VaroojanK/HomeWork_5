#Basic imports
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import quandl
import plotly.figure_factory as ff
import matplotlib as mpl
import plotly.plotly as py

#Data imports
data_GDP = quandl.get("FRED/GDP", authtoken = "ekmCB1FwgSn3RsyAqVBy")
data_Google = quandl.get("WIKI/GOOGL", authtoken = "ekmCB1FwgSn3RsyAqVBy")
data_Bitcoin = quandl.get("BCHARTS/ABUCOINSUSD", authtoken = "ekmCB1FwgSn3RsyAqVBy")

#Figure_1 as gr1

x_values_1_gr1 = ["X8","X7","X6","X5"]
x_values_2_gr1 = ["X4","X3","X2","X1"]

y_values_1_gr1 = [18,40,18,20]
y_values_2_gr1 = [-18,-55,-5,-38]


trace_1_gr1 = go.Bar(y=x_values_1_gr1, x=y_values_1_gr1, name="<b>Negative</b>", orientation="h",
                 marker=dict(
                     color="pink",
                     line=dict(
                         color="red",
                         width=2))
                )

trace_2_gr1 = go.Bar(y=x_values_2_gr1, x=y_values_2_gr1, name="Positive", orientation="h",
                 marker=dict(
                     color="lightblue",
                     line=dict(
                         color="blue",
                         width=2))
                 )

layout_gr1 = dict(title="<b>Correlation with employees probability of churn</b>",
                 yaxis=dict(title="Variable"))


data_gr1 = [trace_1_gr1,trace_2_gr1]
gr1 = dict(data=data_gr1, layout=layout_gr1)

#Figure_2 as gr2

x_values_gr2 = pd.to_datetime(data_GDP.index.values)
y_values_gr2 = data_GDP.Value

trace_gr2 = go.Scatter(x=x_values_gr2, y = y_values_gr2,
                        mode = "lines", fill = "tozeroy")


layout_gr2=dict(title="<b>US GDP over time</b>",)

data_gr2 = [trace_gr2]
gr2 = dict(data=data_gr2, layout=layout_gr2)


#Figure_3 as gr3

x_values_1_gr3=data_Google.Open.pct_change()
x_values_2_gr3=data_Bitcoin.Open.pct_change()

trace_1_gr3 = go.Box(x=x_values_2_gr3, name="<b>Bitcoin</b>")
trace_2_gr3 = go.Box(x=x_values_1_gr3, name="<b>Google</b>")

layout_gr3=dict(title="Distribution of Price Changes")

data_gr3 = [trace_1_gr3,trace_2_gr3]
gr3 = dict(data=data_gr3, layout=layout_gr3)

#Figure_4 as gr4

header = dict(values=['Google', 'Bitcoin'],
            align=["left", "center"],
            font=dict(color="white", size=12),
            fill=dict(color="#3349FF"),
             )

data_Google["%C"]=data_Google.Open.pct_change()
data_Bitcoin["%C"]=data_Bitcoin.Open.pct_change()


data_Google_1=data_Google.iloc[1:5, -1].round(3)
data_Bitcoin_1=data_Bitcoin.iloc[1:5, -1].round(3)

data_Google_2=data_Google_1.values
data_Bitcoin_2=data_Bitcoin_1.values


cells = dict(values=[data_Google_2,data_Bitcoin_2],
             align=["left", "center"],
             fill=dict(color=["yellow", "white"])
            )

trace_gr4 = go.Table(header=header, cells=cells)

data_gr4 = [trace_gr4]
layout_gr4=dict(width=500, height=300)
gr4=dict(data=data_gr4, layout=layout_gr4)

#Figure_5 as gr5

import plotly.figure_factory as ff

trace_gr5=[dict(Task="Task 1", Start="2018-01-01", Finish="2018-01-31", Resource = 'Idea Validation'),
          dict(Task="Task2", Start="2018-03-01", Finish="2018-04-15", Resource = 'Prototyping'),
          dict(Task="Task3", Start="2018-04-15", Finish="2018-09-03", Resource = 'Team Formation')]

data_gr5=ff.create_gantt(trace_gr5, index_col='Resource' , title='Startup Roadmap', show_colorbar=True)
