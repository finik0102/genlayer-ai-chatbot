# { "Depends": "py-genlayer:test" }
from genlayer import *
import json

class AIChatBot(gl.Contract):
    last_answer: str
    last_price: str
    history: DynArray[str]

    def __init__(self):
        self.last_answer = ""
        self.last_price = ""
        self.history = []

    @gl.public.write
    def ask_ai(self, user_query: str) -> None:
        result = gl.nondet.exec_prompt(user_query)
        self.last_answer = result
        self.history.append("Q: " + user_query + " | A: " + result)

    @gl.public.view
    def get_last_answer(self) -> str:
        return self.last_answer

    @gl.public.write
    def get_crypto_price(self, ticker: str) -> None:
        prompt = (
            "What is the current price of " + ticker + " in USD? "
            'Respond ONLY with JSON: {"price": "value"}'
        )
        result = gl.nondet.exec_prompt(prompt)
        try:
            parsed = json.loads(result)
            self.last_price = parsed.get("price", result)
        except Exception:
            self.last_price = result

    @gl.public.view
    def get_last_price(self) -> str:
        return self.last_price

    @gl.public.view
    def get_history(self) -> DynArray[str]:
        return self.history
