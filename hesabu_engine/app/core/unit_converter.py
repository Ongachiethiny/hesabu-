"""Small collection of unit conversion helpers."""

def kg_to_lb(kg: float) -> float:
    return kg * 2.2046226218


def lb_to_kg(lb: float) -> float:
    return lb / 2.2046226218


def m_to_ft(m: float) -> float:
    return m * 3.280839895


def ft_to_m(ft: float) -> float:
    return ft / 3.280839895
