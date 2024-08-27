import bpy

def apply_action(action_name):
    # Get the armature object
    armature = bpy.context.active_object
    
    # Switch to Pose Mode
    bpy.ops.object.mode_set(mode='POSE')
    
    # Set the action to the armature
    action = bpy.data.actions.get(action_name)
    if action:
        armature.animation_data.action = action
    else:
        print(f"Action '{action_name}' not found.")

def switch_pose_based_on_input(input_value):
    if input_value == "Fist":
        apply_action('fist')
    elif input_value == "Point":
        apply_action('point')
    elif input_value == "Victory":
        apply_action('victory')
    elif input_value == "ThumbsUp":
        apply_action('ThumbsUp')
    
    text_obj = bpy.data.objects.get('Text')
    if text_obj and text_obj.type == 'FONT':  # Ensure the object is a text object
        text_obj.data.body = f"Current action: {input_value}"
    else:
        print("Text object not found or not a FONT type.")


actions = ["Fist","Point","Victory","ThumbsUp"]
print("Start")
switch_pose_based_on_input(actions[1])