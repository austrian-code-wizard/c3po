import py_compile
import os
import sys

def check_python_syntax():
    """Check Python syntax for all .py files in src directory"""
    errors = []
    for root, dirs, files in os.walk('src'):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                try:
                    py_compile.compile(filepath, doraise=True)
                    print(f"✓ {filepath}")
                except py_compile.PyCompileError as e:
                    errors.append(f"✗ {filepath}: {e}")
                    print(f"✗ {filepath}: {e}")
    
    if errors:
        print(f"\nFound {len(errors)} syntax errors:")
        for error in errors:
            print(error)
        return False
    else:
        print(f"\nAll Python files passed syntax check!")
        return True

if __name__ == "__main__":
    success = check_python_syntax()
    sys.exit(0 if success else 1)
