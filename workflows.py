name: Multiverse CI/CD Workflow

on:
  push:
  pull_request:
    types: [approved, opened, edited, reopened]
  workflow_dispatch:

jobs:
  pytest:
    name: Test the Survey Application
    runs-on: ubuntu-latest
    steps:
    - name: Checkout the repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.x'

    - name: Update pip
      run: python -m pip install --upgrade pip

    - name: Install Pytest
      run: pip install pytest pytest-cov

    - name: Run Pytest
      run: pytest
      working-directory: input