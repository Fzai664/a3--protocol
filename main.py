"""
A3 Protocol Demo
Autonomous AI Agent Accountability System
"""

from src.agent.agent import A3Agent
from src.accountability import Accountability
from src.verifier import Verifier


def main():

    agent = A3Agent("agent_001")

    context = {
        "market": "DeFi",
        "task": "risk analysis"
    }

    decision = agent.make_decision(context)

    verifier = Verifier()
    result = verifier.validate(decision)

    accountability = Accountability()

    record = accountability.create_record(
        agent.agent_id,
        decision
    )

    print("Decision:")
    print(decision)

    print("\nVerification:")
    print(result)

    print("\nAccountability Record:")
    print(record)


if __name__ == "__main__":
    main()