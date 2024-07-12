from pydantic import BaseModel

class UserCreateInput(BaseModel):
    name: str

class StandartOutput(BaseModel):
    messsage: str

class AlternativeOutpu(StandartOutput):
    detail: str

class ErrorOutput(BaseModel):
    details: str
