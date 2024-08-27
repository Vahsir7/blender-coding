import bpy
import time

def raise_blocks(input_value):
    # Reset positions
    bpy.data.objects['r'].location.z = 0
    bpy.data.objects['w'].location.z = 0
    bpy.data.objects['x'].location.z = 0

    # Logic to raise blocks
    if input_value & 1:  # Check if the first bit is set
        bpy.data.objects['r'].location.z += 1
    if input_value & 2:  # Check if the second bit is set
        bpy.data.objects['w'].location.z += 1
    if input_value & 4:  # Check if the third bit is set
        bpy.data.objects['x'].location.z += 1

    # Update the text object with the input value
    text_obj = bpy.data.objects.get('Text')
    if text_obj and text_obj.type == 'FONT':  # Ensure the object is a text object
        text_obj.data.body = f"Given input: {input_value}"
    else:
        print("Text object not found or not a FONT type.")

raise_blocks(0)
