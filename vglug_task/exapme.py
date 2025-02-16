# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]

nums = [0,1,2,4,5,7]

output = []
chacking = 0
for i in nums:
    if chacking == i:
        output.append(i)
        chacking +=1
    else:
        output.append(i)
        chacking = i
        chacking+=1


print(output)
frist_num = output[0]
last_num = output[-1]

print(f"{frist_num}->{last_num}")