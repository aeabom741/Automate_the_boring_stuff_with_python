def spam(divideby):
    try:
        return 42 / divideby
    except:
        print("Error:Invalid arguement")

print(spam(2))
print(spam(12))
print(spam(4))
spam(0)