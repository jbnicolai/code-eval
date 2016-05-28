#!/usr/bin/env Rscript
# Sample code to read test cases
#
args <- commandArgs(trailingOnly=TRUE)
test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
for (test in test.cases) {
    if (length(test) > 0) {
      words = unlist(strsplit(test, ' '))
      word_lengths = unlist(lapply(words, nchar))
      cat(words[which(word_lengths == max(word_lengths))][[1]])
      cat('\n')
    }
}
