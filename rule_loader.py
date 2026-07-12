# ==========================
# DEEK AI RULE LOADER
# ==========================

import os
import importlib


def load_rules():

    rules = []

    current_dir = os.path.join(
        os.path.dirname(__file__),
        "planner_rules"
    )

    for filename in sorted(os.listdir(current_dir)):

        if (
            filename.endswith("_rule.py")
            and not filename.startswith("__")
        ):

            module_name = filename[:-3]

            module = importlib.import_module(
                f"planner_rules.{module_name}"
            )

            if hasattr(module, "match"):

                rules.append(module.match)

    return rules
