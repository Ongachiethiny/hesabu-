from fastapi import APIRouter

router = APIRouter()


@router.get("/preview")
def preview_fluid(reynolds: float = 1e3):
    # placeholder: classify flow regime
    r = reynolds
    regime = "laminar" if r < 2300 else "transitional" if r < 4000 else "turbulent"
    return {"domain": "fluid_mechanics", "reynolds": r, "regime": regime}
