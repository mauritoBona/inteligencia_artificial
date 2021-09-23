import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   #Data visualisation libraries 
import seaborn as sns
#import scipy as sc
#from sklearn.linear_model import LinearRegression
#from sklearn.model_selection import train_test_split

#"ts","device","co","humidity","light","lpg","motion","smoke","temp"
def obtenerMediaYDesvioStandar(telemetryDf):
	mean_co_df = telemetryDf['co'].mean()
	std_co_df = telemetryDf['co'].std()
	print('Media del Monóxido de Carbono {:.12f}'.format(mean_co_df))
	print('Desvio Standar del Monóxido de Carbono {:.12f}'.format(std_co_df))
	
	mean_temp_df = telemetryDf['temp'].mean()
	std_temp_df = telemetryDf['temp'].std()
	print('Media de la Temperatura {:.12f}'.format(mean_temp_df))
	print('Desvio Standar de la Temperatura {:.12f}'.format(std_temp_df))

def coeficienteCorrelacion(telemetryDf):
	pearson_corr = telemetryDf.corr(method='pearson')
	print(pearson_corr)

def graficarDeAPares(telemetryDf):
	sns.pairplot(telemetryDf)
	plt.show()

def main():
	telemetryDf = pd.read_csv("iot_telemetry_data.csv")
	#obtenerMediaYDesvioStandar(telemetryDf)
	#graficarDeAPares(telemetryDf)
	coeficienteCorrelacion(telemetryDf)

main()