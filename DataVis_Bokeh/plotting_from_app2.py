# Ne znam zašto ne radi.

import pandas
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df=pandas.read_csv('Sample_of_the_produced_time_values.csv')
cds=ColumnDataSource(df)

p = figure(width=1000, height=500, x_axis_type="datetime", sizing_mode="scale_both")
# p=figure(x_axis_type='datetime', height=300, width=800, title="Motion Graph")

q=p.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

# print(df["Start"])
# print(df["End"])
output_file("Graph.html")
show(p)
