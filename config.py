DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'mysql://root:JungleDungle82@localhost/jungle'
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

CSRF_ENABLED = True

CSRF_SESSION_KEY = 'ahwf984hguablvjn98-3BFWPBSDFA1'

SECRET_KEY = "43-th98qpwiebfAPOIRQB#&)FVBKSD IQNpv"