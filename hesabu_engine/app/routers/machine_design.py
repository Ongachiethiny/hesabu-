from fastapi import APIRouter

from ..core import unit_converter

router = APIRouter()


@router.get("/preview")
def preview_mechanical(value: float = 0.0):
    # simple preview: return converted units and a small sample derived value
    kg = value
    lb = round(unit_converter.kg_to_lb(kg), 4)
    sample_design = round(kg * 1.15, 4)
    return {"domain": "machine_design", "input_kg": kg, "input_lb": lb, "sample_design": sample_design}
