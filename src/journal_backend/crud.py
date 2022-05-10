from sqlalchemy.orm import Session, joinedload

from . import models, schemas
from datetime import date

def create_journal_item(db: Session, journal_item: schemas.JournalItemBase):
    db_journal_item = models.JournalItem(**journal_item.dict())
    db.add(db_journal_item)
    db.commit()
    db.refresh(db_journal_item)
    return db_journal_item


def create_journal_entry(db: Session, journal_entry: schemas.JournalEntryBase):
    today = date.today()
    db_journal_entry = models.JournalEntry(**journal_entry.dict(), date=today)
    db.add(db_journal_entry)
    db.commit()
    db.refresh(db_journal_entry)
    return db_journal_entry


def get_journal_entry(db: Session, date_query: date | None = None):
    if not date_query:
        date_query = date.today()
    return (
        db.query(models.JournalEntry)
        .filter(models.JournalEntry.date == date_query)
        .first()
    )
