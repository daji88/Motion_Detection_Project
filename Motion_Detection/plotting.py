from capture import df1
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df1["Start_str"] = df1["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df1["End_str"] = df1["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df1)

p = figure(x_axis_type='datetime', height=300, width=1050, title='Motion Graph')
p.yaxis.minor_tick_line_color = None
p.ygrid.grid_line_alpha = 0.00

hover = HoverTool(tooltips = [("Start", "@Start_str"), ("End", "@End_str")])
p.add_tools(hover)

q = p.quad(left='Start', right='End', top=1, bottom=0, color='Green', source = cds)

output_file('Graph.html')
show(p)