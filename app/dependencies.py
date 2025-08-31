from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.configs.database import get_db
from app.services.item_service import ItemService


def get_item_service(session: Session = Depends(get_db)) -> ItemService:
    return ItemService(session)
