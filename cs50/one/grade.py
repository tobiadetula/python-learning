"""
    _summary_
    Grade comparison calculation
    
"""


score = int(input("Score: "))

# Alternate means of writing 
#if 90 <= score and score <= 100:

if score >= 90:
    print("Grade: A")
elif  score >= 80:
    print("Grade: B")
elif  score >= 70:
    print("Grade: C")
elif  score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
