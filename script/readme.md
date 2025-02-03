# Content Uutomation Posting

This repositori provides the content automation posting on **Medium** and **Substack** using **Python** and **Selenium**.

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

## Medium 2FA and Human Interaction
- Medium requires **two-factor authentication (2FA)** to log in. During the login process, you may be prompted to confirm your identity via email or another authentication method.
- **Human Action Required**: When running the `run_medium.py` script, the system will pause and wait for you to complete the 2FA process manually. Once authenticated, the script will resume automatically.
- Ensure you monitor the email account linked to your Medium account during the process to complete the required actions promptly.

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
        "subtitle": "subtitle"
    }
```

## Additional Notes
Ensure Chromedriver is installed and added to your system's PATH.
Draft content is expected to be pre-prepared in JSON format and accessible by the scripts.

Possible future updates:
- AI image creation to complement Medium and Substack post.
- Substack tags addition.
