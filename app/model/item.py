from sqlalchemy import Column, Integer, BigInteger, String

from app.configs.database import Base

class Item(Base):
    __tablename__="items"

    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True)
    item_id = Column("item_id", BigInteger, index=True, nullable=False)
    item_name = Column("item_name", String, nullable=False)
    created_by = Column("created_by", BigInteger, nullable=False)
    created_on = Column("created_date", BigInteger, nullable=False)
    updated_by = Column("updated_by", BigInteger, nullable=False)
    updated_on = Column("updated_on", BigInteger, nullable=False)
    deleted_by = Column("deleted_by", BigInteger, nullable=True)
    deleted_on = Column("deleted_on", BigInteger, nullable=True)