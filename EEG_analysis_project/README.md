## Unbossed Spectral Analysis 
### Project to use EEG frequency data on a machine learning model to bring out the best frequencies that would explain the state of the brain 

### Author -Valisha Shah 

### Workflow
1. This python script reads in the matlab data which has values of EEG for each frequency at different timepoints after the drug was administered to a Wild Type or Mutant mouse.
2. After the data is in python readable format, the model is trained on the data with WT or Mutant as the Target variable
3. The data predicted data is then cross validated with accuracy, F1 score and stability score (over 1000 iterations)
4. Finally, the frequencies that could predict with WT vs Mutant with maximum metrics are chosen.
