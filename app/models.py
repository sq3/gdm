
# -*- coding: utf-8 -*-

from sqlalchemy import (Column, Unicode, Integer, ForeignKey, DateTime,
                        SmallInteger, UniqueConstraint)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Models = declarative_base()


class Walker(Models):
    __tablename__ = 'walker'

    pk = Column(Integer, primary_key=True)
    from_address = Column(Unicode, nullable=False)
    client_id = Column(Unicode, nullable=True)
    client_secret = Column(Unicode, nullable=True)

class Migration(Models):
    __tablename__ = 'migration'

    pk = Column(Integer, primary_key=True)
    walker_id = Column(Integer, ForeignKey('walker.pk'), nullable=False)
    to_address = Column(Unicode, nullable=False)
    started = Column(DateTime, nullable=False)
    finished = Column(DateTime, nullable=False)
    total_files = Column(Integer, nullable=False)
    duplicated_files = Columen(Integer, nullable=False)


    walker = relationship(Walker, backref=backref('migration', uselist=True,
                        cascade='delete,all'))
