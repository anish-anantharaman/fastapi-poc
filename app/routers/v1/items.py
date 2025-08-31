from fastapi import APIRouter, Depends, status, Request, Query

from app.dependencies import get_item_service
from app.schema.v1.item_schema import BaseItemSchema, UpdateItemSchema, DeleteItemSchema
from app.services.item_service import ItemService
from app.utils.constants import StatusMessage
from app.utils.project_util import get_request_id
from app.utils.response_builder import build_response, ResponseBuilder

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("", response_model=ResponseBuilder, status_code=status.HTTP_201_CREATED)
def add_item(request: Request, input_data: BaseItemSchema, item_service: ItemService = Depends(get_item_service)):
    response = item_service.add_item(input_data, request)
    return build_response(
        status_code=status.HTTP_201_CREATED,
        status_message=StatusMessage.CREATED,
        response_data=response,
        request=request
    )

@router.patch("", response_model=ResponseBuilder, status_code=status.HTTP_200_OK)
def update_item(request: Request, input_data: UpdateItemSchema, item_service: ItemService = Depends(get_item_service)):
    response = item_service.update_item(input_data, request)
    return build_response(
        status_code=status.HTTP_200_OK,
        status_message=StatusMessage.SUCCESS,
        response_data=response,
        request=request
    )

@router.delete("/{item_id}", response_model=ResponseBuilder, status_code=status.HTTP_200_OK)
def delete_item(request: Request, item_id: int, deleted_by: int = Query(...),
                item_service: ItemService = Depends(get_item_service)):
    delete_item_schema = DeleteItemSchema(item_id=item_id, deleted_by=deleted_by)
    response = item_service.delete_item(delete_item_schema, request)
    return build_response(
        status_code=status.HTTP_200_OK,
        status_message=StatusMessage.SUCCESS,
        response_data=response,
        request=request
    )

@router.get("", response_model=ResponseBuilder, status_code=status.HTTP_200_OK)
def get_items(request: Request, item_service: ItemService = Depends(get_item_service)):
    response = item_service.get_items()
    return build_response(
        status_code=status.HTTP_200_OK,
        status_message=StatusMessage.SUCCESS,
        response_data=response,
        request=request
    )

@router.get("/{item_id}", response_model=ResponseBuilder, status_code=status.HTTP_200_OK)
def get_item_by_id(request: Request, item_id: int, item_service: ItemService = Depends(get_item_service)):
    response = item_service.get_item_by_id(item_id)
    return build_response(
        status_code=status.HTTP_200_OK,
        status_message=StatusMessage.SUCCESS,
        response_data=response,
        request=request
    )