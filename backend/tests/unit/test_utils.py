import datetime
import pytest
from app.core.utils import Utils
import jwt

def test_hash_and_verify_password():
    utils = Utils()
    password = "mysecretpassword"
    hashed = utils.hash_password(password)
    assert utils.verify_password(password, hashed)
    assert not utils.verify_password("wrongpassword", hashed)

def test_create_and_decode_access_token():
    utils = Utils()
    user_data = {"sub": "user@example.com", "user_id": 1, "role": "user"}
    token = utils.create_access_token(user_data)
    decoded = utils.decode_token(token)
    assert decoded["sub"] == "user@example.com"
    assert decoded["role"] == "user"
    assert decoded["refresh"] is False

def test_create_and_decode_refresh_token():
    utils = Utils()
    user_data = {"sub": "user@example.com", "user_id": 1, "role": "user"}
    token = utils.create_refresh_token(user_data)
    decoded = utils.decode_token(token)
    assert decoded["sub"] == "user@example.com"
    assert decoded["refresh"] is True

def test_decode_token_expired():
    utils = Utils()
    # Create a token that is already expired
    expired_payload = {"sub": "user@example.com", "exp": datetime.datetime.now().timestamp() - 100, "refresh": False}
    token = jwt.encode(expired_payload, utils.secret_key, algorithm=utils.algorithm)
    with pytest.raises(ValueError, match="Token has expired"):
        utils.decode_token(token)

def test_decode_token_invalid():
    utils = Utils()
    with pytest.raises(ValueError, match="Invalid token"):
        utils.decode_token("notavalidtoken")
