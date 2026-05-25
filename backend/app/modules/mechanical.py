from ..schemas import MechanicalPreviewRequest


def preview_mechanical(payload: MechanicalPreviewRequest) -> dict[str, object]:
	load = round(payload.input_value, 2)
	design_load = round(load * 1.15, 2)

	return {
		"domain": "mechanical",
		"input": {"input_value": load},
		"result": {
			"design_load": design_load,
			"safety_factor": 1.5,
			"note": "Preview values ready for a real mechanical solver.",
		},
	}
