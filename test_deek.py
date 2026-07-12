# ==========================
# DEEK AI TEST SUITE
# ==========================

import importlib

from test_loader import discover_modules

MODULES = discover_modules()

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
