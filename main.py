from src.verifier import Verifier


# Agent's predefined SLA
sla = {
    "max_trade_amount": 1000,
    "allowed_protocols": [
        "Jupiter",
        "Raydium"
    ],
    "max_slippage": 0.01,
    "max_leverage": 2
}


# Simulated agent action
action = {
    "agent": "Agent-001",
    "protocol": "Jupiter",
    "amount": 1500,
    "slippage": 0.005,
    "leverage": 1
}


verifier = Verifier(sla)

result = verifier.validate(action)

print("\n=== A3 Verification Result ===")
print(result)