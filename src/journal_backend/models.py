from pydantic import ColorError
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    journal_items = relationship("JournalItem")

class JournalItem(Base):
    __tablename__ = "journal_items"

    id = Column(Integer, primary_key=True, index=True)
    note = Column(String)
    type = Column(String)
    journal_entry_id = Column(Integer, ForeignKey("journal_entries.id"))
