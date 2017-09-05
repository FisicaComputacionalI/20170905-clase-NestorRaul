[alumno@mod302 ~]$ python
Python 2.6.6 (r266:84292, Jul 22 2015, 16:47:47) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> import pylab as pl
>>> x=[5000, 6000, 7000, 8000, 9000]
>>> y=[65, 78, 88, 89, 93]
>>> pl.plot(x, y)
/usr/lib64/python2.6/site-packages/matplotlib/backends/backend_gtk.py:621: DeprecationWarning: Use the new widget gtk.Tooltip
  self.tooltips = gtk.Tooltips()
[<matplotlib.lines.Line2D object at 0x397b290>]
>>> x1=[7000, 8000, 9000, 10000, 11000]
>>> y2=[65, 75, 85, 86, 90]
>>> pl.plot(x1, y2)
[<matplotlib.lines.Line2D object at 0x33346d0>]
>>> pl.xlabel('Voltaje')
<matplotlib.text.Text object at 0x3740d50>
>>> pl.ylabel(Eficiencia')
  File "<stdin>", line 1
    pl.ylabel(Eficiencia')
                         ^
SyntaxError: EOL while scanning string literal
>>> pl.ylabel('Eficencia')
<matplotlib.text.Text object at 0x3745bd0>
>>> pl.savefig('Eficiencia.png')
>>> 
