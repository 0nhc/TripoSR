import trimesh
import pyrender

def visualize_obj(file_path):
    # Load the .obj file using trimesh
    mesh = trimesh.load(file_path)
    if not isinstance(mesh, trimesh.Trimesh):
        raise ValueError("The provided file is not a valid .obj mesh.")

    # Create a pyrender scene
    scene = pyrender.Scene()
    mesh = pyrender.Mesh.from_trimesh(mesh)
    scene.add(mesh)

    # Create a viewer
    viewer = pyrender.Viewer(scene, use_raymond_lighting=True)
    return viewer

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python visualize_obj.py <path_to_obj_file>")
        sys.exit(1)

    obj_file_path = sys.argv[1]
    visualize_obj(obj_file_path)

# Example usage: python visualize_obj.py path/to/your/model.obj