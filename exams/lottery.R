probs <- c("1A", "1B", "1C", "1D", "1E", "1F", "1G","1H", 
           "2A", "2B", "2C", "2D",
           "3A", "3B", "3C", "3D", "3E", "3F",
           "4A", "4B")

cppTasks <- c("1F", "1G", "1H", "2C", "2D", "4B")


found <- FALSE
while (isFALSE(found)) {
  xx <- sample(probs, size=5)
  found <- length(intersect(xx,cppTasks)) == 1
  
  found <- found && (length(unique(c(substr(xx,1,1)))) == 4)
}

print(paste0(xx))

