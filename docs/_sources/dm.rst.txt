.. _dm:

=================
Data Manipulation 
=================


Combining DataFrame
+++++++++++++++++++

Mutating Joins
--------------

0. Datasets

.. content-tabs:: right-col

    .. tab-container:: python
        :title: Python

        .. code-block:: python

			import pandas as pd
			left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
			                    'B': ['B0', 'B1', 'B2', 'B3'],
			                    'C': ['C0', 'C1', 'C2', 'C3'],
			                    'D': ['D0', 'D1', 'D2', 'D3']},
			                    index=[0, 1, 2, 3])

			right = pd.DataFrame({'A': ['A0', 'A1', 'A6', 'A7'],
			                       'F': ['B4', 'B5', 'B6', 'B7'],
			                       'G': ['C4', 'C5', 'C6', 'C7'],
			                       'H': ['D4', 'D5', 'D6', 'D7']},
			                       index=[4, 5, 6, 7])

			print(left)
			print(right)

			    A   B   C   D
			0  A0  B0  C0  D0
			1  A1  B1  C1  D1
			2  A2  B2  C2  D2
			3  A3  B3  C3  D3
			    A   F   G   H
			4  A0  B4  C4  D4
			5  A1  B5  C5  D5
			6  A6  B6  C6  D6
			7  A7  B7  C7  D7


    .. tab-container:: r
        :title: R

        .. code-block:: r


			left = data.frame(A = c('A0', 'A1', 'A2', 'A3'), 
			                  B = c('B0', 'B1', 'B2', 'B3'), 
			                  C = c('C0', 'C1', 'C2', 'C3'),
			                  D = c('D0', 'D1', 'D2', 'D3'))
			left

			right = data.frame(A = c('A0', 'A1', 'A6', 'A7'), 
			                   F = c('B4', 'B5', 'B6', 'B7'), 
			                   G = c('C4', 'C5', 'C6', 'C7'),
			                   H = c('D4', 'D5', 'D6', 'D7'))
			right        

			> left
			   A  B  C  D
			1 A0 B0 C0 D0
			2 A1 B1 C1 D1
			3 A2 B2 C2 D2
			4 A3 B3 C3 D3

			> right
			   A  F  G  H
			1 A0 B4 C4 D4
			2 A1 B5 C5 D5
			3 A6 B6 C6 D6
			4 A7 B7 C7 D7

1. Left join 

.. content-tabs:: right-col

    .. tab-container:: python
        :title: Python

        * Code:

        .. code-block:: python

			# left join
			left_join = left.merge(right, on='A', how='left')
			print(left_join)

        * Result:

        .. code-block:: python

			    A   B   C   D    F    G    H
			0  A0  B0  C0  D0   B4   C4   D4
			1  A1  B1  C1  D1   B5   C5   D5
			2  A2  B2  C2  D2  NaN  NaN  NaN
			3  A3  B3  C3  D3  NaN  NaN  NaN


    .. tab-container:: r
        :title: R

        * Code:

        .. code-block:: r

			library(dplyr)

			# left join
			dplyr::left_join(left,right, by = 'A')
			# or 
			left %>% left_join(right, by ='A')

        * Result:

        .. code-block:: r

			> dplyr::left_join(left,right, by = 'A')
			   A  B  C  D    F    G    H
			1 A0 B0 C0 D0   B4   C4   D4
			2 A1 B1 C1 D1   B5   C5   D5
			3 A2 B2 C2 D2 <NA> <NA> <NA>
			4 A3 B3 C3 D3 <NA> <NA> <NA>
			Warning message:
			Column `A` joining factors with different levels, coercing to character vector 
			> left %>% left_join(right, by ='A')
			   A  B  C  D    F    G    H
			1 A0 B0 C0 D0   B4   C4   D4
			2 A1 B1 C1 D1   B5   C5   D5
			3 A2 B2 C2 D2 <NA> <NA> <NA>
			4 A3 B3 C3 D3 <NA> <NA> <NA>

2. Right join 

.. content-tabs:: right-col

    .. tab-container:: python
        :title: Python

        * Code:

        .. code-block:: python

			# right join
			right_join = left.merge(right, on='A', how='right')
			print(right_join)

        * Result:

        .. code-block:: python

			    A    B    C    D   F   G   H
			0  A0   B0   C0   D0  B4  C4  D4
			1  A1   B1   C1   D1  B5  C5  D5
			2  A6  NaN  NaN  NaN  B6  C6  D6
			3  A7  NaN  NaN  NaN  B7  C7  D7


    .. tab-container:: r
        :title: R

        * Code:

        .. code-block:: r

			library(dplyr)

			# right join
			dplyr::right_join(left,right, by = 'A')
			left %>% right_join(right, by ='A')
       
        * Result:

        .. code-block:: r

			> dplyr::right_join(left,right, by = 'A')
			   A    B    C    D  F  G  H
			1 A0   B0   C0   D0 B4 C4 D4
			2 A1   B1   C1   D1 B5 C5 D5
			3 A6 <NA> <NA> <NA> B6 C6 D6
			4 A7 <NA> <NA> <NA> B7 C7 D7
			Warning message:
			Column `A` joining factors with different levels, coercing to character vector 
			> left %>% right_join(right, by ='A')
			   A    B    C    D  F  G  H
			1 A0   B0   C0   D0 B4 C4 D4
			2 A1   B1   C1   D1 B5 C5 D5
			3 A6 <NA> <NA> <NA> B6 C6 D6
			4 A7 <NA> <NA> <NA> B7 C7 D7
			Warning message:
			Column `A` joining factors with different levels, coercing to character vector 

3. Inner join 

.. content-tabs:: right-col

    .. tab-container:: python
        :title: Python

        * Code:

        .. code-block:: python

			# inner join
			inner_join = left.merge(right, on='A', how='inner')
			print(inner_join)

        * Result:

        .. code-block:: python

			    A   B   C   D   F   G   H
			0  A0  B0  C0  D0  B4  C4  D4
			1  A1  B1  C1  D1  B5  C5  D5


    .. tab-container:: r
        :title: R

        * Code:

        .. code-block:: r

			library(dplyr)

			# inner join
			dplyr::inner_join(left,right, by = 'A')
			left %>% inner_join(right, by ='A')

        * Result:

        .. code-block:: r

			> dplyr::inner_join(left,right, by = 'A')
			   A  B  C  D  F  G  H
			1 A0 B0 C0 D0 B4 C4 D4
			2 A1 B1 C1 D1 B5 C5 D5
			Warning message:
			Column `A` joining factors with different levels, coercing to character vector 
			> left %>% inner_join(right, by ='A')
			   A  B  C  D  F  G  H
			1 A0 B0 C0 D0 B4 C4 D4
			2 A1 B1 C1 D1 B5 C5 D5
			Warning message:
			Column `A` joining factors with different levels, coercing to character vector 

4. Full join 

.. content-tabs:: right-col

    .. tab-container:: python
        :title: Python

        * Code:

        .. code-block:: python

			# full join
			full_join = left.merge(right, on='A', how='outer')
			print(full_join)

        * Result:

        .. code-block:: python

			    A    B    C    D    F    G    H
			0  A0   B0   C0   D0   B4   C4   D4
			1  A1   B1   C1   D1   B5   C5   D5
			2  A2   B2   C2   D2  NaN  NaN  NaN
			3  A3   B3   C3   D3  NaN  NaN  NaN
			4  A6  NaN  NaN  NaN   B6   C6   D6
			5  A7  NaN  NaN  NaN   B7   C7   D7


    .. tab-container:: r
        :title: R

        * Code:

        .. code-block:: r

			library(dplyr)

			# full join
			dplyr::full_join(left,right, by = 'A')
			left %>% full_join(right, by ='A')

        * Result:

        .. code-block:: r

			> dplyr::full_join(left,right, by = 'A')
			   A    B    C    D    F    G    H
			1 A0   B0   C0   D0   B4   C4   D4
			2 A1   B1   C1   D1   B5   C5   D5
			3 A2   B2   C2   D2 <NA> <NA> <NA>
			4 A3   B3   C3   D3 <NA> <NA> <NA>
			5 A6 <NA> <NA> <NA>   B6   C6   D6
			6 A7 <NA> <NA> <NA>   B7   C7   D7
			Warning message:
			Column `A` joining factors with different levels, coercing to character vector 
			> left %>% full_join(right, by ='A')
			   A    B    C    D    F    G    H
			1 A0   B0   C0   D0   B4   C4   D4
			2 A1   B1   C1   D1   B5   C5   D5
			3 A2   B2   C2   D2 <NA> <NA> <NA>
			4 A3   B3   C3   D3 <NA> <NA> <NA>
			5 A6 <NA> <NA> <NA>   B6   C6   D6
			6 A7 <NA> <NA> <NA>   B7   C7   D7
			Warning message:
			Column `A` joining factors with different levels, coercing to character vector 


Filtering Joins
---------------


DataFrame Operations
++++++++++++++++++++





TO DO .....