import configuration
import data
import requests

header = {
    "Content-Type": "application/json"
}


# создание нового заказа
def create_new_order():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        headers=header,
        json=data.create_order,
    )


# получение данных о заказе по его треку
def get_info_order(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + str(track_id))
