from sqlalchemy import Sequence, Row

from app.schema.v1.item_schema import ResponseItemSchema


def map_items_response(rows: Sequence[Row]) -> list[ResponseItemSchema]:
    return [map_item_response(row) for row in rows]

def map_item_response(row: Row) -> ResponseItemSchema:
    return ResponseItemSchema(
        id=row.id,
        item_id=row.item_id,
        item_name=row.item_name
    )