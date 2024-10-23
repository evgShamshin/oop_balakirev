class Figure:
    type_fig = 'ellipse'
    color = 'red'

fig1 = Figure()

_data = {"start_pt": (10, 5),
         "end_pt": (100, 20),
         "color": "blue"}

[setattr(fig1, _d[0], _d[1]) for _d in _data.items()]
if 'color' in fig1.__dict__: delattr(fig1, "color")
print(*fig1.__dict__)