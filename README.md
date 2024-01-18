**M.E.K.E README FILE**

M.e.k.e software projectfor the Lab of Software porject development exam.

**Group Composition**

-Akenten Princess Emmanuela Adomah 891924 

-Favero Elisa 890183 

-Gatto Marco 891185

-Ylli Klementina 888981


**What does our software consist of?**

We used the CSV file provided to develop software that assists students in finding the school best suited to their specific needs. This tool analyzes data relating to schools in the Veneto region, allowing students to select an institution based on personalized criteria, such as school type, geographical location, and other relevant characteristics.

We used the details regarding the province, the number of services offered by each school and the city, contained in the CSV file

From the main interface of our software, users can access a variety of services. Among these, there is the functionality that allows you to find the best school in a specific city, based on criteria such as the services offered. Additionally, you can search by filtering by the grade level of a school within a given province, making it easier to select primary, secondary or other level institutions in specific geographic areas.
Another important feature of the software is the ability to generate a list of schools based on the type of managing entity: public, private or religious. 

**Dataset**
We got our dataset for the Euroupean official website, here is the link:

https://data.europa.eu/data/datasets/elenco-degli-edifici-scolastici-della-regione-del-veneto-scuole-pubbliche?locale=en

The data is about schools, of every grade, in the Veneto region.


**Development of the application**

***Feature 1***

The function elenco_scuole_con_infrastrutture is designed to identify schools within a specified Italian province that have certain infrastructural facilities. This tool is particularly useful for educational administrators, policy makers, or researchers interested in analyzing the distribution and availability of school facilities such as sports facilities across different regions.

The function accepts three parameters:

data: A DataFrame representing the dataset of school information.
nome_provincia: A string representing the name of the province to be analyzed.
infrastrutture: A list of infrastructure facilities to look for in schools (e.g., 'Mensa' for cafeteria, 'Palestra Piscina' for gym and pool).

It filters the provided dataset to focus only on the schools located in the specified province.
The function then identifies schools that possess all of the listed infrastructural facilities.
If a non-existent province is entered, the function returns an error message indicating that the province does not exist in the dataset.


***Feature 2***

The function best_school_in_town is meticulously crafted to assist students and parents in identifying the most service-rich school in a specific city and school level. This feature is incredibly valuable for those seeking a comprehensive educational environment that offers a wide array of services. It is particularly useful for making informed decisions regarding school selection based on available facilities and services.

***Function Parameters:***
data: A Pandas DataFrame that encapsulates the dataset containing detailed information about various schools.
city: A string parameter representing the city where the search for the best school is to be conducted.
school_level: A string that specifies the educational level of the school, such as 'primary', 'middle', or 'high school'.

***Functionality:***
Data Filtering: The function initially filters the dataset to include only those schools that are located in the specified city and match the given school level.

Service Evaluation: It then evaluates the schools based on the number of services they offer. This includes a comprehensive check of facilities like auditoriums, cafeterias, and sports complexes.

Result Presentation: The output is a dictionary containing key information about the best school, such as the school's name, the services it offers, and the total count of these services.


***Feature 3***

The function school_by_province, allows you to view the list of schools in a specific province, by simply typing your province of interest.
This function can be useful for many targets, from educators, governement services, to indivudual or families relocating, in their planning, research or relocation process.

***Functionality:***

The function goes through the dataset, and takes into accout only the schools located in the the province required.

> [!TIP]
>**How to use and start the M.E.K.E Software**

***Preparation***
Ensure that the necessary dataset ('name_of_your_file.csv') is present in the backend part. It is essential for the software's operation.

In order to start the software you need to follow the following steps:

1. Open the folder of the repository on Visual Studio code.
1. From the terminal on your PC run the command 'docker compose build'.This command will install the necessary Docker images for the software.
1. Open the docker icon on VS code and run the containers.
1. Right-click on a container and select "Attach VSCode". Open the /app folder inside the container.
1. Make sure that you have alraedy installed the necessary estension, go to the debug section and press start.
1. After starting the debugger you should have access to the adress localhost:8080.


> [!WARNING]
>***Troubleshooting***
If you encounter issues in launching the application (for example, CSV file formatting errors), check the backend's status and, if necessary, reload the CSV file.

***Navigating the Interface***

The various features developed are available in the top bar of the user interface. For example, the functionality to find the best school in a specific city, based on criteria such as the services offered.

**Test**

We adressed different aspect and scenario of our backend.
In order to run the test you can open the terminal on your PC and run the command: 

`pytest --cov=app --cov-report=html tests/`