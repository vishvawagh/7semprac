import os

disk_path = '/dev/sdX'  # Replace with your disk path
output_dir = 'recovered_files'
os.makedirs(output_dir, exist_ok=True)

# Create a disk image
os.system(f'dd if={disk_path} of=disk_image.img bs=512')

# Analyze and recover files
with open('disk_image.img', 'rb') as img:
    while (data := img.read(512)):
        if b'FILE_START_MARKER' in data:
            start, end = data.find(b'FILE_START_MARKER'), data.find(b'FILE_END_MARKER')
            if start != -1 and end != -1:
                recovered_data = data[start:end + len(b'FILE_END_MARKER')]
                filename = f'{output_dir}/recovered_{len(os.listdir(output_dir))}.dat'
                with open(filename, 'wb') as f:
                    f.write(recovered_data)

os.remove('disk_image.img')
print("Recovery complete. Check 'recovered_files' directory.")
