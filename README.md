# Password-Generator

## Overview
This **Password Generator** is a Python-based project that allows users to create strong, unique passwords tailored to their preferences. The tool emphasizes security by offering options to customize the number of letters, numbers, and symbols in the generated password, providing a robust solution for safeguarding your digital assets.

## Features
- **User Input Customization**: Users can specify how many letters, numbers, and symbols they want in their password, ensuring that their generated passwords meet personal security standards.
- **Two Generation Modes**: 
  - **Easy Mode**: Generates a password without shuffling the characters, simply concatenating the selected characters in the order they are chosen.
  - **Hard Mode**: Utilizes the `random.shuffle()` method to randomize the order of characters, resulting in a more secure and unpredictable password.
- **Randomized Character Selection**: Utilizes Python's `random` module to ensure that the selection of characters is truly random, enhancing the strength of the generated passwords.

## Key Concepts
- **For Loops**: The project employs `for` loops to iterate through user-defined ranges, allowing the program to select the specified number of letters, numbers, and symbols efficiently.
- **Random Module**: The `random` module is imported to access functions that facilitate random selection and shuffling, ensuring the generation of secure passwords.

## Installation
To run this project locally:
1. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd password-generator
   ```
3. Run the script:
   ```bash
   python password_generator.py
   ```

## Usage
1. Upon execution, the program welcomes the user and prompts for the desired number of letters, numbers, and symbols.
2. After inputting the preferences, the program generates a password based on the selected options and displays it to the user.

## Challenges and Learning Outcomes
This project presented several challenges, including:
- Understanding how to effectively handle user input and validate it.
- Implementing secure password generation techniques to ensure that the final output is robust against potential security threats.
- Gaining hands-on experience with Python’s `random` module and improving my skills in string manipulation.

This project has deepened my appreciation for programming's role in enhancing cybersecurity and has motivated me to continue exploring the world of coding.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.
