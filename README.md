Copy Python Paths (Fork Of: [CopyPythonPath](https://github.com/pokidovea/copy_python_path))
================

Simple plugin to copy python import path in various formats to clipboard.

Install
=======

The easiest way to install this is with [Package Control](http://wbond.net/sublime_packages/package_control).

Usage
=====

To copy the python import path of the module select an option from the context menu of side bar or tab.
To copy the path of the python class or method put caret on it and press <kbd>Ctrl+Shift+K</kbd> or `right-click` and select an option from the context menu.


Example
=======

Suppose the following directory tree of your Python project:
```
x.py (class X (def m))
A/
  __init__.py
  y.py (class Y (def m))
  B/
    __init__.py
    z.py (class Z (def m))
```
Depending on the current working file, the following paths will be stored in clipboard:

|(current working file)| (python path copied to clipboard) | (python import path copied to clipboard) | (python django path copied to clipboard)|
|:---------------------|:----------------------------------|:-----------------------------------------|:----------------------------------------|
| x.py | x | import x | x |
| x.py (class X) |  x.X | from x import X | x:X |
| x.py (class X (def M))|  x.X.m | from x.X import m | x:X.m |
| z.py | A.B.z | form A.B import z | A.B.z |
| z.py (class Z)| A.B.z.Z | form A.B.z import Z | A.B.z:Z |
| A/__init__.py | A | import A | A |
| A/B/__init__.py | A.B | from A import B | A.B |