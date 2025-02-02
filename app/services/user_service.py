from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, col
from db.models import UserDb
from db.schemas import  UserUpdate
from typing import Any
from fastapi import HTTPException, status

class UserService:
    async def get_user_by_email(self, user_email: str, session: AsyncSession):
        user = await session.exec(select(UserDb).where(col(UserDb.email) == user_email))
        result = user.first()
        return result
    
    
    async def existing_user(self, user_email: str, session: AsyncSession):
        user = await self.get_user_by_email(user_email, session)
        return user
    
    
    async def update_user(self, data: UserUpdate,
                        session: AsyncSession ,
                        current_user : Any
                        ):
        userdb = await self.get_user_by_email(current_user.email, session)
        if not userdb:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="user not found")

        userdata = data.model_dump(exclude_unset=True)
        for key, value in userdata.items():
            setattr(userdb, key, value)
        session.add(userdb)
        await session.commit()
        await session.refresh(userdb)
        return userdb

        
    # todo : delete current user
    def remove_user(self):
        pass

