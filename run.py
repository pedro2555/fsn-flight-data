#!/usr/bin/env python
"""
This program is just an example API
Copyright (C) 2017 Pedro Rodrigues <prodrigues1990@gmail.com>

This file is part of N360 Sample API.

N360 Sample API is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

N360 Sample API is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with N360 Sample API.  If not, see <http://www.gnu.org/licenses/>.
"""

from eve import Eve
import os

app = Eve()

# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    host = '0.0.0.0'
    debug = False
else:
    port = 5000
    host = '0.0.0.0'
    debug = True

if __name__ == '__main__':
	app.run(host=host, port=port, debug=debug)
