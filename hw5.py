#Homework5
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import quandl
import plotly.figure_factory as ff
import matplotlib as mpl
import plotly.plotly as py


from Figures import gr1
from Figures import gr2
from Figures import gr3
from Figures import gr4
from Figures import data_gr5

slider_data = quandl.get ("FRED/GDP", authtoken = "ekmCB1FwgSn3RsyAqVBy")

app=dash.Dash()

app.css.append_css({"external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

#Heading

app.layout=html.Div([

	html.Div([html.H1(children="Homework 5", style={"color":"red", "text-align":"center", "font-weight":"bold",})],
		className="twelve columns"),

#Radio Button

html.Div([
			
			html.Div([

			dcc.RadioItems(id="radio", options=[
            {"label": "Employee Churn", "value": gr1}],
            value="show"),

            dcc.RadioItems(id="radio", options=[
            {"label": "Startup RoadMap", "value": data_gr5}],
            value="show")

            ], className="three columns"),

			
			html.Div([
			dcc.Graph(id="Graph")],
			className="nine columns"),

			], className="twelve columns"),

#Dropdown menu

html.Div([
			html.Div([dcc.Dropdown(
				id = 'dropdown',
				options=[
	            {'label': 'Google', 'value': 'GOOGL'},
	            {'label': 'Apple', 'value': 'AAPL'},
	            {'label': 'Microsoft', 'value': 'MSFT'},
	            {'label': 'Lenovo', 'value': '00992'},
	            {'label': 'HP', 'value': 'HPQ'}
			],
				placeholder='Please, select a stock', multi=True),

				html.Button(id='submit',n_clicks=0, children='Submit'),
			],	className="two columns"),

			html.Div([
			dcc.Graph(id="Boxplot")],
			className="five columns"),

			html.Div([
			dcc.Graph(id="Table")],
			className="five columns"),

			], className="twelve columns"),



#slider

html.Div([
	html.Div([dcc.RangeSlider(id = 'option_in', min=0, max=len(slider_data.index), value= [0, len(slider_data.index)])],
	className= 'four columns'),

	html.Div([dcc.Graph(id='GDP')],
		className= 'eight columns'),
	], className= 'twelve columns',)


])

#Button

@app.callback(
    Output(component_id="Graph", component_property="figure"),
    [Input(component_id="radio", component_property="value")])
	
def update_graph(Input_value):
	figure=Input_value
	return figure



#Dropdown


@app.callback(
    Output(component_id='Boxplot', component_property='figure'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='dropdown', component_property='value')])

def update_graph(clicks, input_value1):
	quandl_input_1 = "WIKI/"+input_value1[0]
	quandl_input_2 = "WIKI/"+input_value1[1]
	
	stock_data_1 = quandl.get(quandl_input_1, authtoken = "ekmCB1FwgSn3RsyAqVBy")
	stock_data_2 = quandl.get(quandl_input_2, authtoken = "ekmCB1FwgSn3RsyAqVBy")
	
	x_values_1 = stock_data_1.Open.pct_change()
	x_values_2 = stock_data_2.Open.pct_change()
	
	trace_1 = go.Box(x=x_values_1, name=input_value1[0])
	trace_2 = go.Box(x=x_values_2, name=input_value1[1])
	
	layout_f3 = dict(title="<i>Distribution of Price changes</i> "+input_value1[0]+" and "+input_value1[1])
	data_f3 = [trace_1,trace_2]
	figure = dict(data=data_f3, layout=layout_f3)
	return figure


#Table

@app.callback(
    Output(component_id='Table', component_property='figure'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='dropdown', component_property='value')]
)

def update_table(clicks, input_value2):

	quandl_input_3 ="WIKI/"+input_value2[0]
	quandl_input_4 = "WIKI/"+input_value2[1]
	
	stock_data_3 = quandl.get(quandl_input_3, authtoken = "ekmCB1FwgSn3RsyAqVBy")
	stock_data_4 = quandl.get(quandl_input_4, authtoken = "ekmCB1FwgSn3RsyAqVBy")

	stock_data_3["%C"] = stock_data_3.Open.pct_change()
	stock_data_4["%C"] = stock_data_4.Open.pct_change()
	
	stock_data3=stock_data_3.iloc[1:5,-1:].round(3)
	stock_data4=stock_data_4.iloc[1:5,-1:].round(3)

	header= dict(values=[input_value2[0],input_value2[1]],
				align=["left", "center"],
				font=dict(color="white", size=12),
				fill=dict(color="#119DFF"),
				)


	cells = dict(values=[stock_data3.values, stock_data4.values],
             align=["left", "center"],
             fill=dict(color=["yellow", "white"]))

	trace_gr4 = go.Table(header=header, cells=cells)

	data_gr4 = [trace_gr4]

	layout_gr4=dict(width=500, height=300)

	gr4=dict(data=data_gr4, layout=layout_gr4)

	return gr4


#SLider


@app.callback(
    Output(component_id='GDP', component_property='figure'),
    [Input(component_id='option_in', component_property='value')]
)
def update_graph(Input_value):

	slide_index = slider_data.index[Input_value[0]: Input_value[1]]
	slide_values = slider_data.Value[Input_value[0]: Input_value[1]]

	data = [go.Scatter(x= slide_index, y=slide_values, fill='tozeroy')]
	layout = dict (title = 'US GDP')
	figure = dict (data=data, layout= layout)
	return figure




if __name__ == '__main__':
	app.run_server(debug=True)
