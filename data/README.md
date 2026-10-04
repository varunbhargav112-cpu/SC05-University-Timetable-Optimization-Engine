# SC05 – University Timetable Optimization Engine

## Step 1 – Beginner Project

A timetable coordinator needs a weekly timetable that places courses into rooms and time slots without faculty, room, or cohort clashes.

### M1 target
Build a Genetic Algorithm timetable for a small test case and compare it with a simple baseline.

### Step 1
This version prepares the repository, input data, validation, test cases, baseline rules, and Product V1 sketch.

## Team
- Member 1: Repository + Testing/UI
- Member 2: Data
- Member 3: Baseline
- Member 4: Testing/UI

## How to run

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Install:
```bash
pip install -r requirements.txt
```

Run validation:
```bash
python src/validate_data.py
```

## Expected result

```text
STEP 1 DATA CHECK PASSED
```

The invalid test is stored separately and should produce a clear FAIL message when checked.

