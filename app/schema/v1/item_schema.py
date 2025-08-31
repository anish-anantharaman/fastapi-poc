from typing import Optional

from pydantic import Field, BaseModel

from app.utils.date_util import current_epoch_millis


class BaseItemSchema(BaseModel):
    """Base schema to create an item entry"""
    item_id: int = Field(...)
    item_name: str = Field(...)
    created_by: int = Field(...)
    created_on: int = Field(default_factory=current_epoch_millis)
    updated_by: int = Field(...)
    updated_on: int = Field(default_factory=current_epoch_millis)
    deleted_by: Optional[int] = Field(None)
    deleted_on: Optional[int] = Field(None)


class UpdateItemSchema(BaseModel):
    """Schema to update an item entry"""
    item_id: int = Field(...)
    item_name: str = Field(...)
    updated_by: int = Field(...)
    updated_on: int = Field(default_factory=current_epoch_millis)

class DeleteItemSchema(BaseModel):
    """Schema to delete an item enry"""
    item_id: int = Field(...)
    deleted_by: int = Field(...)
    deleted_on: int = Field(default_factory=current_epoch_millis)


class ResponseItemSchema(BaseModel):
    """Schema to fetch items"""
    id: int
    item_id: int
    item_name: str

