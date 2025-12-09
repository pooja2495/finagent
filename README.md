python -m venv .venv

Run locally:
1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r backend/requirements.txt
4. uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

Visit:
- Dashboard: http://localhost:8000/dashboard/
- Dummy Bank: http://localhost:8000/dummy_bank/

Playwright runner (local CLI demo):
- python agent/agent_runner.py
