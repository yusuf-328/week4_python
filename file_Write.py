# File Read & Write with Error Handling

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