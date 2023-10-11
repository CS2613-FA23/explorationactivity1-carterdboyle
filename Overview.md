# Package / Library Overview

The `open3d` package was selected for this Exploration Activity. It is the equivalent of OpenCV to computer vision, but for 3-D modelling. 

The purposes of this exploration were namely focuses on the visualization of and mesh creation from a point cloud `.ply` file.

The `numpy` library should be automatically included as a dependancy with the `open3d` library. `open3d` and `numpy` can be imported as follows:

```
import numpy as np
import open3d as o3d
```

## Functionality of `open3d` [[1]](http://www.open3d.org/docs/release/)

Open-3D is a modern library for 3D data processing and is used for supporting rapid development of software that deals with 3D data, with an optimized back-end for parallelization and secured front-end.

### Point clouds
The `read_point_cloud` function in `o3d.io` module is crucial for reading in the information from the `.ply` file. It attempts to read in the file and decode from the extension name.
``` py
  ply_pcl = o3d.io.read_point_cloud(<file_path>)
  print(ply_pcl) #This can show more details about the point cloud file
```
The `draw_geometries` function will visualize the point_cloud from various angles and zoom levels depending on the parameters.

A very important function relates to *voxel downsampling* which is a where a voxel grid is created uniformly to downsample a point cloud.
```
down_sampled_pcd = ply_pcl.voxel_down_sample(voxel_size=0.05)
```
The `estimate_normals` function is very important as well, and can help visualize the surfaces. The normals are calculated from the principal axis of nearby points using a covariance analysis.
Two key paramaters are the `radius` and `max_nn` which denote the search radius and maximum nearest neighbour, respectively. 

These normals can be accessed from `downsampled_pcd.normals`, which can then be transformed with `numpy` using `np.asarray(downsampled_pcd.normals)[:5, :])` for the first 5 points. `numpy` is often required for further processing down the line. 

The point cloud colours can be painted as well with `ply_pcl.paint_uniform_color([<r>, <g>, <b>])`.

### Meshes

In a similar fashion to point cloud data, a mesh can be loaded in from a file, so long as it is present in the file as:
```py
mesh = o3d.io.read_triangle_mesh("<file_path>")
print(mesh) # To view more mesh information
print('Vertices:') #
print(np.asarray(mesh.vertices)) #
print('Triangles:') #
print(np.asarray(mesh.triangles)) #
```
If a mesh has no color values or normals, then the mesh will not look very good, and is usually dark and hard to see. 
![image](https://github.com/CS2613-FA23/explorationactivity1-carterdboyle/assets/94463154/1f07cb58-b440-4513-a535-04e5a7da36d3)

The image can be rotated around, but still won't look good. The surface normalization is critical for observing a proper looking mesh.
```py
mesh.compute_vertex_normals()
```
After re-plotting using the visualizer: 

![image](https://github.com/CS2613-FA23/explorationactivity1-carterdboyle/assets/94463154/c6b97c0e-211a-4859-ad23-e1cb33df8530)

Visualizer can be configured from: 

```py
visualizer = o3d.visualizer.Visualizer()

""" where things can be added after creating a window... """

visualizer.create_window(window_name="Sample Window", width=500, height=500)
visualizer.add_geometry(mesh)

visualizer.run()
visualizer.destroy_window()
```
There is tons of additional functionality in `open3d` (like obtaining various properties as follows:) 

``` py
edge_manifold = mesh.is_edge_manifold(allow_boundary_edges=True)
    edge_manifold_boundary = mesh.is_edge_manifold(allow_boundary_edges=False)
    vertex_manifold = mesh.is_vertex_manifold()
    self_intersecting = mesh.is_self_intersecting()
    watertight = mesh.is_watertight()
    orientable = mesh.is_orientable()
```

Downsampling can be performed either with a pointcloud object or a mesh object. For meshes the `mesh.sample_points_uniformly(number_of_points=<#>)` is an option and for the pointcloud `ply_pcd.uniform_down_sample(<#>)` is an option. The latter was used in the purposes of decreasing the number of points in the massive data set in the sample program. 

On meshes this will return points which may not be the intended result, if a triangular mesh is still required then decimation can be performed:
```py
  mesh_simple = mesh_in.simplify_quadric_decimation(target_number_of_triangles=<#>)
```
## History and Choice of Package

This package was created in 2015 [[2]](http://www.open3d.org/paper.pdf), and has been in development since then. 

This package was selected as topic because it is important in finite element analysis and for creating 3D assets. The visualization of point cloud information is also used for surveying, drone mapping, geomatics, infrastructure analysis and virtual reality. I worked previously for a survey company where I did data processing on hydrographic data obtained from remote-operated vehicles that would use sonar technology to survey the ocean floor. The .xyz coordinate information could be used to create digital terrain models and engineering charts for the surveyors/clients.

## Learning Takeaways

Learning this library reinforced my understanding of the package managers available in python and how to create virtual environments. It also provided insight into the differences between Python versions. In the case of this library, my newer version of Python was not compatible with the package so there were issues with pip finding the package. I learned more about arrays in Python and how to access values and convert them to arrays in other forms like the ones found in `numpy`. 

I would recommend this package to someone if they were trying to visualize 3-D point data or if they were dealing with huge data sets and wanted to create smaller subsets of the point cloud or decimate a triangular mesh. It is simple to install and is easy to use when in a time crunch for manipulating data and visualizing. For reference, in a previous co-op I was programming with C++ and using VTK for this type of 3-D modelling and it was much more difficult to use. I would gladly keep using this package in the future, since we have just scratched the surface in terms of functionality as well. 
