from hesabu_engine.app.core import unit_converter


def test_kg_to_lb_roundtrip():
    kg = 10.0
    lb = unit_converter.kg_to_lb(kg)
    assert round(unit_converter.lb_to_kg(lb), 6) == round(kg, 6)


def test_m_to_ft_roundtrip():
    m = 3.5
    ft = unit_converter.m_to_ft(m)
    assert round(unit_converter.ft_to_m(ft), 6) == round(m, 6)
