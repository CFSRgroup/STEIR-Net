# STEIR-Net
The organization of the repo is as follows

## ICRS-framework
There are two py files which used to build the GUI corresponding to the two datasets. (SEED & SEED-IV)

## label
File **orginal label** contains the instantaneous affective intensity labels of two datasets. These labels are collected by ICRS-framework. 

- SEED: There are three sessions and the video clips of each session are the same. So, there are 20 (individuals) * 15 (clips) labels in total.
- SEED-IV: There are three session and the videos clips of each session are different. So, there are 3 (sessions) * 20 (individuals) * 24 (clips) labels in total.

File **preprocessed label** contains the preprocessed label of two datasets. The preprocessing method is mentioned in the paper, if interested please refer to the paper

## model
The source code of the STEIR-Net.