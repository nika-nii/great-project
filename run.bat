start "Bot" cmd /K "python bot\echo_bot.py" 
start "API" cmd /K "cd backend && python -m uvicorn main:app --reload" 