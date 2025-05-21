import pytest

from urls import Urls
import requests
import allure
from data import HotelInfo

class TestReceiveHotelInfo:
    @allure.title("Успешное получение мета-данных отеля")
    @allure.description("Передаем корректный uid в тело запроса")
    def test_get_hotel_data_with_valid_uid(self):
        response= requests.get(Urls.GET_HOTEL_INFO, data ={"uid":HotelInfo.hotel_uid_valid} )
        response_data = response.json()

        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200

        with allure.step('Проверяем структуры JSON-ответа'):
            assert ("name" in response_data['account']
                and "phone" in response_data['account']
                and "address" in response_data['account'])

        with allure.step('Проверяем тип данных'):
            assert isinstance(response_data['account']['name'], str)
            assert isinstance(response_data['account']['phone'], str)
            assert isinstance(response_data['account']['address'], str)

        with allure.step('Проверяем корректность данных'):
            assert (response_data['account']['name'] == HotelInfo.name
                and response_data['account']['phone'] == HotelInfo.phone
                and response_data['account']['address'] == HotelInfo.address)

        with allure.step('Проверяем значение поля hotel_type'):
            assert response_data['account']['hotel_type'] == HotelInfo.hotel_type


    @allure.title("Получение ошибки при передаче некорректного uid в тело запроса")
    @allure.description("Передаем некорректный uid в тело запроса")
    @pytest.mark.parametrize('uid_invalid',['','123','!!!','d7494710-8c8c-4c4c-bba4-f71caf96', 123])
    def test_get_hotel_data_with_invalid_uid(self, uid_invalid):
        response = requests.get(Urls.GET_HOTEL_INFO, data={"uid":uid_invalid})
        with allure.step('Проверяем код ошибки'):
            assert response.status_code == 404

    @allure.title('Получение ошибки при отсутствии обязательного параметра в теле запроса')
    @allure.description('Не передаем обязательный параметр uid в тело запроса')
    def test_get_hotel_data_without_uid(self):
        response = requests.get(Urls.GET_HOTEL_INFO)
        with allure.step('Проверяем код ошибки'):
            assert response.status_code == 400





#'id': 535, 'name': 'Отель «Вилла Олива» , API', 'phone': '+799955555', 'email': 'alena.s@bnovo.ru', 'address': 'Санкт-Петербург, Коломяжский пр-кт, 15, к 2',