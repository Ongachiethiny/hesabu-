from ..schemas import ElectricalPreviewRequest


def preview_electrical(payload: ElectricalPreviewRequest) -> dict[str, object]:
	circuit_label = payload.circuit_label.strip()
	label_score = round(len(circuit_label) * 0.9, 2)

	return {
		"domain": "electrical",
		"input": {"circuit_label": circuit_label},
		"result": {
			"label_score": label_score,
			"status": "Ready for sizing",
			"note": "Preview values ready for a real electrical solver.",
		},
	}
