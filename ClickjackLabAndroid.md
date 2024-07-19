# Welcome to DeadmanXXXII's Lab Guide

Welcome to my lab guide! Below, you'll find instructions for setting up and using various tools and techniques, including a detailed walkthrough for experimenting with clickjacking using Nethunter. Dive in and explore!

## Getting Started

Today, I set up my own lab. For a detailed walkthrough of the process, including the nearly opaque overlay in the hosted files, follow the steps below.

**Prerequisites:** You need Nethunter, available for both Android and iPhone. Here are the two methods for installation:

### Method 1: Installation via David Bombal's Video

1. **Find David Bombal on YouTube:**
   - [Watch his Nethunter installation video here](https://youtu.be/KxOGyuGq0Ts?si=a3Mdc-4VtLAgnFB1). The link is also available in `FreeU.txt`.

### Method 2: Manual Installation

1. **Install Kali Nethunter Full Version**

2. **Install Dependencies in Termux:**
   ```bash
   pkg update -y && pkg install wget -y

3. **Download the Installation Script:**
```bash
wget https://raw.githubusercontent.com/rc-chuah/Kali-Nethunter-In-Termux/master/install-nethunter-full-termux

4. **Give Execution Permission:**
```bash
chmod +x install-nethunter-full-termux

5. **Run the Script:**
5. **next**
```bash
./install-nethunter-full-termux

### Start Kali Nethunter:

1. **Firstly:**
```bash
nethunter
nh -r
Note: This process may take a while, especially on models like the Google Pixel 3a and 4.

2. **Update and Install Necessary Packages:**
```bash
dpkg --configure -a
apt update && upgrade -y
apt install python3
apt install wget -y
Credited to Offensive Security

# Nethunter Clickjacked
## Lab Begins:

If you don't have a code editor, use GitHub.dev, which provides a VSCode-like editor in your web browser.

1. **Create Lab Directory:**
```bash
mkdir self_hosting
cd self_hosting

**Download Initial HTML File:**
```bash
wget -u https://github.dev/DeadmanXXXII/5-day-coding-challenge/blame/main/Day%205%20challenge%203.html -O index.html

**Check the Downloaded File:**
```bash
ls
cat index.html

**Start a Local HTTP Server:**
```bash
python3 -m http.server 8000
Open your phone’s browser and navigate to http://0.0.0.0:8000/ to view the page. It should display "How to make tea."

**Update CSS File:**
```bash
wget -u https://github.dev/DeadmanXXXII/5-day-coding-challenge/blame/main/Day%205%20challenge%203.css -O index.css
Refresh your browser at http://0.0.0.0:8000/ to see the updated page with new icons and orange headers.

**Update HTML for Clickjacking:**
```bash
wget -u https://github.dev/DeadmanXXXII/attack/blame/main/clickjackingselfhost.html -O index.html
Ensure that href or src attributes point to http://0.0.0.0:8000/ or adjust them as needed. If required, use nano or vim to edit index.html.

**Verify Python Version:**
```bash
python3 --version
Ensure it’s version 3.11.0 or above.

**Restart the Local HTTP Server:**
```bash
python3 -m http.server 8000
Visit http://0.0.0.0:8000/ in your browser. You should see a "Click Me" button. If it doesn’t appear, the attack might not be compatible with your phone’s OS. You can try other clickjacking examples from GitHub or modify the existing ones.

# Happy Hacking!

Feel free to explore different clickjacking techniques. Some might use opaque overlays, invisible buttons, or redirections to other sites or files.

Note: Be cautious when testing different attacks, as improper use may have legal consequences.

Enjoy your experimenting!!

- DeadmanXXXII
