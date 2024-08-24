# Useful SLURM Commands

This is a collection of useful SLURM commands that I have found useful when running jobs on the HPC2 node.

You can find more information about SLURM commands in the [SLURM documentation](https://slurm.schedmd.com/squeue.html).

## Submitting a Job

To submit a job to the HPC2 node, you will need to create a job script. Below is an example of a job script that you can
use to submit a job to the HPC2 node.

The file is called `job_script.sh` and contains the following code:

```bash
#!/bin/bash -l
#SBATCH -J job_name
#SBATCH --mem=150G
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:2
#SBATCH --time=15-00:00:00
#SBATCH --partition=gpu-qi
#SBATCH --mail-user=nsabzwari@ucdavis.edu
#SBATCH --mail-type=ALL
#SBATCH -o training_irf_jobs/training_irf_job-%j.output
#SBATCH -e training_irf_jobs/training_irf_job-%j.error

# Run the Python script with the input file
module load conda3/4.X
conda activate regression_dl
python training_irf_models.py
```

Comment lines with `SBATCH` are the parameters that you can set for your job. The parameters that you can set are:

- `-J job_name`: The name of the job
- `--mem=150G`: The amount of memory that you want to allocate to the job
- `--cpus-per-task=4`: The number of CPUs that you want to allocate to the job
- `--gres=gpu:2`: The number of GPUs that you want to allocate to the job
- `--time=15-00:00:00`: The amount of time that you want to allocate to the job
- `--partition=gpu-qi`: The partition that you want to allocate the job to
- `--mail-user=nsabzwari@ucdavis.edu`: The email address that you want to receive notifications at.
    - **Note**: After speaking with IT, this directive is not functional on the HPC2 node.
- `--mail-type=ALL`: The type of notifications that you want to receive
    - **Note**: After speaking with IT, this directive is not functional on the HPC2 node.
- `-o training_irf_jobs/training_irf_job-%j.output`: The output file for the job
- `-e training_irf_jobs/training_irf_job-%j.error`: The error file for the job

After you have created the job script, you can submit the job to the HPC2 node using the following command:

```bash
sbatch job_script.sh
```

This file should be sufficient for our purposes. If you need to add more parameters, you can refer to
the [SLURM documentation](https://slurm.schedmd.com/sbatch.html).

## Monitoring Jobs

To monitor the jobs that you have submitted to the HPC2 node, you can use the following commands:

- `squeue`: This command will show you all of the jobs that are currently running on the HPC2 node
    - `squeue -u nsabzwar`: This command will show you all of the jobs that are currently running on the HPC2 node for
      the user `nsabzwar`
    - `squeue -A gpu-qi`: This command will show you all of the jobs that are currently running on the HPC2 node for the
      partition `gpu-qi`
- `sacct`: This command will show you the status of the jobs that you have submitted to the HPC2 node
    - `sacct -u nsabzwar`: This command will show you the status of the jobs that you have submitted to the HPC2 node
      for the user `nsabzwar`
    - `sacct -X -o jobId,start,end,state`: This command will show you the job ID, start time, end time, and state of the
      jobs that you have submitted to the HPC2 node
- `scontrol show job <job_id>`: This command will show you the details of a specific job that you have submitted to the
  HPC2 node
    - `scontrol show job 12345`: This command will show you the details of the job with the job ID `12345`

You can find more information about these commands in the [SLURM documentation](https://slurm.schedmd.com/squeue.html).

## Cancelling Jobs

To cancel a job that you have submitted to the HPC2 node, you can use the following command:

- `scancel <job_id>`: This command will cancel the job with the job ID `<job_id>`
    - `scancel 12345`: This command will cancel the job with the job ID `12345`

You can find more information about this command in the [SLURM documentation](https://slurm.schedmd.com/scancel.html).