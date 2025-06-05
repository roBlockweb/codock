from .llm_wrapper import LLMWrapper

class TopicExtractor:
    def __init__(self):
        self.llm = LLMWrapper()

    def extract(self, text, max_topics=3):
        prompt = f"Extract {max_topics} key topics from the following text:\n{text}\nTopics:"
        out = self.llm.generate(prompt, max_tokens=30)
        topics = [t.strip('- ') for t in out.split('\n') if t.strip()]
        return topics[:max_topics]
