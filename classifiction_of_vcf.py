#!/usr/bin/env python3

"""Scripting for importing PCA results from the variant call file and defining a workflow for analysis and classification based on the ancestry of each call set"""

def import_libraries():
    """
    Functions to import libraries 
    """
    import pandas as pd
    import argparse
    import numpy as np
    from sklearn.model_selection import train_test_split
    from collections import Counter
    from imblearn.over_sampling import SMOTE
    from imblearn.under_sampling import RandomUnderSampler
    from imblearn.pipeline import Pipeline
    from sklearn.preprocessing import LabelEncoder
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score, classification_report
    from sklearn.model_selection import RandomizedSearchCV
    import matplotlib.pyplot as plt
    import seaborn as sns
    print("Loaded required libraries")


def reading_pca_results(pca_table, labels):
    acs_mini_pca = pd.read_csv(pca_table, sep = " ", header=None)
    acs_mini_pca.drop([0,1], inplace=True, axis=1)
    ## defining cols
    cols = []
    for i in acs_mini_pca.columns:
        cols.append(str('PC{}'.format(i-1)))
        acs_mini_pca.columns = cols
    v1 = pd.read_csv(labels, sep="\t")
    frames = [v1, acs_mini_pca]
    acs_mini_pca_table = pd.concat(frames, axis = 1)
    return acs_mini_pca_table


def plot_PC_values(eigenvalue_file):
    """
    Function forp plotting the PC values with variance explained
    """
    eigenval = pd.read_csv("eigenvalue_file", header=None)
    e = list(eigenval.iloc[:,0])
    pve = {}
    for i in range(0, 20):
        pve.update({('PC{}'.format(i)):e[i]/sum(e)*100})
    pve = pd.DataFrame.from_dict(pve, orient='index')
    h = list(pve.iloc[:, 0])
    bars = list(pve.index)
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, h)
    plt.xticks(y_pos, bars)
    plt.ylabel('Explained Variance')
    plt.xlabel('Principal Components')
    plt.savefig('PC_explained_variance.jgp')
    plt.show()

def remove_NA_values(acs_mini_pca_table):
    """
    Function to remove the NA values to make the training dataset
    """
    acs_mini_ancestry = acs_mini_pca_table[~(pd.isna(acs_mini_pca_table['ancestry']))]
    acs_mini_ancestry['ancestry'].value_counts()
    acs_mini_ancestry_na = pd.DataFrame(acs_mini_pca_table[(pd.isna(acs_mini_pca_table['ancestry']))])
    acs_mini_ancestry_na.drop('ancestry', inplace=True, axis=1)
    return acs_mini_ancestry, acs_mini_ancestry_na


def balance_dataset_SMOTE(acs_mini_ancestry):
    """
    Removing the imbalance in the dataset using SMOTE on the whole dataset and then splitting in training and testing making sure there is an equal split in training and testing
    """
    acs = acs_mini_ancestry.drop(['ancestry', 'sample_id'], inplace=False, axis=1)
    target, ancestry = pd.factorize(acs_mini_ancestry['ancestry'])
    acs_mini_train = acs.reset_index(drop=True)
    training_sampleids = list(acs_mini_ancestry['sample_id'])
    y = LabelEncoder().fit_transform(y)
    oversample = SMOTE()
    X, y = oversample.fit(acs_mini_ancestry, target)
    adict = {}
    for i, _ in enumerate(ancestry):
        adict.update({i:ancestry[i]}) 
    return X, y, adict


def svm_training(X, y, adict, acs_mini_ancestry_na):
    """
    Running SVM model with poly kernel on the first 10 Prinicipal Components.
    As proven in the python notebook
    Returns a final dataframe with the predicted variables 
    """
    X = X.iloc[:, 0:10]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.85, random_state=0)
    poly = svm.SVC(kernel='poly', degree=3, C=1, decision_function_shape='ovo').fit(X_train, y_train)
    poly_pred = poly.predict(X_test)
    accuracy_poly = poly.score(X_test, y_test)
    print('Accuracy Polynomial Kernel: ', accuracy_poly)
    report_poly = classification_report(y_test, poly_pred)
    print('Classification report: ', report_poly)
    na_sampleids = acs_mini_ancestry_na['sample_id']
    acs_na = acs_mini_ancestry_na.drop('sample_id', inplace=False, axis=1)
    pred_na_poly = poly.predict(acs_na)
    pred_na_poly = pd.DataFrame(pred_na_poly)
    pp = []
    for i in pred_na_poly[0]:
        pp.append(adict[i])
    final_df_na = acs_mini_ancestry_na.reset_index(drop=True)
    final_df_na['ancestry'] = pp 
    return final_df_na, na_sampleids


def creating_the_final_df(final_df_na, acs_mini_pca_table):
    acs_mini_pca_table_pc = acs_mini_pca_table.iloc[:, 0:12]
    na_sampleids = acs_mini_ancestry_na['sample_id']
    for i in na_sampleids:
        s = (final_df_na_pc.loc[final_df_na_pc['sample_id']==i, 'ancestry'].values)
        acs_mini_pca_table_pc.loc[acs_mini_pca_table_pc['sample_id']==i, 'ancestry'] = s[0]
    acs_mini_pca_table_pc = pd.DataFrame(acs_mini_pca_table_pc)
    return acs_mini_pca_table_pc


def plot_PCA_distribution(acs_mini_pca_table_pc):
    """
    Plot PCA distribution after predicting the NA values
    """
    acs_mini_sns = pd.melt(acs_mini_pca_table_pc.iloc[:, 1:], id_vars="ancestry")
    sns.set(rc={'figure.figsize':(30,20)})
    sns.set_style("darkgrid")
    ax = sns.factorplot(x = "variable", y = "value", hue = "ancestry", data = acs_mini_sns)
    plt.show()
    sns.set(rc={'figure.figsize':(30,20)})
    acs_mini_sns_wo_outliers = acs_mini_sns.loc[acs_mini_sns['value'].between(acs_mini_sns['value'].quantile(.15), acs_mini_sns['value'].quantile(.85))]
    sns.set_style("darkgrid")
    ax = sns.boxplot(x = "variable", y = "value", hue = "ancestry", data = acs_mini_sns_wo_outliers)
    ax.tick_params(axis='both', which='major', labelsize=35)
    ax.tick_params(axis='both', which='minor', labelsize=35)
    ax.set_xlabel("Prinicipal Components", fontsize=50)
    ax.set_ylabel("PC values", fontsize=50)
    ax.set_title("Boxplot for Prinicipal Component distribution for all the ancestry labels", fontsize=50)
    ax.legend(loc="upper right", fontsize=40)
    plt.show()
    sns.set()
    sns.set_style("darkgrid")
    ax = sns.barplot(x = "variable", y = "value", hue = "ancestry", data = acs_mini_sns_wo_outliers)
    ax.tick_params(axis='both', which='major', labelsize=35)
    ax.tick_params(axis='both', which='minor', labelsize=35)
    ax.set_xlabel("Prinicipal Components", fontsize=50)
    ax.set_ylabel("PC values", fontsize=50)
    ax.set_title("Barplot for Prinicipal Component distribution for all the ancestry labels", fontsize=50)
    ax.legend(loc="upper right", fontsize=40)
    plt.show()
    sns.set()
    sns.set_style("darkgrid")
    ax = sns.pointplot(x = "variable", y = "value", hue = "ancestry", data = acs_mini_sns_wo_outliers, jitter=True, palette="Set2", split=True)
    ax = sns.lineplot(x = "variable", y = "value", hue = "ancestry", data = acs_mini_sns_wo_outliers)
    ax.tick_params(axis='both', which='major', labelsize=35)
    ax.tick_params(axis='both', which='minor', labelsize=35)
    ax.set_xlabel("Prinicipal Components", fontsize=50)
    ax.set_ylabel("PC values", fontsize=50)
    ax.set_title("Lineplot for Prinicipal Component distribution for all the ancestry labels", fontsize=50)
    ax.legend(loc="upper right", fontsize=40)
    plt.show()


if __name__ == "__main__":
    import_libraries()
    PARSER = argparse.ArgumentParser(description="files to be inputted PCA and labels")
    PARSER.add_argument('--pca_file', '-i1', dest='pca_table', type=str, help='Enter the filename with the PCA values', required=True)
    PARSER.add_argument('--ancestry_labels', '-i2', dest='labels', type=str, help='Enter the filename with the ancestry labels', required=True)
    PARSER.add_argument('--eigenvalues', '-i3', dest='eigenvalues', type=str, help='Enter the filename with the eigenvalues', required=True)
    ARGS = PARSER.parse_args()
    pca_table = ARGS.pca_table
    labels = ARGS.labels
    eigenvalues = ARGS.eigenvalues
    acs_mini_pca_table = reading_pca_results(pca_table, labels)
    plot_PC_values(eigenvalues)
    acs_mini_ancestry, acs_mini_ancestry_na = remove_NA_values(acs_mini_pca_table)
    X, y, adict = balance_dataset_SMOTE(acs_mini_ancestry)
    final_df_na, _ = svm_training(X, y, adict, acs_mini_ancestry_na)
    acs_mini_pca_table_pc = creating_the_final_df(final_df_na, acs_mini_pca_table)
    plot_PCA_distribution(acs_mini_pca_table_pc)
