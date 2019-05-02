df = data.frame(A = c(1, 0, NA, 3), 
                B = c(1, 0, 0, 0), 
                C = c(4, NA, 7, 8))

library(tidyr)
library(dplyr)

na2zero <- function(data){
  data %>% mutate_all(~replace(., is.na(.), 0))
}


na2mean <- function(data){
  for(i in 1:ncol(data)){
    data[is.na(data[,i]), i] <- mean(data[,i], na.rm = TRUE)
  }
  return(data)
}

na2mean(df)
