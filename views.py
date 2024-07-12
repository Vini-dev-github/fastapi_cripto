from fastapi import APIRouter, HTTPException
from services import UserService

from schemas import UserCreateInput, StandartOutput, ErrorOutput

user_route = APIRouter(prefix='/user')
assets_route = APIRouter(prefix='/assets')

@user_route.post('/create', response_model=StandartOutput, responses={400: {'model': ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(name=user_input.name)
        return StandartOutput(messsage='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
