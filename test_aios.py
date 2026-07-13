# ==========================
# DEEK AIOS TEST
# Phase 1
# ==========================

from controller_v2 import ControllerV2


def main():

    print("=" * 50)
    print("        DEEK AIOS TEST")
    print("=" * 50)

    controller = ControllerV2()

    while True:

        print()

        question = input("You: ")

        if question.lower() in [

            "exit",
            "quit",
            "bye"

        ]:

            print("\nGoodbye!")
            break

        response = controller.process(question)

        print()
        print("Deek:")
        print(response.message)

        print()
        print("-" * 50)
        print("Goal:")
        print(response.metadata.get("goal"))

        print()
        print("Confidence:")
        print(response.metadata.get("confidence"))

        print()
        print("Tools Used:")
        print(response.metadata.get("tools_used"))
        print("-" * 50)


if __name__ == "__main__":
    main()
