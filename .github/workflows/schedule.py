name: Sync SRF SHEET

on:
  schedule:
  workflow_dispatch:

jobs:
  sync SRF SHEET:
    name: Sync - SRF SHEEt
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Set up Python 3.13
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Write Google credentials to file
        run: echo '${{ secrets.GOOGLE_CREDENTIALS_JSON }}' > credentials.json

      - name: Run irf_sync.py
        env:
          JOTFORM_API_KEY:         ${{ secrets.JOTFORM_API_KEY }}
          JOTFORM_FORM_ID:         ${{ secrets.JOTFORM_FORM_ID }}
          GOOGLE_SHEET_NAME:       ${{ secrets.GOOGLE_SHEET_NAME }}
          GOOGLE_WORKSHEET_NAME:   ${{ secrets.GOOGLE_WORKSHEET_NAME }}
          START_DATE:              ${{ secrets.START_DATE}}
          GOOGLE_CREDENTIALS_PATH: credentials.json
        run: python srf_automatic.py

      - name: Clean up credentials
        if: always()
        run: rm -f credentials.json