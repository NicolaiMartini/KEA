# Lav typecasting fra floating points til integer (heltal)
# 1.1
float1=5799.7345
int1=int(float1)
print(int1)

# 1.2
float2=1111.1111
int2=int(float2)
print(int2)

# 1.3
float3=339.993
int3=int(float3)
print(int3)

# 1.4
float4=1.0
int4=int(float4)
print(int4)

# Bruteforce one
print(int(5799.7345))

# For variable in list
floats=[5799.7345,1111.1111,339.993,1.0]
for i in floats:
    print(int(i))
