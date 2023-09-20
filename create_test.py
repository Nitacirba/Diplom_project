# Анастасия Шкиря, 08-а когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


# Создание автотеста

def test_create_get_track():
    j_body = sender_stand_request.create_new_order().json()  # создание заказа и конвертация ответа в формат json
    track_id = j_body['track']  # извлечение номера трека

    response = sender_stand_request.get_info_order(track_id)  # получаем данные о заказе по номеру трека

    assert response.status_code == 200  # проверка кода ответа
