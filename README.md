# oecd_demo
Demo SDMX-VTL on OECD data

## Installation

This project uses Poetry for dependency management. Make sure you have Poetry installed on your system.

### Prerequisites

- Python 3.11 or higher
- Poetry (install from [poetry.poetry.dev](https://poetry.poetry.dev/))

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd oecd_demo
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Activate the virtual environment:
- Poetry 1.x
```bash
poetry shell
```
- Poetry 2.x
```bash
poetry env activate
```
This will print the activation command for the virtual environment.  

**Example (Windows PowerShell):**
```powershell
& "C:\Users\<your-user>\AppData\Local\pypoetry\Cache\virtualenvs\oecd-demo-xxxx\Scripts\activate.ps1"
```
**Example (Unix/MacOS):**
```bash
source ~/path/to/your/virtualenv/bin/activate
```



    

## Usage

### Running the Jupyter Notebook

1. Make sure you're in the Poetry virtual environment:
- Poetry 1.x
```bash
poetry shell
```
- Poetry 2.x
```bash
poetry env activate
```

2. Navigate to the src directory and run Jupyter:
```bash
cd src
jupyter notebook
```

3. Open `notenook.ipynb` in your browser

### Running from Command Line

You can also run the notebook directly from the command line:

```bash
poetry run jupyter notebook src/notenook.ipynb
```

### Alternative: Run as Python Script

If you prefer to run it as a Python script, you can convert the notebook or run it programmatically:

```bash
poetry run python -c "
from src.notenook import *
# Your code here
"
```

## Project Structure

- `src/notenook.ipynb` - Main Jupyter notebook with OECD data processing
- `output/` - Generated output files and logs
- `pyproject.toml` - Poetry configuration and dependencies
- `poetry.lock` - Locked dependency versions

## Dependencies

The main dependencies are managed by Poetry and include:
- `pysdmx` - SDMX data handling
- `vtlengine` - VTL transformation engine
- `jupyter` - Jupyter notebook environment

## Output

The notebook generates several output files:
- Validation logs in `output/validations/`
- Derivation logs in `output/derivation/`
- Final dataset logs in `output/derivation/final_dataset_logs.csv`
