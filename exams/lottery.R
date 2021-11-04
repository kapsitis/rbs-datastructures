probs <- c("1A", "1B", "1C", "1D",
           "2A", "2B", "2C", "2D",
           "3A", "3B", "3C", "3D",
           "4A", "4B", "4C", "4D", 
           "5A", "5B", "5C", "5D",
           "6A", "6B", "6C", "6D", "6E")

OneTasks <- c("1A", "1B", "1C", "1D")
TwoTasks <- c("2A", "2B", "2C", "2D")
ThreeTasks <- c("3A", "3B", "3C", "3D")
FourTasks <- c("4A", "4B", "4C", "4D")
FiveTasks <- c("5A", "5B", "5C", "5D")

cppTasks <- c("6A", "6B", "6C", "6D", "6E")

oldTasks <- c("1A", "2A", "3A", "4D", "5A", "6C")


found <- FALSE
while (isFALSE(found)) {
  xx <- sample(probs, size=5)
  found <- length(intersect(xx,cppTasks)) == 1
  
  found <- found && (length(unique(c(substr(xx,1,1)))) == 5)
  
  found <- found && (length(intersect(xx,oldTasks)) == 0)
}

print(paste0(xx))


