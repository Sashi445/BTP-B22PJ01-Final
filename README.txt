STEPS TO RUN THE APPLICATION:
--------------------------------------------------------------------------------

You can test the model by training with dataset or simply use the .off files we provided in "test_set"

To train the project you need the dataset, go ahead and download the dataset
from kaggle using the following link.

https://www.kaggle.com/datasets/balraj98/modelnet10-princeton-3d-object-dataset

Make sure the dataset and it's contents lie in a directory named "dataset"

NOTE: Training the model with dataset is not MANDATORY since the application already has a PRE-TRAINED MODEL.

Now after downloading the dataset it's time for the project setup. 

The project setup is simple and straight forward

First Create directories for uploads and outputs by typing commands

> mkdir uploads
> mkdir out

This creates folders for uploads and outputs.

Now install the required dependencies by typing out command 

> pip install -r requirements.txt

Now that all required dependencies are installed 

you can run the application by typing command

> flask run

Now the web application is up and running on localhost:5000

NOTE: The application takes input as .off file format only. 



