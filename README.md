# D-Crack (Dhinesh-Crack)

**D-Crack** is a simple yet powerful tool for cracking password-protected ZIP and PDF files using brute-force attacks. It allows users to specify character sets, password lengths, and other parameters to customize the brute-force process, making it flexible and efficient for different use cases.

## Features
- Supports password cracking for:
  - ZIP files (with AES encryption via `pyzipper`)
  - PDF files (via `PyPDF2`)
- Configurable character sets:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Digits (0-9)
  - Special characters
- Allows user to specify minimum and maximum password lengths
- Displays each password attempt and saves the successful password in a text file
- Compatible with both Windows and Linux

## Prerequisites
Make sure to install the following dependencies:
```bash
pip install pyfiglet pyzipper PyPDF2
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dcrack.git
   cd dcrack
   ```

2. Run the script:
   ```bash
   python dcrack.py
   ```

3. Select the type of file to crack (ZIP or PDF):
   - Option [1]: Crack ZIP File
   - Option [2]: Crack PDF File

4. Enter the file path of the protected ZIP or PDF file.

5. Customize the brute-force attack by choosing which character sets to include and setting the minimum/maximum password length.

6. The script will begin attempting passwords and display each attempt. Once the correct password is found, it will be saved in a text file (`found_zipFile_Password.txt` or `found_PdfFile_Password.txt`).

## Example

To crack a ZIP file:
```
Enter file path: /path/to/encrypted.zip
Include lowercase a-z: 1
Include uppercase A-Z: 0
Include digits 1-9: 1
Include symbols: 0
Enter minimum length of password: 3
Enter maximum length of password: 4
```

The script will attempt all combinations of lowercase letters and digits between 3-4 characters long until the correct password is found.

## Limitations
- **Brute-force time**: The time taken to crack a password increases exponentially with the password length and the size of the character set used. Ensure that you adjust the parameters accordingly.
- **File type limitations**: Currently supports only ZIP and PDF files.

## Contributing
If you'd like to contribute or report issues, feel free to open a pull request or an issue in the repository. Contributions are always welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
