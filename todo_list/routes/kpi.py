from fastapi import APIRouter, Depends

from todo_list.controllers.kpi import KpiController
from todo_list.dependencies import get_kpi_controller

router = APIRouter(
    prefix="/kpi",
    tags=["kpi"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def get_users_kpi(*, kpi_controller: KpiController = Depends(get_kpi_controller)):
    return kpi_controller.get_users_kpi()
