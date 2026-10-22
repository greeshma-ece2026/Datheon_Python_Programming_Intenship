import os
import shutil

print("=" * 45)
print("   AUTOMATED FILE ORGANIZER")
print("=" * 45)

folder = input("Enter folder path to organize: ").strip().strip('"')

if not os.path.isdir(folder):
    print("Error: Folder does not exist!")
else:
    categories = {
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Archives": [".zip", ".rar", ".7z"],
        "Code": [".py", ".c", ".cpp", ".java", ".html", ".css", ".js"]
    }

    moved = 0
    errors = 0

    for filename in os.listdir(folder):
        source = os.path.join(folder, filename)

        if not os.path.isfile(source):
            continue

        extension = os.path.splitext(filename)[1].lower()
        category = "Others"

        for name, extensions in categories.items():
            if extension in extensions:
                category = name
                break

        destination_folder = os.path.join(folder, category)

        try:
            os.makedirs(destination_folder, exist_ok=True)
            destination = os.path.join(destination_folder, filename)

            if os.path.exists(destination):
                print("Skipped duplicate:", filename)
                continue

            shutil.move(source, destination)
            print("Moved:", filename, "->", category)
            moved += 1

        except (PermissionError, OSError) as error:
            print("Could not move:", filename, "-", error)
            errors += 1

    print("\n" + "=" * 45)
    print("ORGANIZATION SUMMARY")
    print("=" * 45)
    print("Files moved:", moved)
    print("Errors:", errors)
    print("Organization completed!")
    input("\nPress Enter to exit...")