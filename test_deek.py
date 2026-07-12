

import importlib

MODULES = [
    "planner",
    "controller",
    "tool_manager",
    "request",
    "response",
    "intent",
    "search_tool",
    "chat_tool",
    "memory_tool",
    "memory_search_tool",
    "calculator_tool",
    "datetime_tool",
    "weather_service",
    "weather_tool",
    "planner_rules.calculator_rule",
    "planner_rules.memory_rule",
    "planner_rules.search_rule",
    "planner_rules.datetime_rule",
    "planner_rules.weather_rule",
]

print("=" * 45)
print("        DEEK AI TEST SUITE")
print("=" * 45)

passed = 0

for module_name in MODULES:

    try:
        module = importlib.import_module(module_name)
        importlib.reload(module)

        print(f"[PASS] {module_name}")
        passed += 1

    except Exception as e:
        print(f"[FAIL] {module_name}")
        print(e)

print("=" * 45)
print(f"Passed: {passed}/{len(MODULES)}")
print("=" * 45)
