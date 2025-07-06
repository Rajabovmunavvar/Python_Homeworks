# 1)create function to check if number is primer or not :
# if prime "true"
# if not prime "false"



def is_prime(number):
        if number < 2:
            return False
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
          if number % i == 0:
            is_prime = False
            print(False)
            break
        if is_prime:
            print(True)


is_prime(9)

# 2)

def digit_sum(k):
    lst = []
    k = str(k)
    for item in k:
       item = int(item)
       lst.append(item)
    
    return sum(lst)



print(digit_sum(3000))


#3)



def two_power_func(num):
    
  number_2 = 2
  lst = []
  cnt = 1

  while number_2 ** cnt <= num:
    result = number_2 ** cnt
    lst.append(result)
    cnt += 1
  return lst

print(two_power_func(88))
