from pydantic import BaseModel, EmailStr, ValidationError, constr



class LoginScheme(BaseModel):
    email: EmailStr
    password: str
    model_config = {'extra':'forbid'}


class SignUpScheme(BaseModel):
    fistname: str
    lastname: str
    email: EmailStr
    password:str =  constr(min_length=8)
    model_config = {'extra':'forbid'}


class CreateOrganizationScheme(BaseModel):
    name: str
    email: EmailStr
    description: str | None
    model_config = {'extra':'forbid'}

try:
    LoginScheme()
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    

try:
    SignUpScheme()
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    