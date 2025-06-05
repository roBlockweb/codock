import abc
from .llm_wrapper import LLMWrapper
from .utils import load_faiss, search_index, add_texts_to_index, save_faiss
from .cache_manager import CacheManager
from .queue_manager import QueueManager
from .db_manager import DBManager

class BaseAgent(abc.ABC):
    def __init__(self, name):
        self.name = name
        self.llm = LLMWrapper()
        self.index = load_faiss()
        self.cache = CacheManager()
        self.queue = QueueManager()
        self.db = DBManager()

    def remember(self, text):
        add_texts_to_index([text], self.index)
        save_faiss(self.index)
        self.db.save_message(self.name, text)

    def recall(self, query, k=3):
        ids = search_index(query, self.index, k)
        return ids

    @abc.abstractmethod
    def generate_reply(self, message):
        pass

    def handle_message(self, message):
        cached = self.cache.get(message)
        if cached:
            reply = cached
        else:
            reply = self.generate_reply(message)
            self.cache.set(message, reply)
        self.remember(reply)
        return reply
