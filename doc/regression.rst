.. _regression:


====================
Regression Algorithm
====================

.. note::

   A journey of a thousand miles begins with a single step -- old Chinese proverb


In statistical modeling, regression analysis focuses on investigating the relationship between a dependent variable and one or more independent variables. `Wikipedia Regression analysis`_

In data mining, Regression is a model to represent the relationship between the value of lable ( or target, it is numerical variable) and on one or more features (or predictors they can be numerical and categorical variables).

Introduction
++++++++++++

Given that a data set :math:`{\displaystyle \{\,x_{i1},\ldots ,x_{in},y_{i}\}_{i=1}^{m}}` which contains n features (variables) and m samples (data points), in simple linear regression model for modeling :math:`{\displaystyle m}` data points with :math:`j` independent variables: :math:`{\displaystyle x_{ij}}`, the formula is given by:

      .. math::

         y_i = \beta_0 + \beta_j x_{ij}, \text{where}, i= 1, \cdots m, j= 1, \cdots n. 
       

In matrix notation, the data set is written as :math:`\X = [\x_1,\cdots, \x_n]` with
:math:`\x_j = {\displaystyle \{x_{ij}\}_{i=1}^{m}}`, 
:math:`\y = {\displaystyle \{y_{i}\}_{i=1}^{m}}` (see Fig. :ref:`fig_fm`)
and :math:`\Bbeta^\top = {\displaystyle \{\beta_{j}\}_{j=1}^{n}}`. 
Then the matrix format equation is written as

      .. math::
      	 :label: eq_Ax

         \y = \X \Bbeta.
         

.. _fig_fm:
.. figure:: images/fm.png
   :align: center

   Feature matrix and label


Ordinary Least Squares Regression (OLSR)
++++++++++++++++++++++++++++++++++++++++



How to solve it?
----------------

Theoretically, you can apply all the following methods to solve :eq:`eq_Ax` if you matrix :math:`\X` have a good properties.

#. Direct Methods (For more information please refer to my `Prelim Notes for Numerical Analysis`_)


	* For squared or rectangular matrices

		- Singular Value Decomposition 
		- Gram-Schmidt orthogonalization 
		- QR Decomposition 

	* For squared matrices

	    - LU Decomposition
	    - Cholesky Decomposition
	    - Regular Splittings


#. Iterative Methods

	* Stationary cases iterative method 

		- Jacobi Method 
		- Gauss-Seidel Method
		- Richardson Method	
		- Successive Over Relaxation (SOR) Method 

	* Dynamic cases iterative method 

		- Chebyshev iterative Method 
		- Minimal residuals Method
		- Minimal correction iterative method 
		- Steepest Descent Method
		- Conjugate Gradients Method


Ordinary Least Squares
----------------------

In mathematics, :eq:`eq_Ax` is a overdetermined system.  The method of ordinary least squares can be used to find an approximate solution to overdetermined systems. For the system overdetermined system :eq:`eq_Ax`, the least squares formula is obtained from the problem

.. math::
	:label: eq_minAx

	{\displaystyle \min _{x}  ||\X \Bbeta-\y||} ,

the solution of which can be written with the normal equations:

.. math::
	:label: eq_solAx

	\Bbeta  = (\X^T\X)^{-1}\X^T\y

where :math:`{\displaystyle {\mathrm {T} }}` indicates a matrix transpose, provided :math:`{\displaystyle (\X^{\mathrm {T} }\X)^{-1}}` exists (that is, provided :math:`\X` has full column rank).

.. note::

   Actually, :eq:`eq_solAx` is derivated by the following way: multiply :math:`\X^T` on side of :eq:`eq_Ax` and then multiply :math:`(\X^T\X)^{-1}` on both side of the former result.

Linear Regression (LR)
++++++++++++++++++++++ 







TO DO .....


.. _Wikipedia Regression analysis: https://en.wikipedia.org/wiki/Regression_analysis
.. _Prelim Notes for Numerical Analysis: http://web.utk.edu/~wfeng1/doc/PrelimNum.pdf