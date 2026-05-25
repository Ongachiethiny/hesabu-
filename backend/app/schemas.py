from pydantic import BaseModel, Field


class MechanicalPreviewRequest(BaseModel):
	input_value: float = Field(..., ge=0)


class StructuralPreviewRequest(BaseModel):
	load_case: str = Field(..., min_length=1)


class ElectricalPreviewRequest(BaseModel):
	circuit_label: str = Field(..., min_length=1)
