from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import NotFoundException, BadRequestException
from app.model.item import Item
from app.utils.mysql_queries import ItemQueries, ValidationQueries


class ItemRepository:

    def __init__(self, session: Session):
        self.session = session
        self.item_queries: ItemQueries = ItemQueries()
        self.validation_queries: ValidationQueries = ValidationQueries()

    def add_item(self, item: Item) -> None:
        try:
            self.session.execute(
                self.item_queries.ADD_ITEM,
                {
                    "item_id": item.item_id, "item_name": item.item_name, "created_by": item.created_by,
                    "created_on": item.created_on, "updated_by": item.updated_by, "updated_on": item.updated_on
                }
            )
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise BadRequestException(f"Item already exists with item ID: {item.item_id}")

    def update_item(self, item: Item) -> None:
        # Check if item exists, then perform update
        item_exists = self.session.execute(
            self.validation_queries.CHECK_ITEM_EXISTS,
                {
                    "item_id": item.item_id
                }
        ).fetchone()
        if not item_exists:
            raise NotFoundException(f"Item not found with item ID: {item.item_id}")

        self.session.execute(
            self.item_queries.UPDATE_ITEM,
            {
                "item_name": item.item_name, "updated_by": item.updated_by,
                "updated_on": item.updated_on, "item_id": item.item_id
            }
        )
        self.session.commit()

    def delete_item(self, item: Item) -> None:
        self.session.execute(
            self.item_queries.DELETE_ITEM,
            {
                "item_id": item.item_id, "deleted_by": item.deleted_by,
                "deleted_on": item.deleted_on
            }
        )
        self.session.commit()

    def get_items(self):
        return self.session.execute(self.item_queries.GET_ITEMS).fetchall()

    def get_item_by_id(self, item_id: int):
        result = self.session.execute(
            self.item_queries.GET_ITEM_BY_ITEM_ID,
            {
                "item_id": item_id
            }
        ).fetchone()
        if not result:
            raise NotFoundException(f"Item not found with item_id: {item_id}")
        return result