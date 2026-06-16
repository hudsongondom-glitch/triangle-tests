# Triangle – Unit Testing exercise

A small Python module with a function that checks whether three values can be
used as the sides of a triangle, together with a data-driven `pytest` test
suite. Quality control is done through automatic unit testing (regression
testing), as required by the *Software Quality Control* lab.

## Files
| File | Purpose |
|------|---------|
| `triangle.py` | `is_triangle(a, b, c)` and bonus `classify_triangle(a, b, c)` |
| `test_triangle.py` | parametrised pytest test suite |
| `requirements.txt` | test dependency (`pytest`) |

## The function under test
`is_triangle(a, b, c)` returns `True` when the three lengths form a valid,
non-degenerate triangle. The rule is the **triangle inequality**: after sorting
the sides, the sum of the two shortest must be **strictly greater** than the
longest, and every side must be positive. The degenerate case `a + b == c`
returns `False`.

## How to run the tests
```bash
python -m venv .venv
# Windows:  .venv\Scripts\activate     Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

The suite uses `@pytest.mark.parametrize` (the pytest equivalent of xUnit's
`[Theory]` / `[InlineData]`) and covers: valid triangles, degenerate triangles,
sides that are too long, non-positive sides, order-independence, the boundary
condition, float inputs, triangle classification and `TypeError` on
non-numeric input.

## Git (required by the lab)
This folder is a local Git repository with an incremental history:
```bash
git log --oneline --graph
```
To add a remote (GitHub / GitLab) and push:
```bash
git remote add origin https://github.com/<you>/triangle-tests.git
git branch -M main
git push -u origin main
```

### learngitbranching.js.org
The lab also asks you to complete the **Introduction → Main** and
**Push & Pull (Remote)** sections at https://learngitbranching.js.org/ and to
attach screenshots as evidence. Those interactive exercises must be done from
your own browser/account — paste the screenshots into the report where marked.
