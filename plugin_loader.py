# ==========================
# DEEK AI PLUGIN LOADER
# ==========================

import os
import importlib


def load_tools():

    tools = {}

    current_dir = os.path.dirname(__file__)

    for filename in os.listdir(current_dir):

        if (
            filename.endswith("_tool.py")
            and filename != "plugin_loader.py"
        ):

            module_name = filename[:-3]

            module = importlib.import_module(module_name)

            function_name = module_name

            if hasattr(module, function_name):

                tool_name = module_name.replace("_tool", "").upper()

                tools[tool_name] = getattr(
                    module,
                    function_name
                )

    return tools
