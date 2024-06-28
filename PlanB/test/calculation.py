import numpy as np

def calculate_visibility(A, B, fov=90):
    """
    Calculate the visibility of vector B from the origin of vector A in 6 directions (front, back, left, right, up, down)
    based on a specified field of view (fov) angle.
    
    Args:
        A (np.array): 3D coordinates of vector A.
        B (np.array): 3D coordinates of vector B.
        fov (float): Field of view angle in degrees. Default is 90 degrees.
        
    Returns:
        dict: A dictionary with visibility percentages for each direction.
    """
    # Calculate the relative position of B with respect to A
    relative_position = np.array(B) - np.array(A)
    relative_position = relative_position / np.linalg.norm(relative_position)  # Normalize the vector
    
    # Convert fov to radians
    fov_rad = np.deg2rad(fov / 2)
    
    # Calculate the visibility for each direction
    visibility = {}
    
    # Front (positive z direction)
    visibility['front'] = max(0, np.dot(relative_position, [0, 0, 1]) / np.cos(fov_rad))
    
    # Back (negative z direction)
    visibility['back'] = max(0, np.dot(relative_position, [0, 0, -1]) / np.cos(fov_rad))
    
    # Left (negative x direction)
    visibility['left'] = max(0, np.dot(relative_position, [-1, 0, 0]) / np.cos(fov_rad))
    
    # Right (positive x direction)
    visibility['right'] = max(0, np.dot(relative_position, [1, 0, 0]) / np.cos(fov_rad))
    
    # Up (positive y direction)
    visibility['up'] = max(0, np.dot(relative_position, [0, 1, 0]) / np.cos(fov_rad))
    
    # Down (negative y direction)
    visibility['down'] = max(0, np.dot(relative_position, [0, -1, 0]) / np.cos(fov_rad))
    
    # Normalize visibility to a percentage scale
    for key in visibility:
        visibility[key] = min(100, visibility[key] * 100)
    
    return visibility

def visibility_matrix(visibility):
    """
    Convert the visibility dictionary to a 3x3 matrix.
    
    Args:
        visibility (dict): A dictionary with visibility percentages for each direction.
        
    Returns:
        np.array: A 3x3 matrix representing the visibility.
    """
    matrix = np.zeros((3, 3))
    # Up direction
    matrix[0, 1] = visibility['up']
    # Left and Right directions
    matrix[1, 0] = visibility['left']
    matrix[1, 2] = visibility['right']
    # Front and Back directions
    matrix[2, 1] = visibility['front']
    matrix[0, 1] = visibility['back']
    return matrix

def is_within_angle(A, B, angle_threshold):
    """
    Check if vector B is within the specified angle from vector A's direction.
    
    Args:
        A (np.array): 3D coordinates of vector A.
        B (np.array): 3D coordinates of vector B.
        angle_threshold (float): Angle threshold in degrees.
    
    Returns:
        bool: True if B is within the angle threshold from A, False otherwise.
    """
    # Calculate the relative position of B with respect to A
    relative_position = np.array(B) - np.array(A)
    
    # Normalize the vectors
    A_norm = A / np.linalg.norm(A)
    B_norm = relative_position / np.linalg.norm(relative_position)
    
    # Calculate the angle between A and B in radians
    dot_product = np.dot(A_norm, B_norm)
    angle_rad = np.arccos(np.clip(dot_product, -1.0, 1.0))
    
    # Convert the angle to degrees
    angle_deg = np.rad2deg(angle_rad)
    
    # Check if the angle is within the threshold
    return angle_deg <= angle_threshold

def adjusted_visibility_matrix(A, B, angle_threshold, fov=90):
    """
    Calculate the visibility matrix and adjust it based on the angle threshold.
    
    Args:
        A (np.array): 3D coordinates of vector A.
        B (np.array): 3D coordinates of vector B.
        angle_threshold (float): Angle threshold in degrees.
        fov (float): Field of view angle in degrees. Default is 90 degrees.
        
    Returns:
        np.array: A 3x3 matrix representing the adjusted visibility.
    """
    if not is_within_angle(A, B, angle_threshold):
        return np.zeros((3, 3))  # Return a zero matrix if B is not within the angle threshold
    
    visibility = calculate_visibility(A, B, fov)
    return visibility_matrix(visibility)


def calculate_Position(A, B):

    # Calculate the relative position of B with respect to A
    relative_position = np.array(B) - np.array(A)
    relative_position = relative_position / np.linalg.norm(relative_position)  # Normalize the vector
    
    # Calculate the visibility for each direction
    position = {}
    
    # Front (positive z direction)
    position['front'] = max(0, np.dot(relative_position, [0, 0, 1]))
    
    # Back (negative z direction)
    position['back'] = max(0, np.dot(relative_position, [0, 0, -1]))
    
    # Left (negative x direction)
    position['left'] = max(0, np.dot(relative_position, [-1, 0, 0]))
    
    # Right (positive x direction)
    position['right'] = max(0, np.dot(relative_position, [1, 0, 0]))
    
    # Up (positive y direction)
    position['up'] =  max(0, np.dot(relative_position, [0, 1, 0]))
    
    # Down (negative y direction)
    position['down'] = max(0, np.dot(relative_position, [0, -1, 0]))
    
    # Normalize visibility to a percentage scale
    for key in position:
        position[key] = min(100, position[key] * 100)
    
    return position


if __name__ == "__main__":
    print("testRun")
    # Example usage
    #[左右,上下,前後]
    A = [0, 0, 1]
    B = [0, 0, 2]
    fov=90
    angle_threshold = 45  # Set the angle threshold to 45 degrees
    adjusted_matrix = adjusted_visibility_matrix(A, B, angle_threshold,fov)
    print("Adjusted visibility matrix:\n", adjusted_matrix)
