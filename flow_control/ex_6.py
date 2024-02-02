def caps_long(str):    
    return str.upper() if len(str) > 10 else str

# if len(str) > 10:
#         return str.upper()
#     else:
#         return str

print(caps_long("Sue Smith"))     # Sue Smith
print(caps_long("Sue Roberts"))   # SUE ROBERTS
print(caps_long("Joe Shea"))      # Joe Shea
print(caps_long("Joe Stevens"))   # JOE STEVENS