# ExplorationActivity1

## Sample program

The sample program showcasing functionality of the chosen library, `open3d`, for use with python can be found in the `sample.py` file. 

The `open3d` library is massive and is useful for visualizing 3-D data. In this case, point cloud data, which is usual 3-D coordinates of a list of points.
The idea of the program is to create a mesh by connecting the 3-D points together to form a series of triangles, which in turn, creates a triangular mesh.
The program also shows how data of this type can be visualized. 

The sample program is configurable, and can show how a triangular mesh can be generated from an input pointcloud file, namely in the form of a .ply file.
The program also shows how a mesh can be downsampled, which is critical if there are many points in the pointcloud as the calculations can take a long time.

The data found in the `/data/` folder was found from [artec3d.com](https://www.artec3d.com/3d-models/fantasy-dragon)

## Installing the dependencies

In order to install `open3d` the following steps must be performed (if Python version > 3.10):
1.  The conda package manager must be installed by installing `miniconda` from [https://docs.conda.io/projects/miniconda/en/latest/]
2.  After installing for whichever OS, open up the Anaconda Prompt and enter the following commands to make an open3d python environment
     ```
     conda create -n open3d_env python=3.8
     conda activate open3d_env
     pip install open3d
     ```
3.  After creating this environment, navigate to folder wherever the sample.py file is located and run (ensuring you are still in the open3d_env)
    ```
    python sample.py
    ```

### If Python version is <= 3.10 a simple `pip install open3d` can be performed from the command line

## Typical inputs and output

Although `open3d` is very flexible in terms of inputs, only the .ply file types will be considered for simplicity. A sample file is included in the `/data/` directory, `fantasy_dragon.ply`.
This file is the input into the program, where the output is a downsampled pointcloud and a generated triangular surface from the pointcloud using the ball-rolling method of generation.

Output -

![image](https://github.com/CS2613-FA23/explorationactivity1-carterdboyle/assets/94463154/c094637a-5f41-4fbd-9d24-9639d4128b6a)

