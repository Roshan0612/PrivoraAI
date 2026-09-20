from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from privoraai.api.dependencies import get_db
from privoraai.api.schemas import ConnectionResponse
from privoraai.repositories.connection_repository import ConnectionRepository
from privoraai.services.connection_service import ConnectionService


router = APIRouter(
    prefix="/api/v1/connections",
    tags=["Connections"],
)


def get_connection_service(
    db: AsyncSession = Depends(get_db),
) -> ConnectionService:

    repository = ConnectionRepository(db)

    return ConnectionService(repository)


@router.get(
    "",
    response_model=list[ConnectionResponse],
)
async def list_connections(
    service: ConnectionService = Depends(get_connection_service),
) -> list:

    # Temporary identity until Better Auth integration.
    user_id = UUID("00000000-0000-0000-0000-000000000000")

    return await service.list_connections(user_id)


@router.get(
    "/{connection_id}",
    response_model=ConnectionResponse,
)
async def get_connection(
    connection_id: UUID,
    service: ConnectionService = Depends(get_connection_service),
) -> ConnectionResponse:

    # Temporary identity until Better Auth integration.
    user_id = UUID("00000000-0000-0000-0000-000000000000")

    connection = await service.get_connection(
        connection_id,
        user_id,
    )

    if connection is None:
        raise HTTPException(
            status_code=404,
            detail="Connection not found",
        )

    return connection