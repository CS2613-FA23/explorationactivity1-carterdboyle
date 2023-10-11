import numpy as np
import open3d as o3d

# Animation callback function
def rotate_cb(visualizer):
    # We create a 3D rotation matrix - in radians
    rot = drgn_mesh.get_rotation_matrix_from_xyz((0, np.deg2rad(5), 0))

    # The rotation matrix is applied to the specified object - in our case the mesh. We can also specify the rotation pivot center
    drgn_mesh.rotate(rot, center=(0, 0, 0))

    # Update geometry and renderer to see any changes
    visualizer.update_geometry(drgn_mesh)
    visualizer.update_renderer()

if __name__ == '__main__':
    print(o3d.__version__)

    # Load mesh, together with setting the flag for post-processing to True, so the texture and material will be loaded
    mesh_path = 'data/fantasy_dragon.ply'
    drgn_mesh = o3d.io.read_triangle_mesh(mesh_path)

    print(drgn_mesh)

    print('Vertices...')
    print(np.asarray(drgn_mesh.vertices))
    print('Triangles...')
    print(np.asarray(drgn_mesh.triangles))

    # mesh contains triangles, lighting and textures
    mesh_faces = drgn_mesh.triangles
    mesh_uvs = drgn_mesh.triangle_uvs
    textures = drgn_mesh.textures

    drgn_mesh.compute_vertex_normals()

    # create a Visualizer window to hold the 3D object and listen for animation callbacks
    visualizer = o3d.visualization.Visualizer()
    # New window, where we can set the name, the width and height, as well as the position on the screen
    visualizer.create_window(window_name='Dragon Initial Mesh & 10 x Downsampled Pointcloud', width=750, height=750)

    # We call add_geometry to add a mesh or point cloud to the visualizer
    visualizer.add_geometry(drgn_mesh)

    # Other objects can be created as well - try to comment out the dragon mesh to see sphere more clearly
    # sphere_mesh = o3d.geometry.TriangleMesh.create_sphere(radius=10)

    # Compute either vertex or face normals
    # sphere_mesh.compute_vertex_normals()
    # Add the sphere to the visualizer
    # visualizer.add_geometry(sphere_mesh)
    # Move it from the center
    # sphere_mesh.translate((1, 0, 0))

    """ Is also possible to read in a point cloud and triangulate the mesh """

    drgn_pcld = o3d.io.read_point_cloud("data/fantasy_dragon.ply")

    # estimate radius for rolling ball
    """ Downsampling 10 x"""
    drgn_pcld = drgn_pcld.uniform_down_sample(10)
    distances = drgn_pcld.compute_nearest_neighbor_distance()
    drgn_pcld.estimate_normals()
    avg_dist = np.mean(distances)
    radius = 1.5 * avg_dist

    """ From point cloud - make the mesh, can take a minute"""
    """drgn_mesh2 = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
        drgn_pcld,
        o3d.utility.DoubleVector([radius, radius * 2])) """

    visualizer.add_geometry(drgn_pcld)
    # visualizer.add_geometry(drgn_mesh2)

    # Uncomment the below line to view full movement
    # visualizer.register_animation_callback(rotate_cb)
    # We run the visualizer
    visualizer.run()

    # Once the visualizer is closed destroy the window and clean up
    visualizer.destroy_window()


