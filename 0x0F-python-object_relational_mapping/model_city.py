#!/usr/bin/python3
"""
Alchemy Docs
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Base Class
    """

    __tablename__ = "cities"
    id = Column("id", Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
	
