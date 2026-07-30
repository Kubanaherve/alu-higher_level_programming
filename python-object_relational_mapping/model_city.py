#!/usr/bin/python3
"""Defines City class for SQLAlchemy ORM."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represents a city for a MySQL database.

    Attributes:
        id: Auto-generated unique integer primary key.
        name: String column with max 128 characters, not null.
        state_id: Foreign key referencing states.id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
