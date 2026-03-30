# CTFd Certificate Generator Plugin

A CTFd plugin that allows authenticated users to generate personalized **Certificates of Participation** with a single click.

The certificate is dynamically generated using data from the CTFd database, including:
- Username
- Team name

---

## Features

- One-click certificate generation  
- Automatically pulls user + team data from CTFd  
- Clean web interface for certificate download  
- Custom certificate template support  
- Designed for post-CTF participant recognition  

---

## Certificate Preview

![Certificate Preview](cert.png)

---

## How It Works

1. User logs into the CTFd platform  
2. Navigates to the certificate page  
3. Clicks **"Generate Certificate"**  
4. Certificate is generated and downloaded instantly  

---

## Requirements

Before using this plugin, ensure:

- User must be **logged into CTFd**  
- Plugin is installed in a working **CTFd instance**  
- Required **custom font is installed on the server**  

---

## Font Requirement (IMPORTANT)

This plugin depends on a custom font for proper certificate rendering.

### Steps:

1. Install the required font on the server hosting CTFd  

2. Update the font path in the plugin configuration:

```python
FONT_PATH = "/path/to/your/font.ttf"
```

If the font is missing or misconfigured:
- Certificate generation may fail  
- Or render incorrectly  

---

## Installation

1. Clone into CTFd plugins directory:

```bash
cd CTFd/CTFd/plugins
git clone https://github.com/LordSudo/CTFd-Certgen.git

2. Restart CTFd:

```bash
docker-compose restart
```
---

## Admin Setup (CTFd UI)

After installing the plugin, an admin must manually create a page in the CTFd UI to expose the certificate feature.

### Steps:

1. Log in as an admin in CTFd  
2. Navigate to:  
   **Admin Panel → Pages → Create Page**

3. Configure the page:
   - **Title:** Certificate  
   - **Route:** `/certificates`  
   - **Content:** Leave empty *(handled by plugin template)*  
   - **Visibility:** Authenticated (recommended)  

4. Save the page  

---

## Access

Once configured, users can access the certificate page via:

```
/certificates
```

> Users must be logged in to generate their certificate.

---

## Configuration

You can customize:

- Certificate background (`cert.png`)  
- Event name    
- Font (via `FONT_PATH`)  

---

## Project Structure

```
ctfd-cert-generator/
│── __init__.py
│── routes.py
│── /templates/certificates.html
│── cert.png
│── README.md
```


## Contributing

Pull requests are welcome. Open an issue first for major changes.

---

## License

MIT License
