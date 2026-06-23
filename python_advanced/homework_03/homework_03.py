from decimal import Decimal

from sqlalchemy import create_engine, String, Numeric, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship

engine = create_engine("sqlite:///:memory:")
LocalSession = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    in_stock: Mapped[bool]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    category: Mapped["Category"] = relationship(back_populates="products")


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))

    products: Mapped[list["Product"]] = relationship(back_populates="category")


with engine.begin() as conn:
    Base.metadata.create_all(conn)

with LocalSession() as session:
    product_1 = Product(
        name="Laptop",
        price=Decimal("1499.00"),
        in_stock=True,
        category=Category(
            name="Electronic",
            description="Electronic devices"
        )
    )

    product_2 = Product(
        name="Coat",
        price=Decimal("199.00"),
        in_stock=True,
        category=Category(
            name="Clothes",
            description="Textile"
        )
    )

    session.add(product_1)
    session.add(product_2)
    session.commit()
