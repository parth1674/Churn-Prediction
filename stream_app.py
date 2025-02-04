import pickle
import streamlit as st
import pandas as pd
from PIL import Image



model_file = 'model_C=1.0.bin'




with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


def main():
	st.title("ChurnMaster: Navigating Customer Loyalty")
	col3,col4 = st.columns(2)
	
	image = Image.open('images/icone.png')
	image2 = Image.open('images/download.png')
	st.image(image,use_column_width=False)
	st.sidebar.header("Team Mahakal")
	add_selectbox = st.sidebar.selectbox(
	"How would you prefer to make predictions?",
	("Online", "Batch"))

	st.sidebar.image(image2)
	st.sidebar.info("Streamlit-based project for predicting customer churn. It offers both online and batch prediction modes, allowing you to get churn predictions for individual customers or from a CSV file. The application provides a convenient interface to input customer details and displays the predicted churn status and risk score.")
	

	
	with col4:
		image3= Image.open("images/download.png")


	st.subheader('Team Members:')
	col5,col6=st.columns(2)

	with col5:
		
		st.write('Shivansh Mishra')
		st.write('Saksham Shrivastava')
		st.write('Parth Verma')
	with col6:
		st.write('Srishti Alung')
		st.write('Ayushi Prajapati')
		
		
	
	col1, col2 = st.columns(2)
	
	if add_selectbox == 'Online':
		with col1:

			gender = st.selectbox('Gender:', ['male', 'female'])
			seniorcitizen= st.selectbox(' Customer is a senior citizen:', [0, 1])
			partner= st.selectbox(' Customer has a partner:', ['yes', 'no'])
			dependents = st.selectbox(' Customer has  dependents:', ['yes', 'no'])
			phoneservice = st.selectbox(' Customer has phoneservice:', ['yes', 'no'])
		
			multiplelines = st.selectbox(' Customer has multiplelines:', ['yes', 'no', 'no_phone_service'])
			internetservice= st.selectbox(' Customer has internetservice:', ['dsl', 'no', 'fiber_optic'])
		with col2:

			
			onlinesecurity= st.selectbox(' Customer has onlinesecurity:', ['yes', 'no', 'no_internet_service'])
			onlinebackup = st.selectbox(' Customer has onlinebackup:', ['yes', 'no', 'no_internet_service'])
			deviceprotection = st.selectbox(' Customer has deviceprotection:', ['yes', 'no', 'no_internet_service'])
			techsupport = st.selectbox(' Customer has techsupport:', ['yes', 'no', 'no_internet_service'])
			streamingtv = st.selectbox(' Customer has streamingtv:', ['yes', 'no', 'no_internet_service'])
			streamingmovies = st.selectbox(' Customer has streamingmovies:', ['yes', 'no', 'no_internet_service'])
			contract= st.selectbox(' Customer has a contract:', ['month-to-month', 'one_year', 'two_year'])
		paperlessbilling = st.selectbox(' Customer has a paperlessbilling:', ['yes', 'no'])
		paymentmethod= st.selectbox('Payment Option:', ['bank_transfer_(automatic)', 'credit_card_(automatic)', 'electronic_check' ,'mailed_check'])
		tenure = st.number_input('Number of months the customer has been with the current telco provider :', min_value=0, max_value=240, value=0)
		monthlycharges= st.number_input('Monthly charges :', min_value=0, max_value=240, value=0)
		totalcharges = tenure*monthlycharges
		output= ""
		output_prob = ""
		input_dict={
				"gender":gender ,
				"seniorcitizen": seniorcitizen,
				"partner": partner,
				"dependents": dependents,
				"phoneservice": phoneservice,
				"multiplelines": multiplelines,
				"internetservice": internetservice,
				"onlinesecurity": onlinesecurity,
				"onlinebackup": onlinebackup,
				"deviceprotection": deviceprotection,
				"techsupport": techsupport,
				"streamingtv": streamingtv,
				"streamingmovies": streamingmovies,
				"contract": contract,
				"paperlessbilling": paperlessbilling,
				"paymentmethod": paymentmethod,
				"tenure": tenure,
				"monthlycharges": monthlycharges,
				"totalcharges": totalcharges
			}

		if st.button("Predict"):
			X = dv.transform([input_dict])
			y_pred = model.predict_proba(X)[0, 1]
			churn = y_pred >= 0.5
			output_prob = float(y_pred)
			output = bool(churn)
		st.success('Churn: {0}, Risk Score: {1}'.format(output, output_prob))
	if add_selectbox == 'Batch':
		file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
		if file_upload is not None:
			data = pd.read_csv(file_upload)
			X = dv.transform([data])
			y_pred = model.predict_proba(X)[0, 1]
			churn = y_pred >= 0.5
			churn = bool(churn)
			st.write(churn)

if __name__ == '__main__':
	main()



	