import flask
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.habit import Habit  # noqa: E501
from openapi_server.models.habit_create import HabitCreate  # noqa: E501
from openapi_server.models.habit_update import HabitUpdate  # noqa: E501
from openapi_server import util


def create_habit(body):  # noqa: E501
    """Создать новую привычку

     # noqa: E501

    :param habit_create: 
    :type habit_create: dict | bytes

    :rtype: Union[Habit, Tuple[Habit, int], Tuple[Habit, int, Dict[str, str]]
    """
    habit_create = body
    if flask.request.is_json:
        habit_create = HabitCreate.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_habit(habit_id):  # noqa: E501
    """Удалить привычку

     # noqa: E501

    :param habit_id: Идентификатор привычки
    :type habit_id: str
    :type habit_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_habit(habit_id):  # noqa: E501
    """Получить одну привычку по id

     # noqa: E501

    :param habit_id: Идентификатор привычки
    :type habit_id: str
    :type habit_id: str

    :rtype: Union[Habit, Tuple[Habit, int], Tuple[Habit, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_habits(archived=None, limit=None, offset=None):  # noqa: E501
    """Получить список своих привычек

     # noqa: E501

    :param archived: Фильтр по архивным привычкам (по умолчанию false)
    :type archived: bool
    :param limit: Сколько записей вернуть
    :type limit: int
    :param offset: Сколько записей пропустить
    :type offset: int

    :rtype: Union[List[Habit], Tuple[List[Habit], int], Tuple[List[Habit], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_habit(habit_id, body):  # noqa: E501
    """Изменить привычку (название, описание, периодичность, архив)

     # noqa: E501

    :param habit_id: Идентификатор привычки
    :type habit_id: str
    :type habit_id: str
    :param habit_update: 
    :type habit_update: dict | bytes

    :rtype: Union[Habit, Tuple[Habit, int], Tuple[Habit, int, Dict[str, str]]
    """
    habit_update = body
    if flask.request.is_json:
        habit_update = HabitUpdate.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'
