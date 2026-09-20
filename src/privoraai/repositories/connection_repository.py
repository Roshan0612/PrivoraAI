from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from privoraai.db.models.oauth_connection import OAuthConnection


class ConnectionRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_for_user(
        self,
        user_id: UUID,
    ) -> list[OAuthConnection]:

        result = await self.db.execute(
            select(OAuthConnection)
            .where(OAuthConnection.user_id == user_id)
            .order_by(OAuthConnection.created_at.desc())
        )

        return list(result.scalars().all())

    async def get_for_user(
        self,
        connection_id: UUID,
        user_id: UUID,
    ) -> OAuthConnection | None:

        result = await self.db.execute(
            select(OAuthConnection)
            .where(
                OAuthConnection.id == connection_id,
                OAuthConnection.user_id == user_id,
            )
        )

        return result.scalar_one_or_none()