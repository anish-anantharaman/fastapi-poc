from fastapi import Request
from sqlalchemy.orm import Session

from app.configs.logging_config import logger
from app.mapper.item_mapper import map_items_response, map_item_response
from app.model.item import Item
from app.repository.item_repository import ItemRepository
from app.schema.v1.item_schema import BaseItemSchema, UpdateItemSchema, ResponseItemSchema, DeleteItemSchema
from app.utils.project_util import get_request_id


class ItemService:

    def __init__(self, session: Session):
        self.repository: ItemRepository = ItemRepository(session)

    def add_item(self, item_data: BaseItemSchema, request: Request) -> bool:
        item = Item(
            item_id=item_data.item_id,
            item_name=item_data.item_name,
            created_by=item_data.created_by,
            created_on=item_data.created_on,
            updated_by=item_data.updated_by,
            updated_on=item_data.updated_on
        )
        self.repository.add_item(item)
        logger.info("Item added successfully | item_id: %s | request_id: %s", item_data.item_id,
                    get_request_id(request))

        return True

    def update_item(self, item_data: UpdateItemSchema, request: Request) -> bool:
        logger.debug("trying to update item!!")
        item = Item(
            item_id=item_data.item_id,
            item_name=item_data.item_name,
            updated_by=item_data.updated_by,
            updated_on=item_data.updated_on
        )
        self.repository.update_item(item)
        logger.info("Item updated successfully | item_id: %s | request_id: %s", item_data.item_id,
                    get_request_id(request))
        return True

    def delete_item(self, item_data: DeleteItemSchema, request: Request) -> bool:
        item = Item(
            item_id=item_data.item_id,
            deleted_by=item_data.deleted_by,
            deleted_on=item_data.deleted_on
        )
        self.repository.delete_item(item)
        logger.info("Item deleted successfully | item_id: %s | request_id: %s",
                    item_data.item_id, get_request_id(request))
        return True

    def get_items(self) -> list[ResponseItemSchema]:
        result = self.repository.get_items()
        return map_items_response(result)

    def get_item_by_id(self, item_id: int) -> ResponseItemSchema:
        result = self.repository.get_item_by_id(item_id)
        return map_item_response(result)
