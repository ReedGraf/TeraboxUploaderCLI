"""
TeraBox Uploader CLI: formatting.py
This module is used to format the output of the program.
It uses the colorama library to color the output.
Used in: main.py

This program is provided as-is, without any warranty.
This program is not affiliated with Terabox in any way.
This program is licensed under the MIT License.

Developed by Gonçalo M. (@dnigamer in GitHub).
For more information, please visit https://github.com/dnigamer/TeraboxUploaderCLI
If you find any bugs, please open an issue in the GitHub repository mentioned in the link above.
"""

from datetime import datetime

from colorama import Fore, Back, Style


class Formatting:
    """
    This class is used to format the output of the program.
    It uses the colorama library to color the output.
    """
    def __init__(self, timestamps=False):
        """
        This method initializes the colorama library.
        :param timestamps: If True, the output will be formatted with a timestamp.
        """
        if timestamps:
            self.timestamps = True
        else:
            self.timestamps = False
        self.fore = Fore
        self.back = Back
        self.style = Style

    def timestamp(self) -> str:
        """
        This method is used to format a message with a timestamp.
        :return:
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') if self.timestamps else ''
        return f"{self.style.BRIGHT}[{timestamp}]{self.style.RESET_ALL}"

    def error(self, subject: str, message: str) -> None:
        """
        This method is used to format a error message.
        :param subject: Add a classification to the logged message.
        :param message: The error message.
        :return:
        """
        return print(f"{self.timestamp()}{self.style.BRIGHT}{self.fore.RED} {subject.upper().ljust(12)}: "
                     f"{self.style.RESET_ALL}{message}")

    def warning(self, subject: str, message: str) -> None:
        """
        This method is used to format a warning message.
        :param subject: Add a classification to the logged message.
        :param message: The warning message.
        :return:
        """
        return print(f"{self.timestamp()}{self.style.BRIGHT}{self.fore.YELLOW} {subject.upper().ljust(12)}: "
                     f"{self.style.RESET_ALL}{message}")

    def success(self, subject: str, message: str) -> None:
        """
        This method is used to format a success message.
        :param subject: Add a classification to the logged message.
        :param message: The success message.
        :return:
        """
        return print(f"{self.timestamp()}{self.style.BRIGHT}{self.fore.GREEN} {subject.upper().ljust(12)}: "
                     f"{self.style.RESET_ALL}{message}")

    def info(self, subject: str, message: str) -> None:
        """
        This method is used to format an info message.
        :param subject: Add a classification to the logged message.
        :param message: The info message.
        :return:
        """
        return print(f"{self.timestamp()}{self.style.BRIGHT}{self.fore.CYAN} {subject.upper().ljust(12)}: "
                     f"{self.style.RESET_ALL}{message}")

    def debug(self, subject: str, message: str) -> None:
        """
        This method is used to format a debug message.
        :param subject: Add a classification to the logged message.
        :param message: The debug message.
        :return:
        """
        return print(f"{self.timestamp()}{self.style.BRIGHT}{self.fore.MAGENTA} {subject.upper().ljust(12)}: "
                     f"{self.style.RESET_ALL}{message}")
