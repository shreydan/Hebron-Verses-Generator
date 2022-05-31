# Praise the Lord

---

## Hebron Calendar Verses Generator

- Uses [scripture.api.bible](https://scripture.api.bible) API
- 3 languages: English, Hindi, Telugu
- WORKING: Uses `google-chrome --headless` to launch a headless browser, replaces placeholder with Bible verses and references, takes 9:16 FHD screenshot.
- `google-chrome --headless` bash command is run from the python script `generator.py` using `subprocess` module and command string is split properly using `shlex`.
- Read more on Chrome headless: [Starting Headless (CLI)](https://developers.google.com/web/updates/2017/04/headless-chrome)
- Saved in `output` folder with month name.

```python
# config.py
API_KEY = 'api_key_string'
```

---
