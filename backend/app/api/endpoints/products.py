from fastapi import APIRouter, Body, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from ..models.products import *
from ..db.dbconnections import *


router = APIRouter()

@router.get("/products", tags=["products"],status_code=HTTP_201_CREATED,)
def get_products():

    products_info_query = f"SELECT * FROM PRODUCTS_INFO "
    products_df = get_sql_df(products_info_query)

    if len(products_df) > 0:
        response = {"data":{"products" : [dict(v) for _, v in products_df.iterrows()]}}
        
        return response
    else:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="There is no data in Products Table"
        )
