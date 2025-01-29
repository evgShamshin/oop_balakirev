class TravelBlog:
    total_blogs = 0

tb1, tb2 = TravelBlog(), TravelBlog()

_data_1 = {"name": 'Франция',
     "days": 6}

_data_2 = {"name": 'Италия',
     "days": 5}

[setattr(tb1, _d[0], _d[1]) for _d in _data_1.items()]
TravelBlog.total_blogs = TravelBlog.total_blogs + 1
[setattr(tb2, _d[0], _d[1]) for _d in _data_2.items()]
TravelBlog.total_blogs = TravelBlog.total_blogs + 1