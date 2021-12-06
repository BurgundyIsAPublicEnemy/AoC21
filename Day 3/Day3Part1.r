library(readr)

getVals <- function(){
    df1 = read_table("output.txt", col_names = FALSE)
    df1[] <- lapply(df1, as.numeric)
    print(df1)

    # Get Binary
    print(table(df1[1])[1] < table(df1[1])[2])
    print(table(df1[2])[1] < table(df1[2])[2])
    print(table(df1[3])[1] < table(df1[3])[2])
    print(table(df1[4])[1] < table(df1[4])[2])
    print(table(df1[5])[1] < table(df1[5])[2])
    print(table(df1[6])[1] < table(df1[6])[2])
    print(table(df1[7])[1] < table(df1[7])[2])
    print(table(df1[8])[1] < table(df1[8])[2])
    print(table(df1[9])[1] < table(df1[9])[2])
    print(table(df1[10])[1] < table(df1[10])[2])
    print(table(df1[11])[1] < table(df1[11])[2])
    print(table(df1[12])[1] < table(df1[12])[2])

}

getVals()
print(strtoi("100110110100", base = 2) * strtoi("011001001011", base = 2))