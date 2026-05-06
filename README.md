# GenLayer AI ChatBot

An Intelligent Contract deployed on GenLayer testnet (Asimov).

## What it does
- `ask_ai(query)` — asks AI any question and stores the answer onchain
- `get_crypto_price(ticker)` — gets crypto price via AI
- `chat(message)` — chat with AI agent, history stored onchain
- `get_last_answer()` — reads last AI response
- `get_history()` — reads full chat history

## Tech Stack
- GenLayer Intelligent Contracts
- Python + GenLayer SDK
- LLM inference via gl.nondet.exec_prompt

## Contract Address
`0x1c...9CCc` (Testnet Asimov)

## Deploy
Built and deployed via [GenLayer Studio](https://studio.genlayer.com)
