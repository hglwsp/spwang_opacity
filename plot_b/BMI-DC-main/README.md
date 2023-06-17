# Synthesizing invariant barrier certificates

[![Mathematica Notebook](https://wolfr.am/lA6mO5hv)](https://github.com/Chenms404/BMI-DC/blob/main/BMI-Invariant.nb)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4725465.svg)](https://doi.org/10.5281/zenodo.4725465)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Chenms404/BMI-DC/blob/main/LICENSE)

This prototypical implementation (as a *Mathematica* Notebook) is dedicated to synthesizing invariant barrier certificates via difference-of-convex programming. It takes as input a differential dynamical system together with an initial and an unsafe set, and tries to find an invariant barrier certificate B(x) (in the form of a given template) that suffices to prove unbounded-time safety of the system.

For more technical details, please refer to our CAV'21 paper:

> Qiuye Wang, Mingshuai Chen, Bai Xue, Naijun Zhan, Joost-Pieter Katoen:
Synthesizing Invariant Barrier Certificates via Difference-of-Convex Programming. In Proc. of CAV'21, to appear.

## Information on the implementation

Current version: v1.0</br>
Validated on platform: Wolfram *Mathematica* 12.1.0.0, 64 bit-CentOS Linux-7.8.2003

Corresponding e-mail: chenms@cs.rwth-aachen.de</br>
List of contributors: Mingshuai Chen, Qiuye Wang, Bai Xue, Naijun Zhan, Joost-Pieter Katoen

Comments and bug-reports are highly appreciated.</br>
© 2021 Lehrstuhl für Informatik 2, RWTH Aachen University. [MIT Licensed](https://github.com/Chenms404/BMI-DC/blob/main/LICENSE).

## How to use the notebook?

1. Install [Wolfram Mathematica](https://www.wolfram.com/mathematica/).
2. Launch the notebook in *Mathematica*:
   ```bash
   cd DIRECTORY_TO_THE_NOTEBOOK
   mathematica BMI-Invariant.nb &
   ```
3. Run the implementation on a collection of benchmark examples simply by clicking in the **Evaluation** panel **Evaluate Notebook**. This may take around 10mins. You can also run a single cell (where your cursor is) by pressing `SHIFT+ENTER`.
4. Test your own examples in the same vein as the provided examples (with explanations on the arguments) in the notebook.
5. Enjoy.
