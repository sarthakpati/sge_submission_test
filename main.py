#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

parallel_compute_command = 'qsub -b y -l gpu -l h_vmem=32G -cwd -o ${outputDir}/$JOB_ID.stdout -e ${outputDir}/$JOB_ID.stderr ./sge_wrapper ' # command to prepend 

currentOutputFolder = './outputDir/0/' # the output directory for a single fold
parallel_compute_command_actual = parallel_compute_command.replace('${outputDir}', currentOutputFolder)

print(parallel_compute_command_actual)
command = parallel_compute_command_actual + ' python -m ./sleep.py' # construct the command to call

subprocess.Popen(command, shell=True).wait() # call the command