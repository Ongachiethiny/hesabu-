from fastapi import APIRouter

router = APIRouter()


@router.get("/preview")
def preview_thermo(temperature_c: float = 20.0):
    # placeholder: compute Kelvin and return a simple metric
    kelvin = temperature_c + 273.15
    return {"domain": "thermodynamics", "temperature_c": temperature_c, "kelvin": kelvin}
