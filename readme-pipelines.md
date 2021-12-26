                                    Versao 3- Pipelines

Introducao ao machine learning- em problemas de classificacao
Resumo:
    Pretende-se demonstrar uma progração em python recorrendo à utilizacao de algoritmos de machine learning

Palavras Chave:
train_test_split, DecisionTreeClassifier, accuracy_score,classification_report, confusion_matrix, LogisticRegression, cross_validate

Passos:
1- Primeiro ensaio de Machine Learning
    1.1-    Ler Base de dados
    1.2-    Separar base de dados em treino e teste
    1.2.1-  DecisionTreeClassifier
    1.2.2-  Logistic Regression
    1.3-    Cross Validate:  Separa os dados em blocos de acordo com o cv escolhido
            Treina o algoritmo o numero de cv definido, ex: cv=7 -> 7 block -> 7 Round
            _________________________________________________________________
            |____________________________X,y________________________| Round |
            |block1 |block2 |block3 |block4 |block5 |block6 |block7 | (cv)  |
            |  Test | Train | Train | Train | Train | Train | Train |   1   |
            | Train |  Test | Train | Train | Train | Train | Train |   2   |
            | Train | Train |  Test | Train | Train | Train | Train |   3   |
            | Train | Train | Train |  Test | Train | Train | Train |   4   |
            | Train | Train | Train | Train |  Test | Train | Train |   5   |
            | Train | Train | Train | Train | Train |  Test | Train |   6   |
            | Train | Train | Train | Train | Train | Train |  Test |   7   |
            -----------------------------------------------------------------
            default: cv=5
    1.4-    Pipeline Sequência de processos
            Comparacao grafica com metodos em separado: LR-CV
                                                        SS-Lr-CV
                                                        pipe(SS-Lr)-CV