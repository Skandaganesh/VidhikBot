from pydantic import BaseModel

class UserData(BaseModel):
    user_id: str

class UserResponse(BaseModel):
    user_id: str
    query: str

class textInput(BaseModel):
    text: str
    
class KnowlegdeQuery(BaseModel):
    user_query: str