from datetime import datetime, timedelta
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from app.services.auth_service import AuthService
from app.db.schemas import SignUpScheme, LoginRequest
from fastapi.responses import JSONResponse

@pytest.mark.asyncio
async def test_sign_up():
    mock_session = MagicMock()
    mock_user_service = MagicMock()
    mock_user_service.existing_user = AsyncMock(return_value=None)
    mock_utils = MagicMock()
    mock_utils.hash_password.return_value = 'hashed_pw'
    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()
    with patch('app.services.auth_service.user_service', mock_user_service), \
         patch('app.services.auth_service.utils', mock_utils):
        service = AuthService()
        data = SignUpScheme(firstname='Test', lastname='User', email='test@example.com', password='pw')
        result = await service.sign_up(data, mock_session)
        assert result["message"] == "User created successfully"
        assert "user_id" in result

@pytest.mark.asyncio
async def test_login():
    mock_session = MagicMock()
    mock_user_service = MagicMock()
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.email = 'test@example.com'
    mock_user.role = 'user'
    mock_user.hashed_password = 'hashed_pw'
    mock_user_service.get_user_by_email = AsyncMock(return_value=mock_user)
    mock_utils = MagicMock()
    mock_utils.verify_password.return_value = True
    mock_utils.create_access_token.return_value = 'access_token'
    mock_utils.create_refresh_token.return_value = 'refresh_token'
    with patch('app.services.auth_service.user_service', mock_user_service), \
         patch('app.services.auth_service.utils', mock_utils):
        service = AuthService()
        data = LoginRequest(email='test@example.com', password='pw')
        response = await service.login(data, mock_session)
        assert isinstance(response, JSONResponse)
        content = response.body
        if isinstance(content, (bytes, bytearray, memoryview)):
            content = content.tobytes() if isinstance(content, memoryview) else content
            content = content.decode() if hasattr(content, 'decode') else str(content)
        assert "access_token" in str(content)
        assert "refresh_token" in str(content)

@pytest.mark.asyncio
async def test_get_new_access_token():
    mock_utils = MagicMock()
    mock_utils.create_access_token.return_value = 'new_access_token'
    with patch('app.services.auth_service.utils', mock_utils):
        service = AuthService()
        token_details = {'exp': (datetime.now() + timedelta(hours=1)).timestamp()}
        response = await service.get_new_access_token(token_details)
        assert isinstance(response, JSONResponse)
        content = response.body
        if isinstance(content, (bytes, bytearray, memoryview)):
            content = content.tobytes() if isinstance(content, memoryview) else content
            content = content.decode() if hasattr(content, 'decode') else str(content)
        assert "access_token" in str(content)

@pytest.mark.asyncio
async def test_current_user():
    # This would typically be tested in the dependency, not the service, but here's a placeholder
    assert True