# 🧮 MATH 215: Computational Linear Algebra

Welcome to my Computational Linear Algebra portfolio! This repository contains a collection of Python-based laboratory projects completed for **MATH 215**. 

Through these projects, I bridge the gap between theoretical linear algebra and practical programming, utilizing **Python, NumPy, Pandas, and Matplotlib** to solve complex, real-world data science and engineering problems.

---

## 🚀 Skills & Technologies
- **Languages:** Python
- **Libraries:** NumPy, Pandas, Matplotlib, SciPy, Scikit-Image
- **Core Concepts:** Matrix Factorizations (LU, QR, SVD), Iterative Methods, Least Squares, Principal Component Analysis (PCA), Eigenvector Centrality, Gram-Schmidt Orthogonalization, Image Compression.

---

## 📁 Repository Contents

Here is a comprehensive breakdown of the computational labs implemented in this repository:

### 1. Core Python & Mathematical Computing
- **Intro to Python I & II**
  - **Focus:** Foundational Python structures, control flow, functions, and vectorized operations using NumPy arrays for high-performance matrix computations.

### 2. Matrix Factorizations & Linear Systems
- **LU Decompositions**
  - **Focus:** Implemented LU decomposition from scratch and applied it with forward/backward substitution to efficiently solve systems of linear equations without computing expensive matrix inverses.
- **Gram-Schmidt and QR Decomposition**
  - **Focus:** Designed algorithms for the Gram-Schmidt orthogonalization process. Built a custom QR decomposition function and utilized it to construct a numerically stable linear system solver.

### 3. Iterative Methods & Stability
- **Iterative Methods**
  - **Focus:** Built Jacobi and Gauss-Seidel iterative solvers for sparse matrices where direct methods are computationally unfeasible.
- **Plotting, Iteration, and Roundoff Error**
  - **Focus:** Explored machine precision, catastrophic cancellation, and numerical instability limits in floating-point arithmetic. Visualized convergence rates of iterative processes using Matplotlib.

### 4. Data Science & Machine Learning Applications
- **Principal Component Analysis (PCA)**
  - **Focus:** Performed dimensionality reduction on high-dimensional healthcare datasets (predicting cancer likelihood based on survey data). Constructed covariance matrices, calculated dominant eigenvectors, and projected data into 2D subspaces to maximize variance and predict outcomes.
- **Least Squares I**
  - **Focus:** Developed linear regression models by solving normal equations to find the line of best fit for scattered datasets. 
- **Eigenvector Centrality**
  - **Focus:** Leveraged adjacency matrices and stochastic transition matrices to implement a foundational version of Google's PageRank algorithm, ranking web pages based on network topology.

### 5. Advanced Applications
- **SVD and Image Compression**
  - **Focus:** Computed the Singular Value Decomposition (SVD) of matrices. Applied lower-rank approximations to compress high-resolution image data while retaining vital visual information, evaluating mathematical trade-offs between memory footprint and image clarity.
- **Linear Transformations**
  - **Focus:** Visualized 2D and 3D linear transformations. Applied transformation matrices to manipulate geometric data structures mathematically.

---

## 💡 Why This Matters
Linear algebra is the mathematical engine powering modern machine learning, computer vision, and data science. This repository demonstrates not just an understanding of *how* these algorithms work mathematically, but the software engineering capability to **implement them from scratch in code**, addressing critical challenges like algorithmic efficiency, numerical stability, and floating-point error.

*Feel free to explore the Jupyter Notebooks (`.ipynb`) and Python scripts (`.py`) inside for detailed mathematical logic and code implementations!*
