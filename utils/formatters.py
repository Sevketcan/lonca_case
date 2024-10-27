def capitalize_name(name: str) -> str:
    return name.capitalize() if name else ""

def format_currency(value: float, currency: str = "USD") -> str:
    return f"{currency} {value:,.2f}"
