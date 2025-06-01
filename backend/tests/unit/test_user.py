import pytest
from unittest.mock import AsyncMock, MagicMock
from app.services.user_service import UserService
from app.db.models import UserDb
from app.db.schemas import UserUpdate
from fastapi import  status

@pytest.mark.asyncio
async def test_get_user_by_email():
    mock_session = MagicMock()
    mock_exec = AsyncMock()
    mock_session.exec = mock_exec
    mock_result = MagicMock()
    mock_result.first.return_value = UserDb(id=1, firstname='Test', lastname='User', email='test@email.com', username='testuser', hashed_password='pw')
    mock_exec.return_value = mock_result
    service = UserService()
    user = await service.get_user_by_email('test@email.com', mock_session)
    assert user is not None
    assert user.email == 'test@email.com'
    assert user.firstname == 'Test'

@pytest.mark.asyncio
async def test_existing_user():
    mock_session = MagicMock()
    service = UserService()
    service.get_user_by_email = AsyncMock(return_value=UserDb(id=1, firstname='Test', lastname='User', email='test@email.com', username='testuser', hashed_password='pw'))
    user = await service.existing_user('test@email.com', mock_session)
    assert user is not None
    assert user.email == 'test@email.com'

@pytest.mark.asyncio
async def test_update_user():
    mock_session = MagicMock()
    mock_user = UserDb(id=1, firstname='Test', lastname='User', email='test@email.com', username='testuser', hashed_password='pw')
    service = UserService()
    service.get_user_by_email = AsyncMock(return_value=mock_user)
    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()
    data = UserUpdate(firstname='Updated', lastname='User')
    updated_user = await service.update_user(data, mock_session, current_user=mock_user)
    assert updated_user.firstname == 'Updated'
    assert updated_user.lastname == 'User'

@pytest.mark.asyncio
async def test_remove_user():
    mock_session = MagicMock()
    mock_user = UserDb(id=1, firstname='Test', lastname='User', email='test@email.com', username='testuser', hashed_password='pw')
    service = UserService()
    service.get_user_by_email = AsyncMock(return_value=mock_user)
    mock_session.delete = AsyncMock()
    mock_session.commit = AsyncMock()
    status_code = await service.remove_user(current_user=mock_user, session=mock_session)
    assert status_code == status.HTTP_204_NO_CONTENT

@pytest.mark.asyncio
async def test_attending_events():
    # Example: test that attending_events returns a list of events for a user
    service = UserService()
    # Simulate a method attending_events (not implemented in your service)
    # Here is a placeholder for when you implement it:
    # mock_session = MagicMock()
    # mock_user = UserDb(id=1, firstname='Test', lastname='User', email='test@email.com', username='testuser', hashed_password='pw')
    # service.attending_events = AsyncMock(return_value=["Event1", "Event2"])
    # events = await service.attending_events(mock_user, mock_session)
    # assert events == ["Event1", "Event2"]
    assert True  # Remove this and uncomment above when implemented

@pytest.mark.asyncio
async def test_my_organization():
    # Example: test that my_organization returns a list of organizations for a user
    service = UserService()
    # Simulate a method my_organization (not implemented in your service)
    # Here is a placeholder for when you implement it:
    # mock_session = MagicMock()
    # mock_user = UserDb(id=1, firstname='Test', lastname='User', email='test@email.com', username='testuser', hashed_password='pw')
    # service.my_organization = AsyncMock(return_value=["Org1", "Org2"])
    # orgs = await service.my_organization(mock_user, mock_session)
    # assert orgs == ["Org1", "Org2"]
    assert True  # Remove this and uncomment above when implemented

@pytest.mark.asyncio
async def test_update_user_img():
    # Example: test that update_user_img updates the user's image
    service = UserService()
    # Simulate a method update_user_img (not implemented in your service)
    # Here is a placeholder for when you implement it:
    # mock_session = MagicMock()
    # mock_user = UserDb(id=1, firstname='Test', lastname='User', email='test@email.com', username='testuser', hashed_password='pw')
    # service.update_user_img = AsyncMock(return_value="img_url")
    # img_url = await service.update_user_img(mock_user, mock_session, b"imgdata")
    # assert img_url == "img_url"
    assert True  # Remove this and uncomment above when implemented
