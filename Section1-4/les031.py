#Using a Step in a Slice
strS = "1,234,567,890,123"

print(strS[1:10:4])
# 1 start index
# 10 end index
# 4 step
# output: ,, => "1[, (start)]234[, (step 4)]567[, (step 4 end)]890,123"

print(strS[1::4])# output: ,,,, 

