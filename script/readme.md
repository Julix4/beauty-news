# Auto Poster

This project automates content posting on **Medium** and **Substack** using **Python** and **Selenium**.

## Requirements
- `Python`
- [Chromedriver](https://chromedriver.chromium.org/downloads)
- `selenium`

## Environment Variables

Set the following environment variables:

```env
### Medium
- `MEDIUM_EMAIL`: Your Medium account email address.

### Substack
- `SUBSTACK_EMAIL`: Your Substack account email address.
- `SUBSTACK_PASSWORD`: Your Substack account password.

### Chrome
- `CHROME_PROFILE_PATH`: Path to your Chrome profile. Example: `C:/Users/YourName/AppData/Local/Google/Chrome/User Data/Profile`
```

## Usage

- Run **all platforms**:
  ```bash
  python run_all.py
  ```
- Run **Medium only**:
  ```bash
  python run_medium.py
  ```
- Run **Substack only**:
  ```bash
  python run_substack.py
  ```

## Draft Content Format

Draft content should be in **JSON format**. Below an example:

```json
{
        "platform_name": "Medium",
        "title": "title",
        "body": "article content goes here in HTML or plain text.",
        "tags": [
            "a",
            "b",
            "c"
        ],
        "featured_image": "https://example.com/image.jpg"
    }

{
        "platform_name": "Substack",
        "title": "title",
        "body": "article content goes here in HTML or plain text.",
        "tags": [
            "a",
            "b",
            "c"
        ],
        "subtitle": "subtitle",
        "audience": "all"
    }

## Additional Notes
Ensure Chromedriver is installed and added to your system's PATH.
Draft content is expected to be pre-prepared in JSON format and accessible by the scripts.

