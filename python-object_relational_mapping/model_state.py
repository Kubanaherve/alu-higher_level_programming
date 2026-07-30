#!/usr/bin/python3
"""Defines State class and Base instance for SQLAlchemy ORM."""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        id: Auto-generated unique integer primary key.
        name: String column with max 128 characters, not null.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
