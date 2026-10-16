# Local Operations Runbook

## Start the application
From the repository root:

```powershell
py -m app
```

## Run one demonstration
```powershell
py -m app --pillar reliability
```

## Run the full test suite
```powershell
py -m unittest discover -s tests -v
```

## Triage a failure
1. Read the complete Python traceback.
2. Confirm the current directory is the repository root.
3. Confirm the file exists at the expected path.
4. Run the smallest relevant test module, e.g. `py -m unittest tests.test_health -v`.
5. Fix the cause, rerun the focused test, then rerun the full suite.

## Simulated incident exercise
- Trigger: `aggregate_health({"catalog": True, "payments-sandbox": False})`.
- Expected: overall status `degraded` and the failed dependency listed.
- Response: inspect dependency status and restore the simulated dependency.
- Evidence: test output and documented incident notes.

This runbook covers local simulations only. It does not configure a production on-call rotation, AWS monitoring, or incident automation.
