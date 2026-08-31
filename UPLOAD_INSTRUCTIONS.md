# How to Upload Your Package to PyPI

Follow these steps to publish your package to PyPI so anyone can install it with `pip install`.

## Step 1: Customize Your Package

Before uploading, update these files with your information:

1. **setup.py** - Replace:
   - `name="my-greeting-package"` with a unique package name
   - `author="Your Name"` with your name
   - `author_email="your.email@example.com"` with your email
   - `url="https://github.com/..."` with your repository URL (if you have one)

2. **pyproject.toml** - Replace the same information:
   - `name = "my-greeting-package"`
   - `authors` section
   - `[project.urls]` section

3. **LICENSE** - Replace "Your Name" with your actual name

4. **my_greeting_package/__init__.py** - Customize the greeting message to display your text!

## Step 2: Install Required Tools

Install the tools needed to build and upload your package:

```bash
pip install build twine
```

## Step 3: Create a PyPI Account

1. Go to [https://pypi.org/account/register/](https://pypi.org/account/register/)
2. Create an account
3. Verify your email address

## Step 4: Build Your Package

Navigate to your project directory and run:

```bash
python -m build
```

This will create a `dist/` folder containing your package files:
- `my-greeting-package-0.1.0.tar.gz`
- `my_greeting_package-0.1.0-py3-none-any.whl`

## Step 5: Upload to PyPI

Upload your package using twine:

```bash
twine upload dist/*
```

You'll be prompted for your PyPI username and password.

**Alternative: Use API Token (Recommended)**

1. Go to [https://pypi.org/manage/account/token/](https://pypi.org/manage/account/token/)
2. Create a new API token
3. Use `__token__` as username and your token as password

## Step 6: Test Your Package

After uploading, wait a few minutes, then try installing:

```bash
pip install my-greeting-package
```

Then run it:

```bash
greet
```

## Optional: Test on TestPyPI First

To practice without affecting the real PyPI:

1. Create account on [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/)
2. Upload to TestPyPI:
   ```bash
   twine upload --repository testpypi dist/*
   ```
3. Install from TestPyPI:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ my-greeting-package
   ```

## Updating Your Package

When you want to release a new version:

1. Update the version number in:
   - `setup.py` (line with `version="0.1.0"`)
   - `pyproject.toml` (line with `version = "0.1.0"`)
   - `my_greeting_package/__init__.py` (line with `__version__ = "0.1.0"`)

2. Delete the old `dist/` folder:
   ```bash
   Remove-Item -Recurse -Force dist
   ```

3. Build and upload again:
   ```bash
   python -m build
   twine upload dist/*
   ```

## Important Notes

- **Package names must be unique** on PyPI. If "my-greeting-package" is taken, choose a different name.
- **Once uploaded, you cannot replace a version**. You must increment the version number for updates.
- Keep your PyPI credentials secure and never commit them to version control.

## Troubleshooting

- **"File already exists"**: The version is already uploaded. Increment your version number.
- **"Invalid package name"**: Choose a different name that's not already taken.
- **"Invalid distribution"**: Make sure you ran `python -m build` successfully.

Good luck with your package! 🎉
