"""
    _summary_
    Grade comparison calculation
    
"""


score = int(input("Score: "))

# Alternate means of writing 
#if 90 <= score and score <= 100:

if 90 <= score <= 100:
    print("Grade: A")
elif  80 <= score < 90:
    print("Grade: B")
elif  70 <= score < 80:
    print("Grade: C")
elif  60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
