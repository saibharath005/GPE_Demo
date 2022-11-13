from pydantic import BaseModel


class UserLoginBase(BaseModel):
    email: str
    password: str

class UserRegisterBase(BaseModel):
    email: str
    password: str
    confirm_password: str

class UserRegisterResponse(BaseModel):
    email: str
