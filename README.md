# ML-Classification
Classification of Request Descriptions 
In this task, features are the words (Keywords) in the description of the request raised by the user. For this, we have used Bag of Words Model (NLP) to find the frequency of the words in a description /Document and make them to classify either as a software or hardware.
Steps to follow:
1.	Preprocess the given dataset 
    a.	Label the set of examples manually 
2.	Create Feature Extractor 
3.	Build the classifier 
4.	Train the Classifier with Manually labelled Dataset
5.	Test the classifier with Test Data(New description)
6.	Evaluate the performance of the classifier 

<b>Open Source Libraries used:</b> Sklearn with NLTK Features <br>
<b>Languages used:</b> Python 2.7 <br>
<b>IDE used:</b> Spyder3 <br>
<b>Algorithms used:</b> Bernoulli NavieBayes <br>

To classifiy the given description entered by the user will be calssiferd into SOFTWARE or HADRWARE(Using Bernoulli NavieBayes)
Results Will be followed as follows:

<h1>Sample Output:</h1><br>
               1.Enter your Description to Classify <br>
               2.Display confusion Matrix(Classifier) <br>
               3.Exit/Quit <br>
               
What would you like to do? 1 <br>
<b>Enter the Request Description to classify: monitor issue<b>
*********************************
'monitor issue' => ['hardware']
*********************************

               1.Enter your Description to Classify
               2.Display confusion Matrix(Classifier)
               3.Exit/Quit
               
What would you like to do? 2 <br>
Classification of Request description(Using Bernoulli NaievBayes Algo)<br>
             	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;precision&nbsp;&nbsp;&nbsp;&nbsp;recall&nbsp;&nbsp;&nbsp;&nbsp;f1-score   support<br>

   hardware       1.00      0.88      0.93         8 <br>
   software       0.83      1.00      0.91         5 <br>

avg / total       0.94      0.92      0.92        13 <br>

The accuracy score is 92.31%

               1.Enter your Description to Classify
               2.Display confusion Matrix(Classifier)
               3.Exit/Quit
               
What would you like to do? 3

Exit >>>


