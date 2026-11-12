import unittest

from flask import json

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.habit import Habit  # noqa: E501
from openapi_server.models.habit_create import HabitCreate  # noqa: E501
from openapi_server.models.habit_update import HabitUpdate  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHabitsController(BaseTestCase):
    """HabitsController integration test stubs"""

    def test_create_habit(self):
        """Test case for create_habit

        Создать новую привычку
        """
        habit_create = {"title":"Пить воду","description":"2 литра в день","frequency":"daily"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/habits',
            method='POST',
            headers=headers,
            data=json.dumps(habit_create),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_habit(self):
        """Test case for delete_habit

        Удалить привычку
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/habits/{habit_id}'.format(habit_id=UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d')),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_habit(self):
        """Test case for get_habit

        Получить одну привычку по id
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/habits/{habit_id}'.format(habit_id=UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d')),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_habits(self):
        """Test case for list_habits

        Получить список своих привычек
        """
        query_string = [('archived', False),
                        ('limit', 20),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/habits',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_habit(self):
        """Test case for update_habit

        Изменить привычку (название, описание, периодичность, архив)
        """
        habit_update = {"title":"title","description":"description","frequency":"daily","archived":True}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v1/habits/{habit_id}'.format(habit_id=UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d')),
            method='PATCH',
            headers=headers,
            data=json.dumps(habit_update),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
