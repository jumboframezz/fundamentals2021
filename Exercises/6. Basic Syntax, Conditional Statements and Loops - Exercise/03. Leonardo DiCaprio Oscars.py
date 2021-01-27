# 3.	Leonardo DiCaprio Oscars
# Write a program that receives a single integer number and prints different messages depending on the number:
# -	If Oscar is 88 - "Leo finally won the Oscar! Leo is happy".
# -	If Oscar is 86 - "Not even for Wolf of Wall Street?!"
# -	If Oscar is not 88 nor 86 (and below 88) - "When will you give Leo an Oscar?"
# -	If Oscar is over 88 - "Leo got one already!"
#
# Examples
# Input	Output
# 88	Leo finally won the Oscar! Leo is happy
# 86	Not even for Wolf of Wall Street?!
# 81	When will you give Leo an Oscar?
# 89	Leo got one already!
#

year = int(input())
if year == 88:
    print("Leo finally won the Oscar! Leo is happy")
elif year == 86:
    print("Not even for Wolf of Wall Street?!")
elif year < 88:
    print("When will you give Leo an Oscar?")
elif year > 88:
    print("Leo got one already!")
