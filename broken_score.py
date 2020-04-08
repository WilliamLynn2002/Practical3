"""
Github link : https://github.com/WilliamLynn2002/practical/blob/master/broken_score.py
"""


def main():

    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Fail")

main()
