import os
import shutil
import zipfile

# Define the source log folders
log_folder1 = r'C:\ProgramData\Cymulate\Agent\AgentLogs'
log_folder2 = r'C:\ProgramData\Cymulate\Agent\AttacksLogs'

# Define the destination folder
destination_folder = 'ctsulogs'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Function to copy log files recursively
def copy_logs(src_folder, dest_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_folder, os.path.relpath(source_file, src_folder))
            dest_path = os.path.dirname(dest_file)

            if not os.path.exists(dest_path):
                os.makedirs(dest_path)

            shutil.copy(source_file, dest_file)

# Print loading status
print("Collection Started")
print("Loading...")

# Copy logs from the source folders to the destination folder
copy_logs(log_folder1, destination_folder)
copy_logs(log_folder2, destination_folder)

# Zip the contents of the destination folder
zip_filename = 'ctsulogs.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(destination_folder):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, destination_folder))

# Remove the destination folder
shutil.rmtree(destination_folder)

# Print completion message
print(f'Finished - Please share the {zip_filename} with your CSM.')
