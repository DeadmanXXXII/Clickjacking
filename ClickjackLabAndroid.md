# Welcome to DeadmanXXXII's Clickjacking Lab Guide

Welcome to my lab guide! 
Below, you'll find a detailed walkthrough for setting up and using various tools and techniques. Dive in and explore!

## Getting Started

Today, I built my own lab, which you can find detailed under this section. If you're interested in experimenting with clickjacking using Nethunter, follow the steps below. You can also check the third-last photo to see the nearly opaque overlay in the hosted files.

**Prerequisites:** You need Nethunter, which is available for both Android and iPhone. There are two ways to set this up:

### Method 1: Installation via David Bombal's Video

1. **Find David Bombal on YouTube:**
   - [Watch his Nethunter installation video here](https://youtu.be/KxOGyuGq0Ts?si=a3Mdc-4VtLAgnFB1). The link is also available in `FreeU.txt`.

### Method 2: Manual Installation

1. **Install Kali Nethunter Full Version**

2. **Install Dependencies in Termux:**
   ```bash
   pkg update -y && pkg install wget -y
Download the Installation Script:

bash
Copy code
wget https://raw.githubusercontent.com/rc-chuah/Kali-Nethunter-In-Termux/master/install-nethunter-full-termux
Give Execution Permission:

bash
Copy code
chmod +x install-nethunter-full-termux
Run the Script:

bash
Copy code
./install-nethunter-full-termux
Start Kali Nethunter:

bash
Copy code
nethunter
nh -r
Note: This step might take a while, depending on your phone model. For Google Pixel 3a and 4, it took approximately 4 days.

Update and Install Necessary Packages:

bash
Copy code
dpkg --configure -a
apt update && upgrade -y
apt install python3
apt install wget -y
Credited to Offensive Security

Nethunter Clickjacked
Lab Begins:

If you don't have a code editor, use GitHub.dev, which provides a VSCode-like editor in your web browser.

Create Lab Directory:

bash
Copy code
mkdir self_hosting
cd self_hosting
Download Files:

bash
Copy code
wget -u https://github.dev/DeadmanXXXII/5-day-coding-challenge/blame/main/Day%205%20challenge%203.html -O index.html
Check the Downloaded File:

bash
Copy code
ls
cat index.html
Start a Local HTTP Server:

bash
Copy code
python3 -m http.server 8000
Open your phone’s browser and navigate to http://0.0.0.0:8000/ to see the page. It should display "How to make tea."

Update CSS File:

bash
Copy code
wget -u https://github.dev/DeadmanXXXII/5-day-coding-challenge/blame/main/Day%205%20challenge%203.css -O index.css
Refresh your browser at http://0.0.0.0:8000/ to see the updated page with new icons and orange headers.

Update HTML for Clickjacking:

bash
Copy code
wget -u https://github.dev/DeadmanXXXII/attack/blame/main/clickjackingselfhost.html -O index.html
Ensure the href or src attributes point to http://0.0.0.0:8000/ or update them accordingly. If needed, use nano or vim to edit index.html.

Verify Python Version:

bash
Copy code
python3 --version
Ensure it’s version 3.11.0 or above.

Restart the Local HTTP Server:

bash
Copy code
python3 -m http.server 8000
Visit http://0.0.0.0:8000/ in your browser. You should see a "Click Me" button. If not, the attack might not be compatible with your phone’s OS. You can try other clickjacking examples from GitHub or modify the existing ones.

Happy Hacking!

Feel free to explore different clickjacking techniques. Some overlays might be opaque, while others may use invisible buttons or redirect to other sites or files.

Note: Be cautious when testing different attacks as running them improperly could have legal consequences.

Additional Resources
Labelled Video: I’ll upload a video demonstration once I'm home and figure out how to upload videos in GitHub.dev.
Enjoy your experiments and have fun hacking!

- DeadmanXXXII

css
Copy code

Feel free to adjust any specific details or URLs to better fit your needs.





