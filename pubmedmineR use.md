# pubmed.mineR use

## pubmed manually search

Advanced search terms:

```
(BAP1[All Fields] AND SETD2[All Fields]) AND ("1999"[PDAT] : "2019"[PDAT])
```

Return 68 publications



## pubmed R search

use same search terms, Also return 68 publications

```
query = "BAP1 and SETD2"
date_start = 1999
date_end = 2019

library(RISmed)
library(dplyr)
library(ggplot2)
library(tidytext)
library(wordcloud)
if(!file.exists(file = file.path(results_dir,
                                 paste0('abstracts_',
                                        query,'_',as.character(date_start),'-',as.character(date_end),
                                        '.rdata')))){
  result <- EUtilsSummary(query, 
                          type = "esearch", 
                          db = "pubmed",
                          datetype = "pdat",
                          retmax = 10000,
                          mindate = date_start, 
                          maxdate = date_end)
  
  fetch <- EUtilsGet(result, type = "efetch", db = "pubmed") 
  
  abstracts <- data.frame(title = fetch@ArticleTitle,
                          abstract = fetch@AbstractText, 
                          journal = fetch@Title,
                          pmid = fetch@PMID, 
                          year = fetch@YearPubmed) 
  
  abstracts <- abstracts %>% mutate(abstract = as.character(abstract))
  save(abstracts, file = file.path(results_dir,
                                   paste0('abstracts_',
                                          query,'_',as.character(date_start),'-',as.character(date_end),
                                          '.rdata')))

  }
```

