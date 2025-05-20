import pytest

from urls import Urls
import requests
import allure
from data import RoomCategory


class TestRoomCategory:
    @allure.title("Успешное получение данных о номере при передаче в тело запроса обязательных параметров")
    @allure.description("Передаем обязательный параметр account_id  в тело запроса")
    def test_get_room_category_account_id_only(self):
        response = requests.get(Urls.GET_ROOMS_INFO, data={"account_id": RoomCategory.account_id_valid})
        response_data = response.json()
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200

        with allure.step('Проверяем структуру JSON-ответа'):
             assert ("id" in response_data['rooms'][0]
                and 'name' in response_data['rooms'][0]
                and "description" in response_data['rooms'][0])

        with allure.step('Проверяем тип данных'):
            assert isinstance(response_data['rooms'][0]['id'],int)
            assert isinstance(response_data['rooms'][0]['name'],str)
            assert isinstance(response_data['rooms'][0]['description'],str)

        with allure.step('Проверяем корректность данных'):
            assert (response_data['rooms'][0]['adults'] == RoomCategory.adults
                and response_data['rooms'][0]['children'] == RoomCategory.children)

    @allure.title("Успешное получение данных о номере при передаче всех параметров в тело запроса")
    @allure.description("Передаем в тело запроса параметр address_included со значениями 1 и 0 поочередно")
    @pytest.mark.parametrize('address_included', [1, 0])
    def test_get_room_category_address_included(self, address_included):
        response = requests.get(Urls.GET_ROOMS_INFO, data={"account_id": RoomCategory.account_id_valid,
                                                           "address_included": address_included})
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200

    @allure.title('Проверка локализации параметра ответа "name"')
    def test_get_room_category_check_localisation(self):
        response = requests.get(Urls.GET_ROOMS_INFO, data={"account_id": RoomCategory.account_id_valid})
        response_data = response.json()
        with allure.step('Проверяем корректность локализации параметра ответа "name"'):
            assert response_data['rooms'][0]['name_ru'] == RoomCategory.name_ru
            assert response_data['rooms'][0]['name_en'] == RoomCategory.name_en
            assert response_data['rooms'][0]['name_de'] == RoomCategory.name_de
            assert response_data['rooms'][0]['name_zh'] == RoomCategory.name_zh
            assert response_data['rooms'][0]['name_es'] == RoomCategory.name_es
            assert response_data['rooms'][0]['name_fr'] == RoomCategory.name_fr
            assert response_data['rooms'][0]['name_ja'] == RoomCategory.name_ja
            assert response_data['rooms'][0]['name_it'] == RoomCategory.name_it
            assert response_data['rooms'][0]['name_ko'] == RoomCategory.name_ko
            assert response_data['rooms'][0]['name_pl'] == RoomCategory.name_pl
            assert response_data['rooms'][0]['name_fi'] == RoomCategory.name_fi
            assert response_data['rooms'][0]['name_lt'] == RoomCategory.name_lt
            assert response_data['rooms'][0]['name_ro'] == RoomCategory.name_ro
            assert response_data['rooms'][0]['name_lv'] == RoomCategory.name_lv
            assert response_data['rooms'][0]['name_uk'] == RoomCategory.name_uk

    @allure.title('Проверка успешного возвращения списка фотографий')
    @allure.description('Передаем индекс комнаты, в которой photos не None')
    def test_get_room_category_photos_not_null(self):
        response = requests.get(Urls.GET_ROOMS_INFO, data={"account_id": RoomCategory.account_id_valid})
        response_data = response.json()
        with allure.step('Проверяем, что возвращается не пустой список фотографий'):
           assert response_data['rooms'][6]['photos'] is not None


    @allure.title("Получение ошибки при отсутствии обязательного параметра в теле запроса ")
    @allure.description("Не передаем в теле запроса параметр account_id")
    def test_get_room_category_without_account_id(self):
        response = requests.get(Urls.GET_ROOMS_INFO)
        with allure.step('Проверяем код ошибки'):
            assert response.status_code == 400

    @allure.title('Получение ошибки при невалидном параметре account_id')
    @allure.description('Передаем невалидный обязательный параметр account_id в тело запроса')
    def test_get_room_category_invalid_account_id(self):
        response = requests.get(Urls.GET_ROOMS_INFO, data={"account_id": RoomCategory.account_id_invalid})
        with allure.step('Проверяем код ошибки'):
            assert response.status_code == 404





