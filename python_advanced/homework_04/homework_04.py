from decimal import Decimal

from sqlalchemy import create_engine, String, Numeric, ForeignKey, select, func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///my_database_1.db")
LocalSession = sessionmaker(bind=engine)


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    in_stock: Mapped[bool]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    category: Mapped["Category"] = relationship(back_populates="products")

    def __str__(self):
        return f"{self.name} {self.price}"


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))

    products: Mapped[list["Product"]] = relationship(back_populates="category")


with engine.begin() as conn:
    Base.metadata.create_all(conn)

with LocalSession() as session:
    electronics = Category(
        name="Electronics",
        description="Gadgets and devices")

    books = Category(
        name="Books",
        description="Books and electronic devices"
    )

    clothes = Category(
        name="Clothes",
        description="Clothes for man and women"
    )

    products = [
        Product(
            name="Smartphone",
            price=Decimal("299.99"),
            in_stock=True,
            category=electronics
        ),
        Product(
            name="Laptop",
            price=Decimal("499.99"),
            in_stock=True,
            category=electronics
        ),
        Product(
            name="SCI-FI Novel",
            price=Decimal("15.99"),
            in_stock=True,
            category=books
        ),
        Product(
            name="Jeans",
            price=Decimal("40.50"),
            in_stock=True,
            category=clothes
        ),
        Product(
            name="T-Shirt",
            price=Decimal("20.00"),
            in_stock=True,
            category=clothes
        )
    ]

    session.add_all([electronics, books, clothes])
    session.add_all(products)
    session.commit()

with LocalSession() as session:
    stmt = select(Product).where(Product.name == "Smartphone")
    product = session.scalars(stmt).first()

    if product is not None:
        product.price = Decimal("349.99")
        session.commit()
    else:
        print("Product is not found")

print("Getting categorized products with prices: ")

with LocalSession() as session:
    categories = session.scalars(select(Category)).all()

    for category in categories:
        print(f"Category: {category.name}")
        for product in category.products:
            print(f"  - {product.name}: {product.price}")

print("-" * 50)
print("Aggregation and group by: ")

with LocalSession() as session:
    stmt = (select(Category.name, func.count(Product.id)).join(Product).group_by(Category.name))
    result = session.execute(stmt).all()

    for cat_name, prod_count in result:
        print(cat_name, prod_count)


print("-" * 50)
print("Filter after group by:")

with LocalSession() as session:
    stmt = (select(Category.name, func.count(Product.id))
            .join(Product).group_by(Category.name).having(func.count(Product.id) > 1))
    result = session.execute(stmt).all()

    for cat_name, prod_count in result:
        print(cat_name, prod_count)
