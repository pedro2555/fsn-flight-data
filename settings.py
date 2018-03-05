#!/usr/bin/env python
"""
RESTfull API for flight telemetry reports for FSN
Copyright (C) 2017 Pedro Rodrigues <prodrigues1990@gmail.com>

This file is part of FSN Flight Data Service.

FSN Flight Data Service is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

FSN Flight Data Service is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with FSN Flight Data Service.  If not, see <http://www.gnu.org/licenses/>.
"""

import os

PAGINATION_LIMIT = 100
PAGINATION_DEFAULT = 100

DOMAIN = {
    'transponders': {
        'item-title': 'transponder',
        'resource_methods': ['POST'],
        'item_methods': ['DELETE'],
        'schema': {}
    },
    'position-reports': {
        'item_title': 'position-report',
        'resource_methods': ['GET', 'POST', 'DELETE'],
        'item_methods': ['GET', 'PUT', 'PATCH', 'DELETE'],
        'allow_unknown': True,
        'schema': {
            'transponder': {
                'type': 'objectid',
                'required': True,
                'data_relation': {
                    'resource': 'transponders',
                    'field': '_id'
                }
            },
            'position': {
                'type': 'point'
            },
            'timestamp': {
                'type': 'datetime'
            },
            'compass': {
                'type': 'integer'
            },
            'altitude': {
                'type': 'integer'
            },
            'groundspeed': {
                'type': 'integer'
            },

        }
    }
}

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'fsn-flight-data')

#X_DOMAINS = ('http://localhost:8081', 'http://127.0.0.1:8081')
X_DOMAINS_RE = [
    '^http://localhost:.+$',
    '^http://127.0.0.1:.+$',
    '^https://fsn-app.herokuapp.co(.+)$',
    '^https://pedro2555.github.io(.+)$']
X_HEADERS = ['Authorization', 'Content-type']
