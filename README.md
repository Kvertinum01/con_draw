<h1 align="center">
  con_draw (0.x)
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/made%20by-Kvertinum01-green">
</p>

> Cross-platform framework for drawing in console

## Hello World

```python
from con_draw import Drawer

drawer = Drawer()

for frame in drawer.frames():
    frame.add_str((3, 5), "Hello world")
    frame.update()
```

> More examples [here](/examples)

## Installation

### Latest version

```shell
pip install -U "git+https://github.com/Kvertinum01/con_draw"
```
