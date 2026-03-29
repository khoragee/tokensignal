# tokensignal
 AI-powered crypto trading signal app built on GenLayer Bradbury testnet
# TokenSignal — AI Consensus Trading Intelligence

> Built for the GenLayer Bradbury Hackathon

## What is TokenSignal?

TokenSignal is an Intelligent Contract on GenLayer that produces AI-powered crypto trading signals using decentralized consensus.

Users input a token symbol (BTC, ETH, SOL, etc.) and 5 validators — each running a different LLM — independently analyze market sentiment and reach consensus on a **BUY / HOLD / SELL** signal.

## How it works

1. User calls `get_signal("BTC")`
2. Each of the 5 validators independently runs an LLM prompt asking for a trading signal
3. **Optimistic Democracy** consensus resolves validator votes
4. **Equivalence Principle** ensures validators agree on the signal even if wording differs
5. Final signal is stored on-chain and readable via `get_last_signal()`

## GenLayer Requirements Met

| Requirement | Implementation |
|---|---|
| Optimistic Democracy | 5 validators vote on the signal via consensus |
| Equivalence Principle | `gl.eq_principle.strict_eq` ensures semantic agreement |
| Intelligent Contract | Written in Python, deployed on GenLayer Studio |

## Contract

- **File:** `token_signal.py`
- **Address (local):** `0xe8932723a291098A3cffE90791C967C5bd36655d`
- **Network:** GenLayer Bradbury Testnet (local Studio)

## Methods

- `get_signal(token: str)` — Write method. Triggers AI consensus and stores result.
- `get_last_signal()` — View method. Returns the last stored signal.

## Frontend

`index.html` — A clean dark-themed dApp UI built with vanilla HTML/CSS/JS.

## Running Locally

1. Install GenLayer Studio (Docker)
2. Deploy `token_signal.py`
3. Open `index.html` and point RPC to `http://localhost:4000`
4. Enter a token symbol and click Analyze

## Tech Stack

- **Smart Contract:** Python (GenLayer SDK)
- **Frontend:** HTML / CSS / JavaScript
- **AI Consensus:** Optimistic Democracy + Equivalence Principle
- **Network:** GenLayer Bradbury Testnet
