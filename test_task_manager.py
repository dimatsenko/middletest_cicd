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
@pytest.mark.parametrize(
    "task_id, description, priority, created_at, is_done", [
        (1, "First task", 1, "2026-01-01 10:00:00", False),
        (2, "Second task", 2, "2026-01-02 11:00:00", True),
    ]
)
def test_task_to_from_dict(
        task_id,
        description,
        priority,
        created_at,
        is_done):
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


def test_add_task(empty_task_manager):
    """Test adding a task updates the in-memory list and the save file."""
    task_id = empty_task_manager.add_task("A new task", 1)

    assert task_id == 1
    assert len(empty_task_manager.tasks) == 1
    assert empty_task_manager.tasks[0].description == "A new task"

    # Ensure it's saved in the file
    assert os.path.exists(empty_task_manager.filename)
    with open(empty_task_manager.filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]['description'] == "A new task"


@pytest.mark.parametrize(
    "task_id_to_delete, expected_result, expected_count", [
        (1, True, 2),  # Deletes Task 1, leaves 2
        (2, True, 2),  # Deletes Task 2, leaves 2
        (999, False, 3),  # Not found, leaves 3
    ]
)
def test_delete_task(
        populated_task_manager,
        task_id_to_delete,
        expected_result,
        expected_count):
    """Test deleting tasks by various IDs."""
    result = populated_task_manager.delete_task(task_id_to_delete)

    assert result is expected_result
    assert len(populated_task_manager.tasks) == expected_count

    if expected_result:
        # Verify it was completely removed
        assert not any(
            t.task_id == task_id_to_delete
            for t in populated_task_manager.tasks
        )


def test_mark_completed(populated_task_manager):
    """Test marking a task as completed."""
    # Based on the implementation, mark_completed deletes the task after
    # saving it as completed.
    result = populated_task_manager.mark_completed(1)

    assert result is True
    assert len(populated_task_manager.tasks) == 2
    assert not any(t.task_id == 1 for t in populated_task_manager.tasks)


@pytest.mark.parametrize("sort_by, expected_id_order", [
    # Priorities are 1, 2, 3 -> corresponding IDs are 2, 3, 1
    ('priority', [2, 3, 1]),
    # Created sequentially -> corresponding IDs are 1, 2, 3
    ('created_at', [1, 2, 3]),
])
def test_get_sorted_tasks(populated_task_manager, sort_by, expected_id_order):
    """Test sorting tasks by priority or creation time."""
    sorted_tasks = populated_task_manager.get_sorted_tasks(sort_by=sort_by)
    actual_id_order = [t.task_id for t in sorted_tasks]

    assert actual_id_order == expected_id_order
