# dumb_menu

[![Downloads](https://static.pepy.tech/badge/dumb-menu)](https://pepy.tech/project/dumb-menu)

simple_term_menu don't support windows, so i made this.

this is not as powerful as simple_term_menu , but this is **THE GOOD OLD MEUN** .

dumb_menu is a **ligh weight** menu ,support **hot key**, for both **win** and **mac** .


## Installation

https://pypi.org/project/dumb-menu/

https://github.com/cornradio/dumb_menu (i want stars ⭐ uwu)

## Usage

```python
import dumb_menu
options = ["[1]Option 1", "[2]Option 2", "[3]Option 3","[q]quit"]
index = dumb_menu.get_menu_choice(options)
print(f"You selected option {index + 1}: {options[index]}")
```

![png](https://raw.githubusercontent.com/cornradio/imgs/main/20230214163952.png)

## how to upload a new version (for me)

en: https://packaging.python.org/tutorials/packaging-projects/ 

zh: https://python-packaging-zh.readthedocs.io/zh_CN/latest/minimal.html#id2

1. change `setup.py`
2. testing `python3 setup.py develop`
3. `python3 setup.py sdist`
4. `twine upload dist/*`

test code :
```
python3

import dumb_menu
dumb_menu.demo()
```

## Get help

Get help ➡️ [Github issue](https://github.com/cornradio/dumb_menu/issues)

## Update log


`1.0.7` fix "flickering on mac zsh" 

`1.0.6` forget write log in 1.0.5

`1.0.5` fix bug in 1.0.4

`1.0.4` support "clean mode" 

`1.0.3` show selected index also when using hotkey  

`1.0.2` first useable version

`1.0.1` fix bug

`1.0.0` first release