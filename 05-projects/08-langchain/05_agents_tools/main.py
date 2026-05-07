# -*- coding: utf-8 -*-
import argparse
from agent import MultiToolAgent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stream", action="store_true", default=False)
    args = parser.parse_args()

    print("=" * 50)
    print("  Multi-function AI Assistant")
    print("=" * 50)
    print("Commands:")
    print("  /quit   - Exit")
    print("  /clear  - Clear history")
    print("=" * 50)

    agent = MultiToolAgent()

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            if user_input.startswith("/"):
                cmd = user_input.lower()
                if cmd == "/quit":
                    print("Goodbye!")
                    break
                elif cmd == "/clear":
                    print(agent.clear_history())
                continue

            response = agent.chat(user_input)
            print(f"AI: {response}\n")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
