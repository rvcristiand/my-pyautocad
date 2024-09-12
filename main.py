from pyautocad import Autocad, APoint
import os
import time

def change_layer_color_in_dwg(file_path, layer_name, new_color):
    acad = Autocad()
    acad.Application.Documents.Open(file_path)
    doc = acad.ActiveDocument

    try:
        layer = doc.Layers.Item(layer_name)
        # Change the color of the layer
        layer.Color = new_color
        doc.Save()
        print(f"Updated color of layer '{layer_name}' in '{file_path}' to {new_color}.")
    except Exception as e:
        print(f"Error processing file '{file_path}': {e}")
    finally:
        document_name = os.path.basename(file_path)
        doc.Close(False)

def process_dwg_files_in_directory(directory, layer_name, new_color):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.dwg'):
                file_path = os.path.join(root, file)
                change_layer_color_in_dwg(file_path, layer_name, new_color)
                # Optional: Add a small delay to ensure AutoCAD processes the file correctly
                time.sleep(1) 

if __name__ == "__main__":
    directory = input("Enter the path of the directory: ")
    layer_name = input("Enter the name of the layer to change color: ")
    new_color = int(input("Enter the new color index (1 to 256): "))

    process_dwg_files_in_directory(directory, layer_name, new_color)
