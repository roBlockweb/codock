# OuroGPT

Welcome to **OuroGPT**! This project contains two friendly AIs named **Ouro** and **Brain** that talk to each other, learn new things from the web and remember what they see. You can chat with them yourself or watch them chat on their own.

The code is written in Python. You do not need to know how to program to run it. Just follow the steps below exactly.

## 1. Install Python

You need Python 3.10 or newer. If you don't have it, download and install it from [python.org](https://www.python.org/downloads/).

## 2. Open a terminal

A *terminal* is a text window where you type commands. On Windows you can use "Command Prompt" or "PowerShell". On macOS or Linux open the "Terminal" app.

## 3. Get the code

Clone the project using `git`. If `git` is not installed, install it first from <https://git-scm.com/>.

```bash
git clone <THIS_REPOSITORY_URL>
cd codock
```

Replace `<THIS_REPOSITORY_URL>` with the address of this project.

## 4. Create a virtual environment (recommended)

A virtual environment keeps the Python packages for this project separate from the rest of your system. Run these commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

You should see `(venv)` in front of your terminal prompt after activating.

## 5. Install the required packages

Copy and paste the line below. It installs all libraries OuroGPT needs, such as the AI models and the tools for web scraping and caching.

```bash
pip install transformers torch sentence-transformers faiss-cpu requests beautifulsoup4 pika redis
```

## 6. (Optional) Start Redis and RabbitMQ

OuroGPT can use Redis for caching and RabbitMQ for messaging. If you have these installed, start them now. If you do not have them or do not want to set them up, you can skip this step—OuroGPT will still run but without caching and queues.

## 7. Initialize the memory index

Run this command once to create the FAISS index with some starter knowledge:

```bash
python -m ourogpt.initialize_faiss
```

You should see the message `FAISS initialized with starter content`.

## 8. Run OuroGPT

You can chat with Ouro directly or let Ouro and Brain talk to each other.

### Interactive mode

```bash
python -m ourogpt.main --mode interactive
```

Type a message and press Enter. Ouro will answer.

### Autonomous mode

```bash
python -m ourogpt.main --mode autonomous
```

Ouro and Brain will have an endless conversation, search the web for new topics and learn from what they find.

## 9. One-line setup and run

If you want to do everything at once, copy and paste this long command. It installs the packages, initializes the index and starts autonomous mode.

```bash
pip install transformers torch sentence-transformers faiss-cpu requests beautifulsoup4 pika redis && python -m ourogpt.initialize_faiss && python -m ourogpt.main --mode autonomous
```

That's it! Press `Ctrl+C` in the terminal to stop the program whenever you want.

Enjoy talking with OuroGPT! If anything goes wrong, check that you installed the packages correctly and that Python can find them.
