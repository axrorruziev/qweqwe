from pydantic import BaseModel


class LoginValidator(BaseModel):
    phone_number: int
    password: str


class RegisterValidator(BaseModel):
    name: str
    surname: str
    phone_number: int
    city: str
    password: str


class EditUserInfoValidator(BaseModel):
    user_id: int
    edit_info: str
    new_info: str

