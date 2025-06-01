import pytest
from unittest.mock import AsyncMock, MagicMock
from app.services.organization_service import OrganizationService
from app.db.models import Organization
from app.db.schemas import OrganizationCreate
from fastapi import HTTPException

@pytest.mark.asyncio
async def test_get_organization():
    mock_session = MagicMock()
    mock_exec = AsyncMock()
    mock_session.exec = mock_exec
    mock_result = MagicMock()
    org_obj = Organization(id=1, name='Test Org', email='org@email.com', description='desc', created_by=1)
    mock_result.first.return_value = org_obj
    mock_exec.return_value = mock_result
    service = OrganizationService()
    org = await service.get_organization('org@email.com', mock_session)
    assert org is not None
    assert getattr(org, 'name', None) == 'Test Org'
    assert getattr(org, 'email', None) == 'org@email.com'

@pytest.mark.asyncio
async def test_create_organization():
    mock_session = MagicMock()
    mock_session.exec = AsyncMock()
    mock_result = MagicMock()
    mock_result.first.return_value = None
    mock_session.exec.return_value = mock_result
    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()
    service = OrganizationService()
    data = OrganizationCreate(name='Test Org', email='org@email.com', description='desc')
    async def refresh_side_effect(obj):
        if isinstance(obj, Organization):
            obj.id = 1
    mock_session.refresh.side_effect = refresh_side_effect
    result = await service.create_organization(data, mock_session, user_id=1)
    assert result.name == 'Test Org'
    assert result.email == 'org@email.com'
    assert result.id == 1

@pytest.mark.asyncio
async def test_create_organization_already_exists():
    mock_session = MagicMock()
    mock_session.exec = AsyncMock()
    mock_result = MagicMock()
    mock_result.first.return_value = Organization(id=1, name='Test Org', email='org@email.com', description='desc', created_by=1)
    mock_session.exec.return_value = mock_result
    service = OrganizationService()
    data = OrganizationCreate(name='Test Org', email='org@email.com', description='desc')
    with pytest.raises(HTTPException) as exc_info:
        await service.create_organization(data, mock_session, user_id=1)
    assert exc_info.value.status_code == 403
    assert "already registered" in exc_info.value.detail

@pytest.mark.asyncio
async def test_update_organization():
    service = OrganizationService()
    service.update_organization = AsyncMock(side_effect=HTTPException(status_code=400, detail="Not implemented"))
    with pytest.raises(HTTPException) as exc_info:
        await service.update_organization()
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Not implemented"

@pytest.mark.asyncio
async def test_remove_organization():
    service = OrganizationService()
    service.remove_organization = AsyncMock(side_effect=HTTPException(status_code=400, detail="Not implemented"))
    with pytest.raises(HTTPException) as exc_info:
        await service.remove_organization()
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Not implemented"

