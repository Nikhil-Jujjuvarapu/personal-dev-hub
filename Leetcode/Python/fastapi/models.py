from sqlalchemy import Column, Integer, String

from database import Base


class ProductTable(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
