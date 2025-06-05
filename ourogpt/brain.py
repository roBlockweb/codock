from .base_agent import BaseAgent

class BrainAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Brain")

    def generate_reply(self, message):
        prompt = f"You are Brain, an analytical AI. Respond logically to: {message}"
        return self.llm.generate(prompt)
