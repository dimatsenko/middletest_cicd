import pytest
import os
import json
from task import Task
from task_manager import TaskManager

@pytest.fixture
def temp_task_file(tmp_path):
    """фікстура для тимчасових файлів."""
    return str(tmp_path / "test_tasks.json")

@pytest.fixture
def empty_task_manager(temp_task_file):
    """фіктсура для таск менеджера пустого."""
    return TaskManager(filename=temp_task_file)

@pytest.fixture
def populated_task_manager(empty_task_manager):
    """фікстура для таскменеджера з заваннями ."""
    empty_task_manager.add_task("Task 1", 3)
    empty_task_manager.add_task("Task 2", 1)
    empty_task_manager.add_task("Task 3", 2)
    return empty_task_manager