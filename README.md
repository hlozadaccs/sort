# Project Setup Guide

This guide will help you set up the project on macOS, Windows, and Linux using `pyenv`, `venv`, and the appropriate tools for development.

## 1. Install `pyenv`

### macOS

Using Homebrew:

```bash
brew update
brew install pyenv
```

Add `pyenv` to your shell:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
exec "$SHELL"
```

### Ubuntu / Linux

Install dependencies and `pyenv`:

```bash
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git

curl https://pyenv.run | bash
```

Add to `.bashrc` or `.zshrc`:

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

Reload your shell:

```bash
exec "$SHELL"
```

### Windows

Use **pyenv-win**:

```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://pyenv.run" -OutFile "./pyenv-win-install.ps1"
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\pyenv-win-install.ps1
```

Ensure the following are added to your system `PATH`:

- `%USERPROFILE%\.pyenv\pyenv-win\bin`
- `%USERPROFILE%\.pyenv\pyenv-win\shims`

## 2. Install Python 3.11 using `pyenv`

```bash
pyenv install 3.11.0
```

## 3. Clone the repository

```bash
git clone git@github.com:hlozadaccs/sort.git
```

## 4. Set Python 3.11 locally for the project

```bash
cd sort
pyenv local 3.11.0
```

---

## 5. Create a virtual environment using Python 3.11

```bash
python3.11 -m venv .venv
```

## 6. Activate the virtual environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows (CMD)

```cmd
.venv\Scripts\activate.bat
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

## 7. Run Pre-commit

```bash
pre-commit run --all-files
```

## 8. Run Pytest with coverage report

```bash
pytest --cov=. --cov-report=term-missing
```
