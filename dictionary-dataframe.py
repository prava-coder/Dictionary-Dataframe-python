#importing pandas library
import pandas as pd
#creating a dictionary
student_info={
    "names":["pravalli","uday","raji","srivani","manju","sravani"],
    "subject":["biology","science","maths","english","mathematics","telugu"],
    "age":[20,25,23,21,22,26],
    "percentile":[70.2,85.3,88.0,65.2,76,86]
}
#creating a data frame by using dictionary
df=pd.DataFrame(student_info)
print(df)