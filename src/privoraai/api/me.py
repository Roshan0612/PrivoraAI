from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from privoraai.api.dependencies import get_db
from privoraai.api.schemas import UserResponse
from privoraai.db.models.user import User


router = APIRouter(
    prefix="/api/v1",
    tags=["Identity"],
)


@router.get("/me", response_model=UserResponse)
async def get_current_user(
    db: AsyncSession = Depends(get_db),
) -> User:

    result = await db.execute(
        select(User).limit(1)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user