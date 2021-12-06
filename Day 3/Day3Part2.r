library(readr)

getVals <- function(){
    df1 = read_table("output.txt", col_names = FALSE)
    df1[] <- lapply(df1, as.numeric)
    print(df1)

    otwo <- df1
    cotwo <- df1

    # Get o2
   for (i in 1:ncol(otwo)) {       # for-loop over columns
   if (nrow(cotwo) > 1){
        m <- (table(otwo[ , i])[1] <= table(otwo[ , i])[2])    
        if (m == TRUE){
            otwo <- subset(otwo, otwo[, i] == 1)
        }
        else if (m == FALSE){
            otwo <- subset(otwo, otwo[, i] == 0)
        }
   }
    }
    # print o2
    print(otwo)

    for (i in 1:ncol(cotwo)) {       # for-loop over columns
        if (nrow(cotwo) > 1){
            n <- (table(cotwo[ , i])[1] <= table(cotwo[ , i])[2])    
            if (n == TRUE){
                cotwo <- subset(cotwo, cotwo[, i] == 0)
            }
            else if (n == FALSE){
                cotwo <- subset(cotwo, cotwo[, i] == 1)
            }
        }
    }

    print(cotwo)
}

getVals()
print(strtoi("10111"))