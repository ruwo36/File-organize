
# Files Organizer

![Files Organizer](https://github.com/ruwo36/File-organize/blob/main/File-organize/file%20organize.gif)

## About

**Files Organizer** is a Python program that arranges and organizes all types of files.

Sorting files is considered one of the most tedious human tasks, especially when dealing with a folder containing hundreds of files such as **_images_**, **_videos_**, **_music_**, **_documents_**, etc. It can be challenging to sort all these files and a lot of time can be wasted.

Example, this program sorts each type of file into a separate dedicated folder. For example, if you have a folder containing **_pdf_**, **_jpg_**, **_mp4_**, **_png_** files, etc., this program will sort them as follows:

- **_pdf_** files in a folder named **PDF**
- **_jpg_** files in a folder named **JPG**
- **_mp4_** files in a folder named **MP4**

This way, all files are sorted efficiently, and you can accomplish a task that would otherwise take a lot of time and effort in just a couple of seconds.

## How it works

When the program is executed, it asks the user to input the folder's path, and after entering it:

1. The program verifies if the path already exists.
2. If the path exists, it searches for all file formats present within this folder.
3. It creates a folder for each format found **after verifying the non-existence** of a folder with the same name or checking the existence of the folder already, and its name is in uppercase letters.
4. It moves each file with a specific format to its corresponding folder.

## Library's

- **os:** Operating System lib, it installs already when you install Python.
- **shutil:** Utility functions for copying and archiving files and directory trees, it installs already when you install Python.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ruwo36/File-organize.git
   ```

2. Install dependencies:

   - The libs already exists.

## Usage

1. Navigate to the project directory:

   ```bash
   cd File-organize
   ```

2. Run the program:

   ```bash
   python main.py
   ```

   After run this command the program ask you to enter folder path that content your files which you want to organize it.

## Example

```bash
python main.py
```
Show it in my [LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7194595374928396288/), I post a video explain it.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact:
- [my Gmail](mailto:mayasajeeb123@gmail.com), or [my Business Gmail](mailto:it.academy.info1@gmail.com).
- [LinkedIn](https://www.linkedin.com/in/ali-n-ajeeb).
