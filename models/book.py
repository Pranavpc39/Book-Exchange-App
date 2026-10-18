from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    author: str = Field(index=True)
    price: int
    is_sold: Optional[bool] = Field(default=False)

    #Foriegn key
    user_id: int = Field(foreign_key="user.id")

    # Relationship
    owner: Optional["User"] = Relationship(back_populates="books")

class BookCreate(SQLModel):
    title: str
    author: str
    price: int
    user_id: int

class BookRead(SQLModel):
    id: int
    title: str
    author: str
    price: int
    is_sold: bool
    user_id: int

class BookUpdate(SQLModel):
    price: Optional[int] = None
    is_sold: bool = None

from models.user import User
Book.model_rebuild()