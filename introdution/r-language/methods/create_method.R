# Title     : Mtethods
# Objective : Create methods in R
# Created by: mendesbarreto
# Created on: 2019-04-07


#install.packages("lmtest", repos = "http://cran.us.r-project.org")
#install.packages("tidyr", repos = "http://cran.us.r-project.org")
#install.packages("ggplot2", repos = "http://cran.us.r-project.org")

library(ggplot2)


print_hello_user <- function(name) {
  print(paste("Hello", sep = " ", name))
}

print_hello_user("Douglas")
