from urls import Urls
import requests
import allure
from data import Plans

class TestPlans:
    @allure.title("Успешное получение данных о тарифах при передаче в тело запроса обязательных параметров")
    @allure.description("Передаем обязательный параметр account_id  в тело запроса")
    def test_get_plans_with_valid_account_id(self):
        response = requests.get(Urls.GET_PLANS, data={"account_id": Plans.account_id_valid})
        response_data = response.json()
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200

        with allure.step('Проверяем структуру JSON-ответа'):
            assert ('id' in response_data['plans'][1]
                and 'name' in response_data['plans'][1]
                and 'description' in response_data['plans'][1])

        with allure.step('Проверяем тип данных'):
            assert isinstance(response_data['plans'][1]['id'], int)
            assert isinstance(response_data['plans'][1]['name'], str)
            assert isinstance(response_data['plans'][1]['description'], str) or response_data['plans'][1]['description'] is None

        with allure.step('Проверяем корректность данных'):
            assert (response_data['plans'][1]['booking_guarantee_sum'] == Plans.booking_guarantee_sum
                and response_data['plans'][1]['booking_guarantee_unit'] == Plans.booking_guarantee_unit)

        with allure.step('Проверяем правила отмены'):
            assert (response_data['plans'][1]['cancellation_rules'] == Plans.cancellation_rules
                and response_data['plans'][1]['cancellation_deadline'] == Plans.cancellation_deadline)

    @allure.title('Полечение ошибки при невалидном параметре account_id')
    @allure.description('Передаем невалидный обязательный параметр account_id в тело запроса')
    def test_get_room_category_invalid_account_id(self):
        response = requests.get(Urls.GET_PLANS, data={"account_id": Plans.account_id_invalid})
        with allure.step('Проверяем код ошибки'):
            assert response.status_code == 404

    @allure.title("Получение ошибки при отсутствии обязательного параметра в теле запроса ")
    @allure.description("Не передаем в теле запроса параметр account_id")
    def test_get_plans_without_account_id(self):
        response = requests.get(Urls.GET_PLANS)
        with allure.step('Проверяем код ошибки'):
            assert response.status_code == 400


