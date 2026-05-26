from hesabu_engine.app.routers import thermodynamics


def test_preview_thermo_defaults():
    out = thermodynamics.preview_thermo()
    assert "kelvin" in out
    assert out["temperature_c"] == 20.0
