# Title     : Mtethods
# Objective : Create methods in R
# Created by: mendesbarreto
# Created on: 2019-04-07


#install.packages("lmtest", repos = "http://cran.us.r-project.org")
#install.packages("tidyr", repos = "http://cran.us.r-project.org")
#install.packages("GetoptLong", repos = "http://cran.us.r-project.org")

# Exe 1 and 2

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


# Exe 3

mutiply <- function(value_left, value_right) {
  value_left_number <- as.numeric(value_right)
  value_right_number <- as.numeric(value_left)
  
  return(value_left_number * value_right_number)
}

mutiply(2,3)


# Exec 4

contains <- function(integer_number, vector) {
  for(item in vector) {
    if(item == integer_number){
      return(TRUE)
    }
  }
  return(FALSE)
}

print(contains(10, c(1,2,4,5)))
print(contains(2, c(1,2,4,5)))

# Exec 5

ocurrencies_count <- function(interger_number, vector) {
  ocurrence_count <- 0
  
  for(value in vector) {
    if(interger_number == value) {
      ocurrence_count <- ocurrence_count + 1 
    }
  }
  
  return(ocurrence_count)
}

print(ocurrencies_count(2, c(1,2,3,4,2,2,2,2)))

# Exec 6

bar_need_to_export <- function(kilograms) {
  amout_of_one_bar <- kilograms %% 5
  amout_of_five_bar <- (kilograms - amout_of_one_bar) / 5
  return(amout_of_one_bar + amout_of_five_bar)
}

print(bar_need_to_export(kilograms = 11))


# Exec 7

is_mutiple_of_three <- function(x) {
  if((x %% 3) == 0)
    return(TRUE)
  return(FALSE)
}

sum_numbers_mutiples_of_three <- function(x,y,z) {
  numbers <- c(0)
  
  if(!is_mutiple_of_three(x)) numbers <- append(x, numbers)
  if(!is_mutiple_of_three(y)) numbers <- append(y, numbers)
  if(!is_mutiple_of_three(z)) numbers <- append(z, numbers)
  
  return(sum(numbers))
}

print(is_mutiple_of_three(3))

print(sum_numbers_mutiples_of_three(1,3,4))
print(sum_numbers_mutiples_of_three(3,3,4))
print(sum_numbers_mutiples_of_three(4,3,4))

# Exec 8

is_prime_number <- function(number) {
  if(number == 2) return(TRUE)
  if(any(number %% 2:(number-1) == 0 )) return(FALSE)
  else return(TRUE)
}

print(is_prime_number(5))


