# FileCategorizer

FileCategorizer is a Python tool designed to organize files in a specified directory by categorizing them into folders based on their file types. It helps to keep your files neat and orderly, making it easier to locate and manage them.

## Features

- Categorizes files into predefined categories such as Images, Documents, Videos, Audio, Archives, Scripts, and Others.
- Automatically creates folders for each category.
- Moves files into their respective folders.
- Handles file conflicts gracefully by skipping files that already exist in the destination folder.

## Categories and Extensions

| Category    | Extensions |
|-------------|------------|
| Images      | jpg, jpeg, png, gif, bmp, tiff, svg, ico, webp |
| Documents   | pdf, doc, docx, txt, xls, xlsx, ppt, pptx, odt, ods, odp, rtf, md |
| Videos      | mp4, mov, avi, mkv, flv, wmv, webm, mpg, mpeg, 3gp |
| Audio       | mp3, wav, aac, flac, ogg, m4a, wma, alac |
| Archives    | zip, rar, tar, gz, 7z, bz2, xz, iso |
| Scripts     | py, js, html, css, sh, bat, php, rb, pl, java, cpp, c, cs |
| Others      | All other file types not listed above |

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. Download the `file_categorizer.py` script directly from the repository. You can find the raw script file [here](https://raw.githubusercontent.com/mrshibly/DailyProjects/main/FileCategorizer/FileCategorizer.py).

   To download the script:
   - Right-click on the link and select "Save link as..." to download the file to your computer.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script by entering the following command:

```bash
python FileCategorizer.py
```

4. When prompted, enter the full path of the directory you want to organize (e.g., `C:\path\to\your\folder`).

## Example

```bash
Enter the path of the directory to organize: C:\Users\mrshibly\Downloads
Files in C:\Users\mrshibly\Downloads have been organized by category.
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to create an issue or submit a pull request.


## Contact

For any questions or suggestions, please reach out to [mahmudurrahman858@gmail.com](mailto:mahmudurrahman858@gmail.com).

---

Happy organizing with FileCategorizer!
