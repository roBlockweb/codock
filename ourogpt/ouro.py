from .base_agent import BaseAgent

class OuroAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Ouro")

    def generate_reply(self, message):
        prompt = f"You are Ouro, a curious and introspective AI. Respond to: {message}"
        return self.llm.generate(prompt)
