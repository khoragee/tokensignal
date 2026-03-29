# 🧠 TokenSignal — AI Consensus Trading Intelligence

> **GenLayer Bradbury Hackathon Submission**
> Built by [@khoragee](https://github.com/khoragee)

---

## What is TokenSignal?

TokenSignal is an **Intelligent Contract** deployed on the GenLayer Bradbury testnet that produces AI-powered crypto trading signals through decentralized consensus.

Traditional trading signal apps rely on a single centralized AI or algorithm. TokenSignal is different — it uses **5 independent AI validators**, each running a different LLM, to reach consensus on a BUY / HOLD / SELL signal for any crypto token. No single point of failure. No single AI bias. Pure decentralized intelligence.

---

## How It Works

```
User inputs token (e.g. "BTC")
        ↓
5 Validators independently ask their LLMs for a trading signal
        ↓
Optimistic Democracy resolves validator votes
        ↓
Equivalence Principle ensures semantic agreement
        ↓
Final BUY / HOLD / SELL signal stored on-chain
        ↓
User reads result via get_last_signal()
```

---

## GenLayer Requirements

| Requirement | Implementation |
|---|---|
| ✅ Optimistic Democracy | 5 validators each independently run an LLM prompt and vote on the signal. Consensus is reached when a majority agrees. |
| ✅ Equivalence Principle | `gl.eq_principle.strict_eq` ensures validators agree on the same signal even if their internal reasoning differs. |
| ✅ Intelligent Contract | Written in Python using the GenLayer SDK, deployed on GenLayer Bradbury testnet. |
| ✅ Non-deterministic execution | Each validator's LLM independently produces a signal — results may vary per validator but consensus resolves the final answer. |

---

## Contract Methods

### `get_signal(token: str)` — Write
Triggers the full AI consensus pipeline for the given token symbol.

**Example:** `get_signal("BTC")`

**What happens:**
1. Each of the 5 validators runs an LLM prompt asking for a trading signal for the token
2. Each LLM returns BUY, HOLD, or SELL
3. Optimistic Democracy reaches consensus
4. Result is stored on-chain

### `get_last_signal()` — View (free, no gas)
Returns the last stored signal as a dict:
```json
{
  "token": "BTC",
  "signal": "HOLD",
  "confidence": "MEDIUM",
  "reason": "AI consensus signal"
}
```

---

## Live Demo

- **Frontend:** https://tokensignal.vercel.app
- **Contract Address:** `0xe8932723a291098A3cffE90791C967C5bd36655d`
- **Network:** GenLayer Bradbury Testnet (local Studio)

> Note: GenLayer Bradbury is currently a local simulator. The Vercel frontend runs in demo mode when not connected to a local node. The contract itself is fully deployed and tested on the local Bradbury testnet.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Intelligent Contract | Python (GenLayer SDK) |
| Consensus | Optimistic Democracy |
| Equivalence | `gl.eq_principle.strict_eq` |
| Frontend | HTML / CSS / JavaScript |
| Hosting | Vercel |
| Network | GenLayer Bradbury Testnet |
| LLM Providers | Claude, GPT-4, Gemini, DeepSeek, LLaMA (via validators) |

---

## Project Structure

```
tokensignal/
├── token_signal.py   # The Intelligent Contract
├── index.html        # Frontend dApp
└── README.md         # This file
```

---

## Running Locally

1. Install and start GenLayer Studio (Docker)
2. Open `http://localhost:8080`
3. Create a new contract file and paste `token_signal.py`
4. Deploy the contract (no constructor inputs needed)
5. Call `get_signal("BTC")` and wait for FINALIZED
6. Call `get_last_signal()` to read the result
7. Open `index.html` in your browser for the full UI

---

## Why TokenSignal?

Most crypto trading signals come from:
- Centralized APIs (single point of failure)
- Single AI models (single point of bias)
- Black-box algorithms (no transparency)

TokenSignal fixes all three by using GenLayer's decentralized AI consensus:
- **5 different LLMs** vote independently
- **Optimistic Democracy** resolves disagreements transparently
- **On-chain storage** makes every signal auditable
- **No oracle needed** — AI validators fetch and analyze data natively

This is what only GenLayer can do. No other blockchain supports this.

---

## Builder

**hacker72847b6** — Front-end developer, Smart contract engineer, Web3 builder
- Location: Nigeria/Delta/Agbor
- Skills: Smart contracts, Frontend, UI/UX
- Currently building: A trading bot (TokenSignal is a natural extension of this)
