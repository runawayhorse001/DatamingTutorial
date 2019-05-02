.. _pre:

.. index:: Pre-processing procedures

.. |nb| replace:: ``Jupyter Notebook``
.. |py| replace:: ``Python``
.. |pyc| replace:: ``:: Python Code:``
.. |out| replace:: ``:: Ouput:``
.. |eg| replace:: ``:: Example:``
.. |syn| replace:: ``::syntax:``

=========================
Pre-processing procedures
=========================

.. note::

   **Well begun is half done** -- old Chinese proverb

In my opinion,  preprocessing is crucial for the data mining algorithms. If you get a good pre-processing, you will definitely get a beeter result. In this section, we will learn how to do a proper pre-processing in  **R** and **Python**.

.. index:: rough preprocessing

Rough Pre-processing 
++++++++++++++++++++

dealing with missing data
-------------------------

Usually, we have two popular way to deal with the missing data: replacing by 0 or replacing by mean value.

.. content-tabs:: right-col

    .. tab-container:: python
        :title: Python

        * dealing with missing data in **Python**  

        |eg| 

        .. code-block:: python

			import pandas as pd

			d = {'A': [1, 0, None, 3],
			     'B': [1, 0, 0, 0],
			     'C': [4, None, 7, 8]}

			df = pd.DataFrame(d)
			print(df)

			# fill missing numerical value with 0
			print(df.fillna(0))

			# fill missing numerical value with mean
			df = df.fillna(df.mean())
			print(df)


        |out|

        .. code-block:: python

			     A  B    C
			0  1.0  1  4.0
			1  0.0  0  NaN
			2  NaN  0  7.0
			3  3.0  0  8.0
			     A  B    C
			0  1.0  1  4.0
			1  0.0  0  0.0
			2  0.0  0  7.0
			3  3.0  0  8.0
			          A  B         C
			0  1.000000  1  4.000000
			1  0.000000  0  6.333333
			2  1.333333  0  7.000000
			3  3.000000  0  8.000000


    .. tab-container:: r
        :title: R

        * dealing with missing data in **R**

        |eg| 

        .. code-block:: r

			library(dplyr)

			df = data.frame(A = c(1, 0, NA, 3), 
			                B = c(1, 0, 0, 0), 
			                C = c(4, NA, 7, 8))
			df

			na2zero <- function(data){
			  data %>% mutate_all(~replace(., is.na(.), 0))
			}

			na2zero(df)

			na2mean <- function(data){
			  for(i in 1:ncol(data)){
			    data[is.na(data[,i]), i] <- mean(data[,i], na.rm = TRUE)
			  }
			  return(data)
			}

			na2mean(df)


        |out| 

        .. code-block:: r

			> df
			   A B  C
			1  1 1  4
			2  0 0 NA
			3 NA 0  7
			4  3 0  8

			> na2zero(df)
			  A B C
			1 1 1 4
			2 0 0 0
			3 0 0 7
			4 3 0 8

			> na2mean(df)
			         A B        C
			1 1.000000 1 4.000000
			2 0.000000 0 6.333333
			3 1.333333 0 7.000000
			4 3.000000 0 8.000000



 



Source Code for This Section
++++++++++++++++++++++++++++

The code for this section is available for download for `R <../code/loaddata.R>`_, for `Python <../code/loadData.py>`_, 
 * R Source code

  .. literalinclude:: ../code/loaddata.R
     :language: r

 * Python Source code

  .. literalinclude:: ../code/loadData.py
