from fastapi import APIRouter, Body, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from ..models.prices import *
from ..db.dbconnections import *


router = APIRouter()

@router.get("/prices", tags=["prices"],status_code=HTTP_201_CREATED,)
def get_prices():

    prices_info_query = f"SELECT * FROM PRICES_INFO "
    prices_df = get_sql_df(prices_info_query)

    if len(prices_df) > 0:
        response = {"data":{"prices" : [dict(v) for _, v in prices_df.iterrows()]}}
        
        return response
    else:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="There is no data in prices Table"
        )
