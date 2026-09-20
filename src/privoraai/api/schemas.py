from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    status: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    email: str


class ConnectionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    provider: str
    status: str
    provider_account_id: str | None
    provider_workspace_id: str | None
    scopes: list[str]
    created_at: datetime
    updated_at: datetime