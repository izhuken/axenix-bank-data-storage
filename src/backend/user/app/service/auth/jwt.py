from datetime import datetime, timezone

from core.config import ACCESS_EXPIRES_TIME, ALGORITHM, REFRESH_EXPIRES_TIME, SECRET_KEY
from dto.exception_dto import ErrorDTO
from dto.success_dto import SuccessDTO
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTClaimsError, JWTError

from app.schemas.auth import TokenDecode, TokenPair, TokenPayload
from app.schemas.response import ErrorResponse

OAUTH2_SCHEMA = OAuth2PasswordBearer(tokenUrl="token")

class JWTAuth:
    access_type = "access"
    refresh_type = "refresh"
    
    def _create_access_token(self, data: TokenPayload):
        expire = datetime.now(timezone.utc) + ACCESS_EXPIRES_TIME
        token_payload = {
            "exp": expire,
            "sub": str(data.id),
            "type": self.access_type,
        }
        return jwt.encode(token_payload, SECRET_KEY, ALGORITHM)

    def _create_refresh_token(self, data: TokenPayload):
        expire = datetime.now(timezone.utc) + REFRESH_EXPIRES_TIME
        token_payload = {
            "exp": expire,
            "sub": str(data.id),
            "type": self.refresh_type,
        }
        return jwt.encode(token_payload, SECRET_KEY, ALGORITHM)


    def decode_token(self, token: str):
        try:
            return SuccessDTO[TokenDecode](jwt.decode(token, SECRET_KEY, ALGORITHM))
        except JWTClaimsError:
            return ErrorDTO[ErrorResponse](status_code=401, detail="Any claim is invalid in any way.")
        except ExpiredSignatureError:
            return ErrorDTO[ErrorResponse](status_code=401, detail="The signature has expired.")
        except JWTError:
            return ErrorDTO[ErrorResponse](status_code=401, detail="The signature is invalid in any way.")

    def create_token_pair(self, data: TokenPayload):
        return TokenPair(
            refresh=self._create_refresh_token(data),
            access=self._create_access_token(data),
        )
        