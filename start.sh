#eval "$(conda shell.bash hook)"
#conda activate {ENV NAME}
#cd {Path to app}
uvicorn app:app --port 8081 --workers 2 --proxy-headers --host 0.0.0.0