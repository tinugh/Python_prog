SUPERVISED MACHINE LEARNING

1) classification:
a)KNN:(K Nearest Neighbours)
#supervised machine learning algorithm:used for both classification and regression but majority used for classification

#in KNN,'K' always will be any odd number
#if KNN is 5; then surrounding 5 objcts willbe selected and the majority willbe the selected one

# to find distance:
#sq root of [(x2-x1)^2]+[(y2-y1)^2]=>EUCLIDEAN formula

PNTS X1 X2 TARGET
#p1   7   7  bad
#p2   7   4  bad
#p3   3   4  good
#p4   1   4  good

#p5  3  7  ?>>>>> find good or bad:
p1>>>>p5 distance
(3-7)^2+(7-7)^2=16+0=16==root(16)==4
similarly p2>>>>>>>p5==5
          p3>>>>>>P5==3
          p4>>>>>p5==3.6
#p5==good ;becoz nearest neighbours has 2 good and 1 bad by taking nearest 3

b)Naive Bayes Algorithm:
#based on probability(chances of occurance)
#this  algorithm  is  based on Bayes theorem>>> based on conditional probability
#condition probablity:posibility of event, based on the probability occured earlier

probability:
P(A/B)= P(A INTERSECTN B)/P(B)

Bayes theorem:
P(A/B)=P(B/A)P(A)/P(B)
P(A/B):posterior probability
P(B/A):likelihood probability
P(A): prior probability
P(B): marginal probability











