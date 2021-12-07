# A MPI-based HelloWorld toy model for CyberGIS-Compute V2

This repo implemented a MPI-based HelloWorld toy model for CyberGIS-Compute V2. Model developers who may want to contribute their own models to CyberGIS-Compute can use this as an example.

For end-users, an example notebook is provides for running the toy model on a HPC resource: Open with CyberGIS-Jupyter for Water (CJW) <a href="http://go.illinois.edu/cybergis-jupyter-water/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcybergis%2Fcybergis-compute-mpi-helloworld&urlpath=tree%2Fcybergis-compute-mpi-helloworld%2Fmpi-hello-world.ipynb&branch=main" target="_blank">HERE</a>


## mainfest.json

Supported HPCs are listed by key "supported_hpc" and default HPC by key "default_hpc";

The key "slurm_input_rules" lists ranges and limits of different slurm flags will be shown to end-users with SDK GUI; For a full list of avaiable keys see https://github.com/cybergis/cybergis-compute-core/blob/v2/src/types.ts#L70

The key "pre_processing_stage", "execution_stage" and "post_processing_stage" specify the commands (and scripts) to run in preprocessing, model execution and postprocessing stages;

The key "container" lists the singularity container to use on HPC (placed on HPC already);

Other kyes for metadata: "name", "description", "estimated_runtime"

## preprocessing.py

Will be called in a single process for preprocessing data before parallel model run.

## main.py

This script is called inside the singularity container in a MPI environment for executing predefined HelloWorld models. Each rank prints out its rank id, total size of the cluster and processor name. The rank 0 prints out environment variables passed in including user-specific parameters and copies all data from "data" folder to "resulsts" folder to indicate it is able to access user-uploaded data.

## postprocessing.py

Will be called in a single process for preprocessing data after parallel model run.

## "images" folder

This folder contains the dockerfile that builds the mpi environment image and a singlarity DEF script that importes the docker image and converts to singularity container.

