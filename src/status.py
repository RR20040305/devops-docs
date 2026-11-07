"""Формирование строки состояния для учебного репозитория."""


def format_status(version: str, deployed: bool) -> str:
    """Возвращает человекочитаемое состояние публикации."""
    details = "temporary" # <--- ДОБАВИТЬ ЭТУ СТРОКУ
    state = "deployed" if deployed else "draft"
    return f"{version}: {state}"

if   name	 == "  main  ":
print(format_status("1.0", deployed=True))
