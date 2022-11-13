from fastapi import APIRouter, Body, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from ..models.user import *
from ..db.dbconnections import *


router = APIRouter()


@router.post("/createuser", response_model=UserRegisterResponse, tags=["users"],status_code=HTTP_201_CREATED,)
def create_user(info:UserRegisterBase):

    email_id = info.email
    user_password = info.password
    user_confirm_password = info.confirm_password

    users_info_query = f"SELECT COUNT(1) FROM USER_INFO WHERE UPPER(EMAIL_ID) = '{email_id}' "
    user_check_df = get_sql_df(users_info_query)

    if (user_password.lower() == user_confirm_password.lower()) and (int(user_check_df.iloc[0][0]) == 0 ):
        insert_user_query =  f"INSERT INTO USER_INFO (EMAIL_ID,PASSWORD) VALUES ('{email_id}','{user_password}')"
        create_response = sql_query_executor(insert_user_query)

        return UserRegisterResponse(email=email_id)
    else:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Email Already Exists"
        )


@router.post("/login", tags=["users"],status_code=HTTP_201_CREATED,)
def login_user(info:UserLoginBase):

    email_id = info.email
    user_password = info.password

    users_info_query = f"SELECT PASSWORD FROM USER_INFO WHERE UPPER(EMAIL_ID) = '{email_id}' "
    user_check_df = get_sql_df(users_info_query)
    db_password = str(user_check_df.iloc[0][0])

    if (user_password.lower() == db_password.lower()):

        return {"response":"User Login Successful"}
    else:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Incorrect Password"
        )
