import os


# Path to the models directory
models_dir = './models'

# Dictionary containing file paths and their corresponding values
battle_ground_data = {'./models\\01_model.keras': 8865, './models\\02_model.keras': 34635, './models\\03_model.keras': 58018, './models\\04_model.keras': 50633, './models\\05_model.keras': 55671, './models\\06_model.keras': 18184, './models\\07_model.keras': 30661, './models\\08_model.keras': 47840, './models\\09_model.keras': 54787, './models\\10_model.keras': 57834, './models\\11_model.keras': 54876, './models\\12_model.keras': 52253, './models\\13_model.keras': 58047, './models\\14_model.keras': 57538, './models\\15_model.keras': 6901, './models\\16_model.keras': 57709, './models\\17_model.keras': 57592, './models\\18_model.keras': 57509, './models\\19_model.keras': 57294}

# Sort data based on values
sorted_data = sorted(battle_ground_data.items(), key=lambda x: x[1], reverse=True)

for item in sorted_data:
    print(f'Model: {item[0]}\tScore: {item[1]}')

# Split data into two halves
split_index = len(sorted_data) // 2

# Delete files in the lower half
for file_path, value in sorted_data[split_index:]:
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

# List all files in the models directory
files = os.listdir(models_dir)

# Sort files if needed, can be customized or removed depending on requirements
files.sort()

# Rename all files in sorted order starting from "01_model.keras"
for index, filename in enumerate(files, start=1):
    old_file_path = os.path.join(models_dir, filename)
    new_file_name = f"{str(index).zfill(2)}_model.keras"
    new_file_path = os.path.join(models_dir, new_file_name)
    try:
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {old_file_path} to {new_file_path}")
    except FileNotFoundError:
        print(f"File not found: {old_file_path}")
    except Exception as e:
        print(f"Error renaming {old_file_path} to {new_file_path}: {e}")
