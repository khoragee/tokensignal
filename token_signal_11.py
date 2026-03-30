# v0.1.0
# { "Depends": "py-genlayer:latest" }

from genlayer import *
import json
import typing


class TokenSignalContract(gl.Contract):
    last_token: str
    last_signal: str
    last_confidence: str
    last_reason: str

    def __init__(self):
        self.last_token = "none"
        self.last_signal = "none"
        self.last_confidence = "none"
        self.last_reason = "none"

    @gl.public.write
    def get_signal(self, token: str) -> typing.Any:
        token_upper = token.upper().strip()

        def analyze() -> typing.Any:
            task = f"""You are a crypto market analyst. Give a short-term trading signal for {token_upper}.

You MUST respond with ONLY one of these three exact strings:
BUY
HOLD
SELL

Do not write anything else. Just the single word.
"""
            result = gl.nondet.exec_prompt(task)
            result = result.strip().upper()
            if "BUY" in result:
                return "BUY"
            elif "SELL" in result:
                return "SELL"
            else:
                return "HOLD"

        final = gl.eq_principle.strict_eq(analyze)

        sig = final.strip().upper()
        if sig not in ("BUY", "HOLD", "SELL"):
            sig = "HOLD"

        self.last_token = token_upper
        self.last_signal = sig
        self.last_confidence = "MEDIUM"
        self.last_reason = "AI consensus signal"

        return {"token": token_upper, "signal": sig}

    @gl.public.view
    def get_last_signal(self) -> dict:
        return {
            "token": self.last_token,
            "signal": self.last_signal,
            "confidence": self.last_confidence,
            "reason": self.last_reason,
        }
