from typing import Any
from fastapi import HTTPException, status
from sqlmodel import select, col
from db.models import Organization
from db.schemas import OrganizationCreate
from sqlmodel.ext.asyncio.session import AsyncSession


class OrganizationService:

    async def get_organization(self, organization_email: str, session: AsyncSession):
        organization_db = await session.exec(select(Organization).where(col(Organization.email) == organization_email))
        org = organization_db.first()
        return org

    async def create_organization(self,
                                  data: OrganizationCreate,
                                  session: AsyncSession,
                                  user_id: int
                                  ):
        get_org = await self.get_organization(data.email, session)
        if get_org:
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Organization email already registered")
        organization_data = Organization(
            name=data.name,
            email=data.email,
            description=data.description,
            created_by=user_id
        )
        session.add(organization_data)
        await session.commit()
        await session.refresh(organization_data)
        return organization_data       
    

    async def update_organization(self):
        pass

    async def remove_organization(self):
        pass

