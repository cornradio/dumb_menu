# dumb_menu
one day i want to make a menu for my progarm, but i don't want to use any library they are so heavy and not support both mac and windows (i am talking about u : simple_term_menu ), so i make this.

dumb_menu is a ligh weight menu ,support hot key, support both win and mac ,not tested on linux.

## Usage

```python
import dumb_menu
options = ["[1]Option 1", "[2]Option 2", "[3]Option 3","[q]quit"]
index = dumb_menu.get_menu_choice(options)
print(f"You selected option {index + 1}: {options[index]}")
```

![png](https://raw.githubusercontent.com/cornradio/imgs/main/20230214163952.png)

## Installation

https://pypi.org/project/dumb-menu/

## how to upload a new version (for me)

en: https://packaging.python.org/tutorials/packaging-projects/ 

zh: https://python-packaging-zh.readthedocs.io/zh_CN/latest/minimal.html#id2

1. change `setup.py`
2. testing `python setup.py develop`
3. `python3 setup.py sdist`
4. `twine upload dist/*`