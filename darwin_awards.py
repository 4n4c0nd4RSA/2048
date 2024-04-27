import os

data = {'./models\\01_model.keras': 5956, './models\\02_model.keras': 6397, './models\\03_model.keras': 5877, './models\\04_model.keras': 7804, './models\\05_model.keras': 4549, './models\\06_model.keras': 5913, './models\\07_model.keras': 5593, './models\\08_model.keras': 5435, './models\\09_model.keras': 13841, './models\\10_model.keras': 4334, './models\\11_model.keras': 4503, './models\\12_model.keras': 5284, './models\\13_model.keras': 291, './models\\14_model.keras': 362, './models\\15_model.keras': 31323, './models\\16_model.keras': 33450, './models\\17_model.keras': 51465}

sorted_data = sorted(data.items(), key=lambda x: x[1])

for item in sorted_data:
    print(item)

split_index = len(sorted_data) // 2

for file_path, value in sorted_data[:split_index]:
    try:
        #os.remove(file_path)
        print(f"Deleted: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")