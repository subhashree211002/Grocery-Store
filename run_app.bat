@echo off

if not exist .venv (
    echo Creating virtual environment...
    python3 -m venv .venv
) else (
    echo Virtual environment already exists.
)

echo Activating virtual environment...
call .venv\Scripts\activate

echo Installing requirements...
pip install -r requirements.txt

echo Running the application...
python main.py