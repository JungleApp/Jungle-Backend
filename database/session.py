#     __             _
#  __|  |_ _ ___ ___| |___
# |  |  | | |   | . | | -_|
# |_____|___|_|_|_  |_|___|
#              |___|
#
# App-Session
# Last Revision: 11/29/16

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

engine = create_engine('mysql://root:JungleDungle82@localhost/jungle', convert_unicode=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a scoped session for thread safety
ssession = scoped_session(Session)