from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, ForeignKey


from app.models import db


class Category(db.Model):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)

    questions: Mapped[list["Question"]] = relationship(back_populates="category")