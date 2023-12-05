# MGT4250 Fall 2023 Course Project
Author:Anthony Szydlik Email address: aszydlik@elon.edu
This repo is for the class project of MGT 4250 Fall 2023 at Elon University
[Link to Tableau Public Visualization](https://public.tableau.com/app/profile/anthony.szydlik/viz/tableaupublicfinalvisualization/Sheet1#1)
[Link to Streamlit Community Cloud](https://2ew5e3xfm3jler5xgrgcvf.streamlit.app/)
## Project Description
What variables have the greatest impact on credit scores and how do these scores affect loans? Understanding the key variables that affect credit scores is crucial for citizens, financial corporations, and lawmakers. When it comes to adult life in most nations credit scores are hugely important as they usually determine your rates and the amount of money you can be lent. Good credit can lead to better financial opportunities and lower rates, while a lower credit score can limit opportunities and increase the cost of borrowing. Anywhere from renting an apartment, to buying a car, to purchasing a house, or getting a loan credit score plays a huge role in the process of securing funds. For people within the loaning industry knowledge of key indicators for credit score is of utmost importance. The more that they know about key indicators the more they can reflect on their practices to loan the correct amount to the right people. In the credit score world variables are constantly being added and changed. As financial technologies and lending practices evolve, new variables may emerge as key indicators in determining credit score. Alternative data sources, innovations, and changes in consumer behavior can all reshape the credit scoring formulas. To stay relevant and responsive, citizens and corporations need to stay informed about the ever-changing world of credit scores and adapt their strategies accordingly. 

Works Cited:

"What's in Your Credit Score." myFICO.com, Fair Isaac Corporation (FICO), 
    https://www.myfico.com/credit-education/whats-in-your-credit-score.
    
"Credit Risk Management Solutions." Equifax, Equifax Inc., 
    https://www.equifax.com/business/credit-risk/.
    
"What is a Credit Score?" Consumer Financial Protection Bureau, 
    https://www.consumerfinance.gov/ask-cfpb/what-is-a-credit-score-en-315/.


### questions of interest
-What factors can we see to have a direct relationship to the outcome of credit score?
-How do these factors affect people and how should one act to raise credit score?
## Data Description
For this project, I decided to look at credit scores and how different variables affect the outcome. I specifically wanted to find the factors that affect these scores the most as it will potentially help other consumers and me in the future. Knowing information like this will help me be smarter about my credit score and practice habits which improve my score. To craft my conclusions, I needed consumer credit score data from some areas of the world. When searching for datasets it became quite clear that they were mostly complete but almost every dataset omitted the credit score received by individuals. To combat this, I was able to find a credit dataset that gives responses for either good, standard, or poor credit. I found this case study of credit scores at [Link to Dataset](https://statso.io/credit-score-classification-case-study/). With a response column, I will be able to use this dataset to craft visualizations and create a predictive model that I can feed variables to generate a potential response. My data has 27 different variables which correspond to the response column being either good, standard, or poor credit. The data also shows credit scores for individuals over 8 months and can show trends in credit scores related to certain behaviors. Many variables have a negligible effect on the outcome and thus columns like social security number, occupation, name, and payment behavior will be omitted. Instead, I will focus on columns where a direct relationship can be drawn like age, monthly in-hand salary, interest rate, and average outstanding debt. From these visualizations, I will be able to conclude as to which variables affect credit scores. Then I will be able to further determine what factor has the most impact on the outcome.  
## Interpreting Visualizations
![newplot (5)](https://github.com/elin202/-mgt4250test/assets/152214492/e19e1ddc-deee-43fa-bdca-bd2f94d90564)

In the first visualization, the relationship between monthly in-hand salary and credit score has been plotted in a boxplot. This shows us the upper and lower bounds of each credit score description based on the monthly in-hand salary. It also includes the median values for each response and looking at this we can see that the median changes only slightly which indicates that the data is similar. This graph allows us to see that there Is a relationship between these two variables and reflects that the more in-hand salary a person has per month the more likely they are to have a higher credit score. This allows us to conclude that the more money a person makes, the more likely they are to have good credit. Although this is only a correlation and not a direct relationship, it shows us that this variable is significant. 
![newplot (4)](https://github.com/elin202/-mgt4250test/assets/152214492/abdf7e27-18bc-4ea1-abf7-3be92c9a4c7a)

In the second visualization, the relationship between age and credit score has been plotted in a boxplot. It shows us the upper and lower bounds for age based on the response for credit score. From this graph, we can see quite definitively that higher age directly correlates to a higher credit score. This relationship makes sense as the older the target is the more likely they have a longer credit history to improve their score. We can also see that the median ages are in the middle of their respective plots meaning that ages are not skewed higher or lower. This shows us that as age increases the likelihood of better credit also increases.
![Screenshot 2023-11-27 142504](https://github.com/elin202/-mgt4250test/assets/152214492/3a3ff340-6b96-4e7a-8276-3c31750ee102)

In the third visualization the relationship between average outstanding debt and credit score is plotted in a line chart. The graph presents three different lines that represent the credit score response based on the average outstanding debt. There are clear differences between the different credit scores. A response for a good credit score can be seen to have an average debt from around $600-$800 while a standard credit score averages around $1,200-$1,500. Poor credit score can be seen to have a much higher average debt of around $2000-$2200. From this graph, we see a correlation between lower average debt and credit scores showing the variable's significance. 


## Discussion & Summary
[link to an article for discussion](https://www.experian.com/blogs/ask-experian/credit-education/score-basics/what-affects-your-credit-scores/)

This article discusses the various factors that affect credit scores and the average weights given to such factors. This will allow us to see how they affect the overall credit score and compare these results to our visualizations. While credit companies' calculations are changing every day this article along with the data will give us insight into the process of finding credit scores. The article states that as much as 35% of your credit score comes from making payments on time. Missing these payments can lower your credit score and default on debt may doom it for the foreseeable future. Another 30% can be attributed to credit amounts and how it is utilized. 15% is comprised of the length of credit history which implies that a longer history with the right behavior can raise scores. Finally, how your credit is structured or credit mix is 10% while new credit accounts for the final 10%. 

"Understanding the factors that go into credit scores can help you recognize the connections between your behaviors and your scores. While there are factors beyond your control (you can't instantly gain 10 more years of credit management experience, for instance), you can make choices today that affect your credit scores relatively quickly."

I also inquired to Chat GPT-4 about the effect of certain variables on credit scores.

Query: I want to know more about how individual factors affect credit scores. what factors are given the most weight in credit score and how should this affect consumer behavior?

Response(Chat GPT-4): 
Credit scores are calculated using a variety of factors, each with a different weight. Here are the most important ones:

Payment History (35%): This is the most significant factor. It includes the regularity of your payments, the number of late payments, and the time it took to make those late payments. To maintain a good credit score, it's crucial to make all payments on time.

Credit Utilization Ratio (30%): This is the ratio of your current total debt to your total available credit. A lower ratio is better for your credit score. It's recommended to keep your credit utilization ratio below 30%.

Length of Credit History (15%): This refers to how long you've had credit. A longer credit history generally improves your credit score. It's beneficial to keep old credit accounts open, even if you don't use them, to lengthen your credit history.

Credit Mix (10%): This refers to the types of credit you have, including credit cards, retail accounts, installment loans, mortgage loans, and finance company accounts. A mix of different types of credit can improve your score.

New Credit (10%): This refers to recently opened credit accounts. Opening too many new accounts in a short period can negatively impact your score. It's better to apply for new credit only when necessary.

In terms of consumer behavior, it's important to make payments on time, keep credit balances low, not open too many new accounts at once, and maintain a mix of different types of credit. It's also beneficial to regularly check your credit report to ensure it's accurate and to quickly address any errors.

Conclusion: 

When looking at the article and Chat GPT's response it is very evident that payments on time and credit utilization are the most important factors for credit score. sadly with our data set a payment history visualization could not be drawn. From the graph of outstanding debt versus credit score, we can see very clearly that the less outstanding debt one has the more likely they are to have good credit. This relationship is reinforced by the response and article. We can also see that length of credit history accounts for as much as 15% of credit score. This reinforces the conclusions drawn from our graph of age versus credit score which shows that the older a person is the more likely they are to have good credit. Although in-hand cash is not mentioned in these references the visualization shows that it is more likely for individuals with more cash on hand to have better credit. Overall the article and Chat GPT-4 both seem to reinforce the conclusions drawn from the visualizations and encourages me to continue with this data.




















