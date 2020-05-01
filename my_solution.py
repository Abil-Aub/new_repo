import sys

# dig_str = sys.argv[1]
#
# s = 0
# for k in dig_str:
#     s += int(k)
#
# print(str(s), end="")

who = "world" if len(sys.argv)<2 else sys.argv[1]
print("hello,  %s" % who)