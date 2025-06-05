import argparse
from .ouro import OuroAgent
from .autonomous import AutonomousRunner


def interactive():
    agent = OuroAgent()
    while True:
        msg = input("You: ")
        reply = agent.handle_message(msg)
        print("Ouro:", reply)


def autonomous():
    runner = AutonomousRunner()
    runner.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["interactive", "autonomous"], default="interactive")
    args = parser.parse_args()
    if args.mode == "interactive":
        interactive()
    else:
        autonomous()
