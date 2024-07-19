##  📖 Table Of Contents
- About
- How to Build
- Documentation
- Code explanation
- Feedback and Contributions
- Contacts

## 🚀 About
The **Twitter_Complaint_Bot** is an automated bot designed to check your internet speed using Speedtest.net and tweet a complaint at your internet service provider if the speed is lower than the promised rate.

## 📝 How to Build
**Prerequisites**
  - Python 3.x
  - selenium library
  - Webdriver

 **To build the project follow these steps:**
  - **installation:**
```shell
# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed
            
# Clone the repository
git clone https://github.com/Akwaowo91/Twitter_Complain_Bot.git
cd Twitter_Complain_Bot       

# Install the required package
pip install selenium
```
  - **Setup Web-Driver:**
      - Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and ensure it's in your system's PATH.
        
  - **Configuration:**
      - Set your Twitter credentials and promised internet speed:
          - Edit the InternetSpeedTwitterBot.py file and replace the placeholders for TWITTER_EMAIL, TWITTER_PASSWORD, PROMISED_DOWN, and PROMISED_UP with your actual values.
            ```shell
            PROMISED_DOWN = 150
            PROMISED_UP = 10
            TWITTER_EMAIL = "YOUR TWITTER EMAIL"
            TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"
            ```
      - **Documentation:**
          - Selenium: https://www.selenium.dev/documentation/
       
## 📄 Code Explanation
  - When you execute the code will execute the following:
      - Open Speedtest.net and perform a speed test.
      - Capture the download and upload speeds.
      - Log in to Twitter.
      - Tweet a complaint to your internet service provider if the actual speeds are lower than the promised speeds.
   
## 🤝 Feedback and Contributions
I have made every effort to implement all the main aspects of the Twitter Complaint Bot project in the best possible way. However, the development journey doesn't end here, and your input is crucial for our continuous improvement.

> [!IMPORTANT]
> Whether you have feedback on features, have encountered any bugs, or have suggestions for enhancements, we're eager to hear from you. Your insights help us make the Twitter Complaint Bot project more robust and user-friendly.

Please feel free to submit an issue or open an issue on this repository, if you have any feedback or suggestions.
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or new features.
I appreciate your support and look forward to making this product even better with your help!

**⚠️ This project is licensed under the MIT License.**

## ©️ Contact
For more questions you can reach me through:  
- email: akwaowoudokop15@gmail.com
- LinkedIn: https://www.linkedin.com/in/akwaowo-udokop-474662229/
