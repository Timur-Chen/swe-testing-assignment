from quick_calc.app import QuickCalcApp


def press_sequence(app, keys):
    result = ""
    for key in keys:
        result = app.press(key)
    return result


def test_full_addition_flow():
    app = QuickCalcApp()
    result = press_sequence(app, ["5", "+", "3", "="])
    assert result == "8"


def test_clear_resets_display():
    app = QuickCalcApp()
    press_sequence(app, ["9", "*", "2", "="])
    result = app.press("C")
    assert result == "0"