#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:00:58 2021

@author: mgao
"""


from flask import Flask
from jinja2 import Markup
from pyecharts import options as opts
from pyecharts.charts import Bar
app = Flask(__name__, static_folder="templates")
def bar_base() -> Bar:
  c = (
    Bar()
      .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
      .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
      .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
      .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
  )
  return c
@app.route("/")
def index():
  c = bar_base()
  return Markup(c.render_embed())
if __name__ == "__main__":
  app.run()