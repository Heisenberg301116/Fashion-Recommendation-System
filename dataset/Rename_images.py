import os

print(os.getcwd())

def rename_images(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    
    # Get a list of all files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # Sort the image files for consistent renaming
    image_files.sort()
    
    # Rename the images
    for index, image_file in enumerate(image_files, start=1):
        # Get the extension of the image file
        _, extension = os.path.splitext(image_file)
        
        # New name for the image
        new_name = f"{index}{extension}"
        
        # Full paths of the old and new names
        old_path = os.path.join(folder_path, image_file)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the image file
        os.rename(old_path, new_path)
        
        print(f"Renamed '{image_file}' to '{new_name}'")

folder_path = ['hat', 'outwear', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 't-shirt']

for i in folder_path:
    rename_images('Images/' + i)