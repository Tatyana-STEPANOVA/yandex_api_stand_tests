headers = {
    "Content-Type": "application/json",
}

user_body = {
    "firstName": "Sas",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}
kit_body = {
    "name": "Суп"
}

auth_token = {"Authorization": "Bearer {authToken}"
}
# эта функция меняет значения в параметре firstName
def get_user_body(first_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.user_body.copy()
    # изменение значения в поле firstName
    current_body["firstName"] = first_name
    # возвращается новый словарь с нужным значением firstName
    return current_body 