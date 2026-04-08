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


# Parametrization for Task initialization and parsing
@pytest.mark.parametrize("task_id, description, priority, created_at, is_done", [
    (1, "First task", 1, "2026-01-01 10:00:00", False),
    (2, "Second task", 2, "2026-01-02 11:00:00", True),
])
def test_task_to_from_dict(task_id, description, priority, created_at, is_done):
    """Test stringification, serialization and deserialization of Task."""
    task = Task(task_id, description, priority, created_at, is_done)
    task_dict = task.to_dict()

    assert task_dict['id'] == task_id
    assert task_dict['description'] == description
    assert task_dict['priority'] == priority
    assert task_dict['created_at'] == created_at
    assert task_dict['is_done'] == is_done

    new_task = Task.from_dict(task_dict)
    assert new_task.task_id == task_id
    assert new_task.description == description
    assert new_task.priority == priority
    assert new_task.created_at == created_at
    assert new_task.is_done == is_done

