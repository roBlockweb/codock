import time
from .ouro import OuroAgent
from .brain import BrainAgent
from .topic_extractor import TopicExtractor
from .utils import scrape

class AutonomousRunner:
    def __init__(self, sleep=1):
        self.ouro = OuroAgent()
        self.brain = BrainAgent()
        self.extractor = TopicExtractor()
        self.sleep = sleep

    def step(self, message):
        reply = self.brain.handle_message(message)
        topics = self.extractor.extract(reply)
        for t in topics:
            content = scrape(f"https://duckduckgo.com/?q={t}")
            if content:
                self.ouro.remember(content)
        response = self.ouro.handle_message(reply)
        return response

    def run(self, start="Hello"):
        message = start
        while True:
            message = self.step(message)
            time.sleep(self.sleep)
