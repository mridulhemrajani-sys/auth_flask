from pydantic import BaseModel, EmailStr, Field

class RegisterRequest(BaseModel):
    name : str
    email : EmailStr
    password : str = Field(min_length=6, description='Password must be atleast 6 characters long')

class LoginRequest(BaseModel):
    email : EmailStr
    password : str

