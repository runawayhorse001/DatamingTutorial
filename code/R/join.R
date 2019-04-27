left = data.frame(A = c('A0', 'A1', 'A2', 'A3'), 
                  B = c('B0', 'B1', 'B2', 'B3'), 
                  C = c('C0', 'C1', 'C2', 'C3'),
                  D = c('D0', 'D1', 'D2', 'D3'))
left

right = data.frame(A = c('A0', 'A1', 'A6', 'A7'), 
                   F = c('B4', 'B5', 'B6', 'B7'), 
                   G = c('C4', 'C5', 'C6', 'C7'),
                   H = c('D4', 'D5', 'D6', 'D7'))

library(dplyr)

# left join
dplyr::left_join(left,right, by = 'A')
left %>% left_join(right, by ='A')
# right join
dplyr::right_join(left,right, by = 'A')
left %>% right_join(right, by ='A')
# inner join
dplyr::inner_join(left,right, by = 'A')
left %>% inner_join(right, by ='A')
# full join
dplyr::full_join(left,right, by = 'A')
left %>% full_join(right, by ='A')
