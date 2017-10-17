.. _dim:

.. index:: Dimension Reduction Algorithms

==============================
Dimension Reduction Algorithms
==============================

What is dimension reduction?
+++++++++++++++++++++++++++++++++++++++++++

**In machine learning and statistics, dimensionality reduction or dimension reduction is the process of reducing the number of random variables under consideration,
via obtaining a set "uncorrelated" principle variables. It can be divided into feature selection and feature extraction.** https://en.wikipedia.org/wiki/Dimensionality_reduction


.. index:: Singular Value Decomposition 

Singular Value Decomposition (SVD)
+++++++++++++++++++++++++++++++++++++++++++

At here, I will recall the three types of the SVD method, since some authors confused 
the definitions of these SVD method. SVD method is important for the the dimension reduction 
algorithms, such as Truncated Singular Value Decomposition (tSVD) can be used to do the dimension 
reduction directly, and the Full Rank Singular Value Decomposition (SVD) can be applied to do Principal Component Analysis (PCA), since PCA is a specific case of SVD.


1. **Full Rank Singular Value Decomposition (SVD)**

 Suppose :math:`{\bf X}\in\mathbb{R}^{n\times p}, (p<n)`, then 

 .. math::
    :label: svd

	\underbracket{\bf X}_{n\times p} =\underbracket{\bf U}_{n\times n} \underbracket{\bf\Sigma}_{n\times p} \underbracket{{\bf V}^T}_{p\times p},

 is called a full rank **SVD** of :math:`{\bf X}` and 

 * :math:`\sigma_i`-- Sigular calues and :math:`{\bf\Sigma}=diag(\sigma_1,\sigma_2, \cdots, \sigma_p)\in \mathbb{R}^{n\times p}`
 * :math:`u_i`-- left singular vectors, :math:`{\bf U}=[u_1,u_2, \cdots, u_n]` and  :math:`{\bf U}` is unitary.
 * :math:`v_i`-- right singular vectors, :math:`{\bf V}=[v_1,v_2, \cdots, v_p]` and  :math:`{\bf V}` is unitary.

  .. _fig_svd:
  .. figure:: images/svd.png
    :align: center

    Singular Value Decomposition 

2. **Reduced Singular Value Decomposition (rSVD)**

 Suppose :math:`{\bf X}\in\mathbb{R}^{n\times p},(n<p)`, then 

 .. math::
    :label: rsvd

	\underbracket{\bf X}_{n\times p} =\underbracket{\bf \hat{U}}_{n\times p} \underbracket{\bf\hat{\Sigma}}_{p\times p} \underbracket{{\bf \hat{V}}^T}_{p\times p},

 is called a Reduced Singular Value Decomposition **rSVD** of :math:`{\bX}` and 

 * :math:`\sigma_i`-- Sigular calues and :math:`{\bf\hat{\Sigma}}=diag(\sigma_1,\sigma_2, \cdots, \sigma_p)\in \mathbb{R}^{p\times p}`
 * :math:`u_i`-- left singular vectors, :math:`{\bf \hat{U}}=[u_1,u_2, \cdots, u_p]` is column-orthonormal matrix.
 * :math:`v_i`-- right singular vectors, :math:`{\bf \hat{V}}=[v_1,v_2, \cdots, v_p]` is column-orthonormal matrix.
  

3. **Truncated Singular Value Decomposition (tSVD)**

 Suppose :math:`{\bf X}\in\mathbb{R}^{n\times p},(r<p)`, then 

 .. math::
    :label: tsvd

	\underbracket{\bf X}_{n\times p} =\underbracket{\bf \hat{U}}_{n\times r} \underbracket{\bf\hat{\Sigma}}_{r\times r} \underbracket{{\bf \hat{V}}^T}_{r\times p},

 is called a Truncated Singular Value Decomposition **tSVD** of :math:`{\bf X}` and 

 * :math:`\sigma_i`-- Sigular calues and :math:`{\bf\hat{\Sigma}}=diag(\sigma_1,\sigma_2, \cdots, \sigma_r)\in \mathbb{R}^{r\times r}`
 * :math:`u_i`-- left singular vectors, :math:`{\bf \hat{U}}=[u_1,u_2, \cdots, u_r]` is column-orthonormal matrix.
 * :math:`v_i`-- right singular vectors, :math:`{\bf \hat{V}}=[v_1,v_2, \cdots, v_p]` is column-orthonormal matrix.

  .. _fig_tsvd:
  .. figure:: images/tsvd.png
    :align: center

    Truncated Singular Value Decomposition 

   
Figure :ref:`fig_tsvd` indictes that the the dimension of :math:`{\bf \hat{U}}` is smaller than :math:`{\bf X}`. We can use this property to do the dimension reduction. But, usually, we will use SVD 
to compute the Principal Components. We will learn more details in next section.

.. index:: Principal Component Analysis

Principal Component Analysis (PCA)
++++++++++++++++++++++++++++++++++

Usually, there are two ways to implement the PCA. Principal Component Analysis (PCA) is a specific case of SVD.

 .. math::
    :label: test

    \underbracket{\bX}_{n\times p} =\hU


.. index:: Independent Component Analysis

Independent Component Analysis (ICA)
++++++++++++++++++++++++++++++++++++

.. index:: Nonnegative matrix factorization

Nonnegative matrix factorization (NMF)
++++++++++++++++++++++++++++++++++++++

TO DO......