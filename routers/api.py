from fastapi import APIRouter, status, HTTPException, Query
from fastapi.responses import JSONResponse
from services.numbers import NumbersService

router = APIRouter(tags=["api"])
numbers_service = NumbersService()


@router.post("/extract/", status_code=status.HTTP_200_OK)
def extract_number(number: int = Query(..., ge=1, le=100)):
    try:
        numbers_service.extract(number)
        return JSONResponse(
            content={"message": f"Número {number} extraído exitosamente."},
            status_code=status.HTTP_200_OK,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/missing/", status_code=status.HTTP_200_OK)
def get_missing_number():
    if numbers_service.extracted_number is None:
        raise HTTPException(
            status_code=400, detail="No se ha extraído ningún número aún."
        )
    missing = numbers_service.find_missing_number()
    return JSONResponse(
        content={"numeros_faltantes": missing},
        status_code=status.HTTP_200_OK,
    )
