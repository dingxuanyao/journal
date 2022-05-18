from datetime import date
from pydantic import BaseModel


# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None


# class ItemCreate(ItemBase):
#     pass


# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     items: list[Item] = []

#     class Config:
#         orm_mode = True


class JournalItemBase(BaseModel):
    journal_entry_id: int
    note: str
    type: str


class JournalItem(JournalItemBase):
    id: int

    class Config:
        orm_mode = True


class JournalEntryBase(BaseModel):
    pass


class JournalEntry(JournalEntryBase):
    id: int
    journal_items: list[JournalItem] = []
    date: date

    class Config:
        orm_mode = True
