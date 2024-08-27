# app file

import cal



print("if you want to use calculator then press 1 otherwise press 0 to exit")

input_keyword = int(input("enter the keyword: "))

if input_keyword == 1:
	output = cal()

else:
	print("exit")


print("This was a cal project")