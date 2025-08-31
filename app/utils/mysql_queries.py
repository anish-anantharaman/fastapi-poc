from sqlalchemy import text

class ItemQueries:

    ADD_ITEM = text("""INSERT INTO items (item_id, item_name, created_by, created_on, updated_by, updated_on) 
                    VALUES (:item_id, :item_name, :created_by, :created_on, :updated_by, :updated_on)""")

    UPDATE_ITEM = text("""UPDATE items SET item_name = :item_name, updated_by = :updated_by, updated_on = :updated_on 
    WHERE item_id = :item_id""")

    DELETE_ITEM = text("UPDATE items SET deleted_by = :deleted_by, deleted_on = :deleted_on WHERE item_id = :item_id")

    GET_ITEMS = text("SELECT id, item_id, item_name FROM items WHERE deleted_on IS NULL")

    GET_ITEM_BY_ITEM_ID = text("""
                    SELECT id, item_id, item_name FROM items WHERE item_id = :item_id AND deleted_on IS NULL
                    """)

class ValidationQueries:

    CHECK_ITEM_EXISTS = text("SELECT 1 FROM items WHERE item_id = :item_id AND deleted_on IS NULL")

