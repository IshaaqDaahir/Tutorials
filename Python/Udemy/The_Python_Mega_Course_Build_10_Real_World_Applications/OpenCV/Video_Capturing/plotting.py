from capture import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%M-%D %H:%M:%S")

cds = ColumnDataSource(df) 

p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode='scale_both', 
           title='Motion Graph')
p.yaxis.minor_tick_line_color = None
p.ygrid.grid_line_color = None

hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q = p.quad(left='Start', right='End', bottom=0, top=1, color='green', source=cds)

output_file('Graph1.html')
show(p)