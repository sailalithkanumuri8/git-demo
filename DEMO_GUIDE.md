# Git Demo Guide for BDBI @ Georgia Tech

## Demo Scenario 1: Basic Add & Commit
**Goal**: Show how to track changes

1. Modify `calculator.py` - add a new function:
```python
def power(a, b):
    """Raise a to the power of b"""
    return a ** b
```

2. Stage and commit:
```bash
git status                    # Show untracked changes
git add calculator.py         # Stage the file
git status                    # Show staged changes
git commit -m "Add power function to calculator"
git push
```

## Demo Scenario 2: Multiple Files
**Goal**: Stage multiple files at once

1. Modify both `utils.py` and `student_grades.py`
2. Stage all changes:
```bash
git status
git add .                     # Stage all changes
git commit -m "Update utils and student grades"
git push
```

## Demo Scenario 3: Branching
**Goal**: Work on a new feature without affecting main code

1. Create a new branch:
```bash
git checkout -b advanced-calculator
```

2. Add new features to `calculator.py`:
```python
def square_root(a):
    return a ** 0.5

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

3. Commit on the branch:
```bash
git add calculator.py
git commit -m "Add square root and factorial functions"
git push
```

4. Switch back to main and merge:
```bash
git checkout main
git merge advanced-calculator
```

## Demo Scenario 4: Viewing History
**Goal**: Show project history

```bash
git log                       # View commit history
git log --oneline            # Compact view
git log --graph --oneline    # Visual branch graph
git diff                     # Show uncommitted changes
```

