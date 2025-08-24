# File Read & Write with Error Handling

This Python script demonstrates how to safely read from a file, modify its content, and write to a new file, with robust error handling for common issues. The script is interactive and provides clear feedback to users about the status of file operations.

## Features

- **Reads a file** specified by user input.
- **Displays the original file content** in the terminal.
- **Appends a footer line** to the original content.
- **Writes the modified content** to a new file (prefixed with `modified_`).
- **Handles errors gracefully**:
  - File not found (`FileNotFoundError`)
  - Permission denied (`PermissionError`)
  - Any other unexpected errors

## Usage

1. Ensure you have Python 3 installed.
2. Save the script to a `.py` file (e.g., `file_read_write.py`).
3. Run the script in a terminal:

   ```sh
   python file_read_write.py
   ```

4. When prompted, enter the path to the file you want to read.

## Example Output

```
Enter the filename to read: sample.txt

--- Original File Content ---
Hello, this is a sample file.

✅ Modified content written to 'modified_sample.txt' successfully!
```

## Error Handling

- **File Not Found**

  ```
  ❌ Error: File not found. Please check the file path and try again.
  ```

- **Permission Error**

  ```
  ❌ Error: You don’t have permission to read this file.
  ```

- **Unexpected Error**

  ```
  ⚠ An unexpected error occurred: <error details>
  ```

## Code Overview

```python
def file_read_write():
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read file
        with open(filename, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()
            print("\n--- Original File Content ---")
            print(content)

        # Modify content (example: add a footer line)
        modified_content = content + "\n\nThis is the appended part below."

        # Write modified content into a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w", encoding="utf-8") as new_file:
            new_file.write(modified_content)

        print(f"\n✅ Modified content written to '{new_filename}' successfully!")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the file path and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠ An unexpected error occurred: {e}")

# Run the function
file_read_write()
```

## Notes

- The script ignores encoding errors when reading files.
- The new file will be created in the same directory as the script unless a full path is specified.
- Modify the appended footer line as needed for your application.

---

Feel free to fork this repository and modify the script for your own needs!
