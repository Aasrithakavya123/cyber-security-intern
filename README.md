task 1
Caesar Cipher Encryption and Decryption Program
This Python program implements the Caesar Cipher algorithm for encrypting and decrypting text messages. The Caesar Cipher shifts each letter in the plaintext by a specified number of places down or up the alphabet.

Features
Encryption: Encrypts a message using a specified shift value.
Decryption: Decrypts an encrypted message using the same shift value.
Supports: Uppercase and lowercase English letters, maintaining non-alphabetic characters.
Usage
1.Run the program
2.Choose whether to encrypt or decrypt a message:

   Enter 'E' for encryption or 'D' for decryption.
   Input the message you want to process.
   Enter an integer shift value for encryption or decryption.
3.Follow the prompts and view the encrypted or decrypted message output.
Example
Encrypting a message:
    Do you want to (E)ncrypt or (D)ecrypt a message? E
    Enter your message: Hello, World!
    Enter the shift value (integer): 3
    Encrypted message: Khoor, Zruog!
Decrypting the encrypted message with the same shift:
    Do you want to (E)ncrypt or (D)ecrypt a message? D
    Enter your message: Khoor, Zruog!
    Enter the shift value (integer): 3
    Decrypted message: Hello, World!





Task -2
Image Encryption Tool
This tool allows users to encrypt and decrypt images using basic pixel manipulation techniques.

Features
   Encryption: Encrypt images by applying a key to pixel values.
   Decryption: Decrypt previously encrypted images using the same key.
   Supported Formats: Works with common image formats supported by Pillow (Python Imaging Library).
Requirements
  Python 3.x
  Pillow (Python Imaging Library)
Usage
1.Run the script
2.Follow the prompts to either encrypt or decrypt an image:

  Enter 'E' for encryption or 'D' for decryption.
  Provide the path to the input image.
  Specify the output path for the encrypted or decrypted image.
  Enter an integer key for encryption or decryption.
Encrypt an image:
  Do you want to (E)ncrypt or (D)ecrypt an image? E
  Enter the path of the image: #path of original image
  Enter the path to save the output image: #path of  output encrypt image
  Enter a key (integer value): 10
  Image encrypted and saved to /path/to/output/encrypted_image.jpg
Decrypt an image:
Do you want to (E)ncrypt or (D)ecrypt an image? D
  Enter the path of the image: #path of original image
  Enter the path to save the output image: #path of  output decrypt image
  Enter a key (integer value): 10
  Image decrypted and saved to /path/to/output/decrypted_image.jpg




Task 3
Password Strength Checker
This Python program assesses the strength of a password based on various criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. It provides feedback on the password's strength and specific areas for improvement.

Features
Password Strength Assessment: Evaluates the strength of a password based on defined criteria.
Criteria Evaluated:
Length: Minimum 8 characters.
Uppercase letters: At least one uppercase letter.
Lowercase letters: At least one lowercase letter.
Numbers: At least one digit.
Special characters: At least one special character from !@#$%^&*(),.?":{}|<>.
Requirements
Python 3.x
Usage
1.Run the program
2.Enter a password when prompted.

3.The program will evaluate the password based on the following criteria:

Minimum length requirement (8 characters).
Presence of uppercase letters.
Presence of lowercase letters.
Presence of numbers.
Presence of special characters.
4.You will receive feedback on the strength of the password and specific areas where it can be improved.
Assessing a password:
Enter a password to assess: MySecurePassword123!
Password Strength: Strong
Feedback:




Task 4
Python Keylogger with pynput
This Python program logs keystrokes from the keyboard using the pynput library. It captures keypress events and records them to a text file (keylog.txt). The program runs in the background and stops when the ESC key is pressed.

Features
Keystroke Logging: Records all keystrokes typed on the keyboard.
Special Key Handling: Handles special keys such as space, enter, and others.
Background Operation: Runs continuously in the background until terminated.
Requirements
 Python 3.x
 pynput library
Usage
1.Run the keylogger.
2.The keylogger will start running and logging keystrokes in real-time.

          Press ESC key to stop the keylogger.
Example
Running the keylogger:
   Keylogger is running. Press ESC to stop.
Output
The keystrokes are logged into keylog.txt file in the same directory where the script is located.

Notes
Ensure to use this tool responsibly and ethically. Obtain appropriate permissions before running the keylogger on any system.
Customize the logging behavior or file location as per your requirements.
Ensure to handle any security and privacy considerations when using or distributing such a tool.
