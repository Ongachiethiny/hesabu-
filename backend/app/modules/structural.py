from ..schemas import StructuralPreviewRequest


def preview_structural(payload: StructuralPreviewRequest) -> dict[str, object]:
	load_case = payload.load_case.strip()
	severity_index = round(len(load_case) * 1.75, 2)

	return {
		"domain": "structural",
		"input": {"load_case": load_case},
		"result": {
			"severity_index": severity_index,
			"classification": "Needs review" if severity_index > 20 else "Nominal",
			"note": "Preview values ready for a real structural solver.",
		},
	}
