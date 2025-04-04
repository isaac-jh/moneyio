from fastapi import APIRouter, Depends
# from utils.authentication import check_bearer_token

from routers import auth

router = APIRouter()

router.include_router(prefix="/auth", router=auth.router)
# router.include_router(sample_router.router, dependencies=[Depends(check_bearer_token)])
