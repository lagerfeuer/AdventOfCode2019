# Advent Of Code 2019

## Dependencies

```bash
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```

## Running a solution

```bash
python3 dayXX/main.py
```

## Testing

Test all solutions:
```bash
pytest
```

Test a specific solution:
```bash
cd dayXX/
pytest
```
or
```bash
pytest dayXX/
```

### Issues

If `pytest` is not working, try `python3 -m pytest` or `deactivate && source venv/bin/activate` and run `pytest` again.
