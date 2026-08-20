from smolagents import tool


@tool
def calculator(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


print(calculator.to_string())


# @tool превращает обычную функцию в Tool в PYTHON.
#
# После этого calculator содержит информацию:
# - имя инструмента
# - описание
# - входные данные
# - тип результата
#
# to_string() показывает это описание в виде текста.
#
# Это описание нужно, чтобы LLM понимала,
# каким инструментом она может пользоваться.
