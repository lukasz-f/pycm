# -*- coding: utf-8 -*-

VERSION="0.6"

PARAMS_DESCRIPTION={"TPR":"sensitivity, recall, hit rate, or true positive rate","TNR":"specificity or true negative rate",
                   "PPV":"precision or positive predictive value","NPV":"negative predictive value",
                   "FNR":"miss rate or false negative rate","FPR":"fall-out or false positive rate",
                   "FDR":"false discovery rate","FOR":"false omission rate","ACC":"accuracy",
                   "F1":"F1 Score - harmonic mean of precision and sensitivity","MCC":"Matthews correlation coefficient",
                   "BM":"Informedness or Bookmaker Informedness","MK":"Markedness","LR+":"Positive likelihood ratio",
                   "LR-":"Negative likelihood ratio","DOR":"Diagnostic odds ratio","TP":"true positive/hit",
                    "TN":"true negative/correct rejection","FP":"false positive/Type 1 error/false alarm",
                    "FN":"false negative/miss/Type 2 error","P":"Condition positive","N":"Condition negative",
                    "TOP":"Test outcome positive","TON":"Test outcome negative","POP":"Population","PRE":"Prevalence",
                    "G":"G-measure geometric mean of precision and sensitivity","RACC":"Random Accuracy",
                    "F0.5":"F0.5 Score","F2":"F2 Score","ERR":"Error Rate"}

PARAMS_LINK={"TPR":"https://en.wikipedia.org/wiki/Sensitivity_and_specificity",
             "TNR":"https://en.wikipedia.org/wiki/Sensitivity_and_specificity",
             "PPV":"https://en.wikipedia.org/wiki/Positive_and_negative_predictive_values",
             "NPV":"https://en.wikipedia.org/wiki/Positive_and_negative_predictive_values",
             "FNR":"https://en.wikipedia.org/wiki/False_positives_and_false_negatives#False_positive_and_false_negative_rates",
             "FPR":"https://en.wikipedia.org/wiki/False_positives_and_false_negatives#False_positive_and_false_negative_rates",
             "FDR":"https://en.wikipedia.org/wiki/False_discovery_rate",
             "FOR":"http://pycm.shaghighi.ir/doc#FOR-(false-omission-rate)",
             "ACC":"https://en.wikipedia.org/wiki/Accuracy_and_precision",
             "F1":"https://en.wikipedia.org/wiki/F1_score",
             "F0.5":"https://en.wikipedia.org/wiki/F1_score",
             "F2":"https://en.wikipedia.org/wiki/F1_score",
             "MCC":"https://en.wikipedia.org/wiki/Matthews_correlation_coefficient",
             "BM":"http://www.shaghighi.ir/pycm/doc/#BM-(Informedness-or-Bookmaker-Informedness)",
             "MK":"http://www.shaghighi.ir/pycm/doc/#MK-(Markedness)",
             "LR+":"https://en.wikipedia.org/wiki/Likelihood_ratios_in_diagnostic_testing",
             "LR-":"https://en.wikipedia.org/wiki/Likelihood_ratios_in_diagnostic_testing",
             "DOR":"https://en.wikipedia.org/wiki/Diagnostic_odds_ratio",
             "TP":"https://en.wikipedia.org/wiki/Confusion_matrix",
             "TN":"https://en.wikipedia.org/wiki/Confusion_matrix",
             "FP":"https://en.wikipedia.org/wiki/Confusion_matrix",
             "FN":"https://en.wikipedia.org/wiki/Confusion_matrix",
             "P":"https://en.wikipedia.org/wiki/Confusion_matrix",
             "N":"https://en.wikipedia.org/wiki/Confusion_matrix",
             "POP":"https://en.wikipedia.org/wiki/Confusion_matrix",
             "TOP":"https://en.wikipedia.org/wiki/Confusion_matrix",
             "TON":"https://en.wikipedia.org/wiki/Confusion_matrix",
             "G":"https://en.wikipedia.org/wiki/F1_score#G-measure",
             "ERR":"http://www.shaghighi.ir/pycm/doc/#ERR(Error-rate)",
             "RACC":"http://www.shaghighi.ir/pycm/doc/#RACC(Random-accuracy)",
             "PRE":"https://en.wikipedia.org/wiki/Prevalence",
             "Overall_ACC":"http://www.shaghighi.ir/pycm/doc/#Overall_ACC",
             "Kappa":"http://www.shaghighi.ir/pycm/doc/#Kappa-(Nominal)",
             "Overall_RACC":"http://www.shaghighi.ir/pycm/doc/#Overall_RACC",
             "Strength_Of_Agreement(Landis and Koch)":"http://www.shaghighi.ir/pycm/doc/#SOA1-(Strength-of-Agreement,"
                                                      "-Landis-and-Koch-benchmark)",
             "Strength_Of_Agreement(Fleiss)":"http://www.shaghighi.ir/pycm/doc/#SOA2-(Strength-of-Agreement,"
                                             "-:-Fleiss%E2%80%99-benchmark)",
             "Strength_Of_Agreement(Altman)":"http://www.shaghighi.ir/pycm/doc/#SOA3-(Strength-of-Agreement,"
                                             "-Altman%E2%80%99s-benchmark)",
             "Strength_Of_Agreement(Cicchetti)":"",
             "TPR_Macro":"http://www.shaghighi.ir/pycm/doc/#TPR_Macro",
             "PPV_Macro":"http://www.shaghighi.ir/pycm/doc/#PPV_Macro",
             "TPR_Micro":"http://www.shaghighi.ir/pycm/doc/#TPR_Micro",
             "PPV_Micro":"http://www.shaghighi.ir/pycm/doc/#PPV_Micro",
             "Scott_PI":"http://www.shaghighi.ir/pycm/doc/#Scott's-pi-(Nominal)",
             "Gwet_AC1":"http://www.shaghighi.ir/pycm/doc/#Gwet's-AC1",
             "Bennett_S":"http://www.shaghighi.ir/pycm/doc/#Bennett-et-al.'s-S-score-(Nominal)"

             }

BENCHMARK_COLOR={"Poor":"Red","Fair":"Orange","Good":"Green","Excellent":"Green","Intermediate to Good":"Green",
                 "Substantial":"Green","Almost Perfect":"Green","Moderate":"Green","Slight":"Orange","None":"White",
                 "Very Good":"Green"}