# ==========================
# DEEK AI TEST LOADER
# ==========================

import os


EXCLUDE = {
    "app.py",
    "ai.py",
    "test_deek.py",
    "test_loader.py",
}


def discover_modules():

    modules = []

    # Root folder
    for filename in sorted(os.listdir(".")):

        if (
            filename.endswith(".py")
            and filename not in EXCLUDE
        ):

            modules.append(filename[:-3])

    # planner_rules
    if os.path.exists("planner_rules"):

        for filename in sorted(os.listdir("planner_rules")):

            if (
                filename.endswith(".py")
                and not filename.startswith("__")
            ):

                modules.append(
                    "planner_rules." + filename[:-3]
                )

    return modules
