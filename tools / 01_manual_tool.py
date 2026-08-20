# Из каких частей соcтоит TOOL, которая понятна ЛЛМ
#
# Tool(
#     name,
#     description,
#     function,
#     inputs,
#     output
# )

calculator_tool = Tool(
    "calculator",                   # name
    "Multiply two integers.",       # description
    calculator,                     # function to call
    [("a", "int"), ("b", "int")],   # input data: names and types
    "int",                          # output type
)


#Tool — создаёт инструмент для агента. ! Кокретно тут ручная настройка !

#1. "calculator"
#   → имя инструмента

#2. "Multiply two integers."
#   → объясняет агенту, что делает инструмент

#3. calculator
#   → функция, которую нужно запустить

#4. [("a", "int"), ("b", "int")]
#   → какие данные функция принимает

#5. "int"
#   → какой тип данных она возвращает
