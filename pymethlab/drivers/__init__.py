#  methlab - A music library application
#  Copyright (C) 2007 Ingmar K. Steen (iksteen@gmail.com)
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

__all__ = ['DRIVERS']

def init():
  drivers = []
  import os, glob
  dirname = os.path.split(__file__)[0]
  for path in glob.glob(os.path.join(dirname, '*.py')):
    filename = os.path.split(path)[1]
    name = os.path.splitext(filename)[0]
    if name == '__init__':
      continue
    try:
      mod = __import__(name, globals(), locals(), ['DRIVERS'], -1)
    except ImportError, e:
      continue
    if hasattr(mod, 'DRIVERS'):
      for driver in mod.DRIVERS:
        drivers.append(getattr(mod, driver))
  return drivers

DRIVERS = init()
for driver in DRIVERS:
  locals()[driver.__name__.split('.')[-1]] = driver
