class Config:
    # paths
    MODEL_PATH = "./models/mistral-7b"
    FAISS_PATH = "./faiss_index"
    DB_PATH = "./ouro.db"
    LOG_PATH = "./logs/ourogpt.log"

    # redis
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379

    # rabbitmq
    RABBIT_HOST = "localhost"
    RABBIT_PORT = 5672
    QUEUE_NAME = "ouro_queue"

    # other
    USER_AGENT = "OuroGPT/0.1"
