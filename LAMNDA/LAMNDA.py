add_ten=lambda X:X+10
print(add_ten(5))

add_power=lambda x,y,z:x*y*z
print(add_power(5,3,2))

vote_eligible=lambda h:h>18
print(vote_eligible(19))

vote_eligible=lambda  h:"yes" if h>18   else "no"
print(vote_eligible(15))