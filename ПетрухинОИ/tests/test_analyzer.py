import pytest

from text_analyzer import analyze_text, normalize_text


def test_normalize_text():
    assert normalize_text("  hello  ") == "hello"


def test_analyze_text_basic():
    result = analyze_text("Hello world hello")

    assert result["characters"] == 17
    assert result["words"] == 3
    assert result["unique_words"] == 2
    assert result["top_words"][0] == ("hello", 2)


def test_analyze_text_handles_punctuation():
    result = analyze_text("Hello, hello! Python.")

    assert result["words"] == 3
    assert result["unique_words"] == 2


def test_analyze_text_empty():
    with pytest.raises(ValueError):
        analyze_text("")


def test_normalize_text_wrong_type():
    with pytest.raises(TypeError):
        normalize_text(123)
