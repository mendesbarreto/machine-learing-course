# Title     : Mtethods
# Objective : Create methods in R
# Created by: mendesbarreto
# Created on: 2019-04-07


#install.packages("lmtest", repos = "http://cran.us.r-project.org")
#install.packages("tidyr", repos = "http://cran.us.r-project.org")
#install.packages("GetoptLong", repos = "http://cran.us.r-project.org")

say_hello_user <- function(name) {
  return(paste("Hello", sep = " ", name)) 
}

say_hello_user_interpolation <- function(name) {
  return(stringr::str_interp("Hello ${name}"))
}

print_hello_user <- function(name) {
  print(say_hello_user(name))
}

print_hello_user_string_interpolation <- function(name) {
  print(say_hello_user_interpolation(name = name))
}

print_hello_user("Douglas")
print_hello_user_string_interpolation("Douglas Mendes Interpolation")

