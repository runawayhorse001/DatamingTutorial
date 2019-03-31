.. _regression:


====================
Regression Algorithm
====================

.. note::

   A journey of a thousand miles begins with a single step -- old Chinese proverb


In statistical modeling, regression analysis focuses on investigating the relationship between a dependent variable and one or more independent variables. `Wikipedia Regression analysis`_

In data mining, Regression is a model to represent the relationship between the value of lable ( or target, it is numerical variable) and on one or more features (or predictors they can be numerical and categorical variables).


Ordinary Least Squares Regression (OLSR)
++++++++++++++++++++++++++++++++++++++++

Introduction
------------

Given that a data set :math:`{\displaystyle \{\,x_{i1},\ldots ,x_{in},y_{i}\}_{i=1}^{m}}` which contains n features
(variables) and m samples (data points), in simple linear regression model for modeling :math:`{\displaystyle m}` data points with one independent variable: :math:`{\displaystyle x_{i1}}`, the formula is given by:

      .. math::

         y_i = \beta_0 + \beta_1 x_{i1}, \text{where}, i= 1, \cdots m. 
       

In matrix notation, the data set is written as :math:`\X = [\x_1,\cdots, \x_n]` with
:math:`\x_i = {\displaystyle \{x_{\cdot i}\}_{i=1}^{n}}`, 
:math:`\By = {\displaystyle \{y_{i}\}_{i=1}^{m}}`
and :math:`\Bbeta^\top = {\displaystyle \{\beta_{i}\}_{i=1}^{m}}`. 
Then the normal equations are written as

      .. math::

         \By = \X \Bbeta.
         
How to solve it?
----------------



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




Linear Regression (LR)
++++++++++++++++++++++ 







TO DO .....


.. _Wikipedia Regression analysis: https://en.wikipedia.org/wiki/Regression_analysis
.. _Prelim Notes for Numerical Analysis: http://web.utk.edu/~wfeng1/doc/PrelimNum.pdf