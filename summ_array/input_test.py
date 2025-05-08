from unittest.mock import MagicMock
from main import 
def test_multiple_inputs_with_mock(monkeypatch):
    mock_input = MagicMock(side_effect=["Alice", "25"])
