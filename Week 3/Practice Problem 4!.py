marks = float(input("Enter the number of marks."))
match marks:
    case marks if marks >= 0 and marks <= 50:
        print("Grade = F")
    case marks if marks >= 0 and marks<=60:
        print("Grade = D")
    case marks if marks >= 0 and marks<=70:
        print("Grade = C")
    case marks if marks >= 0 and marks <= 80:
        print("Grade = B")
    case marks if marks >= 0 and marks <=100:
        print("Grade = A")
    case _:
        print("Mark is not valid")