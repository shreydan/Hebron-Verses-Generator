```
warning: Chrome headless currently has a bug which defaults the screenshots to 800x600, switching to headless=new + updated resolution.

```


# Praise the Lord

---

## Hebron Calendar Verses Generator

- Uses [scripture.api.bible](https://scripture.api.bible) API
- 3 languages: English, Hindi, Telugu
- WORKING: Uses `google-chrome --headless` to launch a headless browser, replaces placeholder with Bible verses and references, takes 9:16 FHD screenshot.
- `google-chrome --headless` bash command is run from the python script `generator.py` using `subprocess` module and command string is split properly using `shlex`.
- Read more on Chrome headless: [Starting Headless (CLI)](https://developers.google.com/web/updates/2017/04/headless-chrome)
- Saved in `output` folder with month name.
- FONTS - saved in [fonts dir](/src/fonts/):
  - English: [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab?query=roboto+slab)
  - Hindi: [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans?query=noto+sans)
  - Telugu: [Hind Guntur](https://fonts.google.com/specimen/Hind+Guntur?query=hind+guntur#standard-styles)

```python
# config.py
API_KEY = 'api_key_string'
```

---

### Hebron | Fellowship

[Hebron Church](https://www.hebronfellowship.in)
HNo: 1-1-574, Golconda X Roads
Musheerabad, Gandhi Nagar
Hyderabad, Telangana-500020
India

---

### Siyyon Prayer House, Raipur, Chhattisgarh, India
