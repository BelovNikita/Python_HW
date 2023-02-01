# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования.

def calc(action, kind):
    data = action.split()
    sign = data[1]

    if kind == "2":
        if sign == "+":
            answer = float(data[0]) + float(data[2])
        elif sign == "-":
            answer = float(data[0]) - float(data[2])
        elif sign == "*":
            answer = float(data[0]) * float(data[2])
        elif sign == "/":
            if data[2] == "0":
                answer = "division for zero"
            else:
                answer = float(data[0]) / float(data[2])
        else:
            answer = "Something unexpected happened"

    elif kind == "1":
        first_num = data[0]
        first_num_new = first_num.split(",")
        second_num = data[2]
        second_num_new = second_num.split(",")
        first_num_complex = complex(float(first_num_new[0]), float(first_num_new[1]))
        second_num_complex = complex(float(second_num_new[0]), float(second_num_new[1]))
        if sign == "+":
            answer = first_num_complex + second_num_complex
        elif sign == "-":
            answer = first_num_complex - second_num_complex
        elif sign == "*":
            answer = first_num_complex * second_num_complex
        elif sign == "/":
            answer = first_num_complex / second_num_complex


    return answer