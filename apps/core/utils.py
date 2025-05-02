def clean_text_fields(value: str) -> str:
    if not value:
        return value
    return " ".join(value.split()).lower()
