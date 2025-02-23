RUN_SERVER_SCRIPT = """
#!/bin/bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
"""

with open("scripts/run_server.sh", "w") as f:
    f.write(RUN_SERVER_SCRIPT)

print("Project structure successfully implemented.")
