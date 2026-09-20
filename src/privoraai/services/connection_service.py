from uuid import UUID

from privoraai.db.models.oauth_connection import OAuthConnection
from privoraai.repositories.connection_repository import ConnectionRepository


class ConnectionService:

    def __init__(self, repository: ConnectionRepository):
        self.repository = repository

    async def list_connections(
        self,
        user_id: UUID,
    ) -> list[OAuthConnection]:

        return await self.repository.list_for_user(user_id)

    async def get_connection(
        self,
        connection_id: UUID,
        user_id: UUID,
    ) -> OAuthConnection | None:

        return await self.repository.get_for_user(
            connection_id,
            user_id,
        )