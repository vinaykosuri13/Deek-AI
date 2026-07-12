# ==========================
# DEEK AI TEST SUITE
# ==========================

import importlib

MODULES = [
    "planner",
    "controller",
    "tool_manager",
    "request",
    "response",
    "search_tool",
    "chat_tool",
    "memory_tool",
    "memory_search_tool",
]

print("=" * 40)
print("      DEEK AI TEST SUITE")
print("=" * 40)

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

print("=" * 40)
print(f"Passed: {passed}/{len(MODULES)}")
print("=" * 40)
