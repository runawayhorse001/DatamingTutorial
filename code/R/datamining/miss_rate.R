# create DataFrame
x = data.frame(A = c(1, 2, NA, 3), B = c(NA, NA, 4, 5), C = c(NA, 'b', 'c', 'd'))

# loding library
library('dplyr')
#library('tidyverse')

# define the missing rate function
missing_rate <- function(df){
  # calculate missing rate and transpose the DataFrame
  rate <-t( df %>% summarize_all(funs(sum(is.na(.)) / length(.))))
  # rename the column
  colnames(rate)[1] <- "missing_rate"
  print(rate)
}

x
missing_rate(x)


df = data.frame(A = c(1, 2, 3, 3), B = c(1, 1, 1, 1), C = c('a', 'b', 'c', 'd'))

zero_variance <- function(df){
  compData <- data.frame(feature= c(NA), count= c(NA))
  for(i in 1:ncol(df))
  {
    compData[i, ] <- c(colnames(df)[i],length(unique(df[,i])))
  }
  return(compData[compData$count==1,]$feature)
}

zero_variance(df)



