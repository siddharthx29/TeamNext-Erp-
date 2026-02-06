# Email Setup Instructions for TeamNext ERP

## How to Configure Gmail to Send OTP Emails

To receive OTP emails in your Gmail inbox (like nsb566@gmail.com), follow these steps:

### Step 1: Enable 2-Step Verification
1. Go to your Google Account: https://myaccount.google.com/
2. Click on **Security** in the left sidebar
3. Under "Signing in to Google", find **2-Step Verification**
4. Click on it and follow the prompts to enable it

### Step 2: Generate an App Password
1. Go to: https://myaccount.google.com/apppasswords
2. You may need to sign in again
3. Under "Select app", choose **Mail**
4. Under "Select device", choose **Other (Custom name)**
5. Type "TeamNext ERP" or any name you prefer
6. Click **Generate**
7. Google will show you a 16-character password (like: `abcd efgh ijkl mnop`)
8. **Copy this password** (you can remove the spaces)

### Step 3: Update settings.py
1. Open `Teamnext/project/settings.py`
2. Find the email settings section
3. Update these two lines:
   ```python
   EMAIL_HOST_USER = 'your-email@gmail.com'  # Your Gmail address
   EMAIL_HOST_PASSWORD = 'your-16-char-app-password'  # The App Password from Step 2
   ```
4. Save the file
5. Restart your Django server

### Step 4: Test
1. Go to the login page
2. Click "Login with OTP"
3. Enter your registered email
4. Check your Gmail inbox for the OTP email
5. The email will have a beautiful HTML format with the OTP clearly displayed

### Troubleshooting

**If emails don't arrive:**
- Check that EMAIL_HOST_USER and EMAIL_HOST_PASSWORD are set correctly
- Make sure you're using an App Password, not your regular Gmail password
- Check your spam/junk folder
- Verify 2-Step Verification is enabled
- Check the Django console for error messages

**If you see errors:**
- Make sure the App Password is correct (16 characters, no spaces)
- Verify your Gmail address is correct
- Check that less secure app access is not required (App Passwords should work)

### Security Note
- Never commit your App Password to version control
- Keep your settings.py file secure
- App Passwords are safer than using your main Gmail password
