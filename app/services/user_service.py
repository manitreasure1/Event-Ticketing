from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, col
from db.models import UserDb

class UserService:
    async def get_user_by_email(self, user_email: str, session: AsyncSession):
        user = await session.exec(select(UserDb).where(col(UserDb.email) == user_email))
        result = user.first()
        return result
    
    async def existing_user(self, user_email: str, session: AsyncSession):
        user = await self.get_user_by_email(user_email, session)
        return user


        
    # todo : update current user
    # async def update_user(user_id: int, user:UpdateUserRequest,  session: AsyncSession):
    #     user_db = session.get(UserDb, user_id)
    #     if not user_db:
    #         raise HTTPException(status.HTTP_404_NOT_FOUND, detail="user not found")
    #     user_data = user.model_dump(exclude_unset=True)
    #     user_db.sqlmodel_update(user_data)
    #     session.add(user_db)
    #     session.commit()
    #     session.refresh(user_db)
    #     return user_db
        
    # todo : delete current user
    def remove_user(self):
        pass

