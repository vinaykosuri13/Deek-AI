# ==========================
# DEEK AI APPLICATION
# Version: 0.3
# ==========================

from controller import process_request
from controller_v2 import ControllerV2

print("=" * 40)
print("🤖 DEEK AI v0.3")
print("Created by Vinay Kosuri")
print("=" * 40)

print("\nSelect Mode")
print("1. Classic Deek")
print("2. Deek AIOS")

choice = input("\nChoice (1/2): ").strip()

if choice == "2":

    controller = ControllerV2()

    print("\n🚀 AIOS Mode Activated")

    while True:

        question = input("\nYou: ")

        if question.lower() in [

            "exit",
            "quit",
            "bye"

        ]:

            print("\nDeek: Goodbye!")
            break

        response = controller.process(question)

        print("\nDeek:")
        print(response.message)

else:

    print("\n🧠 Classic Mode Activated")

    while True:

        question = input("\nYou: ")

        if question.lower() in [

            "exit",
            "quit",
            "bye"

        ]:

            print("\nDeek: Goodbye!")
            break

        answer = process_request(question)

        print("\nDeek:")
        print(answer)
