#importar bibliotecas
import streamlit as st
import base64
import streamlit.components.v1 as components

@st.cache_data
def carregar_imagem_base64(caminho):
    with open(caminho, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = carregar_imagem_base64("eu.png")
img_bc = carregar_imagem_base64("bc.png")
img_vanzolini = carregar_imagem_base64("vanzolini.png")
img_comerc = carregar_imagem_base64("comerc.png")
img_renova = carregar_imagem_base64("renova.png")
img_pibic = carregar_imagem_base64("pibic.png")





idioma = st.toggle("🌎 English")

####tab
st.markdown("""
<style>

/* Container */
div[data-baseweb="tab-list"] {
    justify-content: center;
    gap: 0px;
}

/* Botão da tab */
div[data-baseweb="tab-list"] button {
    font-weight: 600 !important;
    padding: 10px 20px;
    color: #ffffff !important;
    background-color: transparent !important;
    border-radius: 8px;
}

/* Texto interno */
div[data-baseweb="tab-list"] button p {
    font-weight: 600 !important;
    color: inherit !important;
}



/* Hover */
div[data-baseweb="tab-list"] button:hover {
    color: #00C2FF !important;
    background-color: rgba(0,194,255,0.08) !important;
}

/* Aba selecionada */
div[data-baseweb="tab-list"] button[aria-selected="true"] {
    color: #00C2FF !important;
    background-color: rgba(0,194,255,0.12) !important;
    border-radius: 8px;
    border-bottom: 3px solid #00C2FF !important;
    box-shadow: none !important;
}

div[data-baseweb="tab-highlight"] {
    background-color: #00C2FF !important;
}

</style>
""", unsafe_allow_html=True)

if idioma:
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👤 About me", 
    "💼 Professional Experience", 
    "📊 Projects",
    "🧠 Skills", 
    "📫 Contact"
    ])

    with tab1:
        st.header("About me  \n")
        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            st.markdown(f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{img_base64}" style="
                    width:200px;
                    height:200px;
                    border-radius:50%;
                    object-fit:cover;
                    object-position: 00% 20%;
                    border:1px solid #00C2FF;
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                ">
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <p style='text-align: justify;'>
        <br>
        My name is Leandro, I am 28 years old, and I hold degrees in Science and Technology (2016–2018) and Petroleum Engineering (2019–2022) from UNIFESP, with a strong quantitative background that supports my work with data, from collection and processing to the generation of strategic insights. Over more than five years of professional experience, I have built a career focused on data analysis and decision-making support, working in diverse organizational contexts and dealing with complex, multifactorial problems.

        <br>
        <p style='text-align: justify;'>
        My name is Leandro, I am 28 years old, and I hold degrees in Science and Technology (2016–2018) and Petroleum Engineering (2019–2022) from UNIFESP, with a strong quantitative background that supports my work with data, from collection and processing to the generation of strategic insights. Over more than five years of professional experience, I have built a career focused on data analysis and decision-making support, working in diverse organizational contexts and dealing with complex, multifactorial problems.

        <p style='text-align: justify;'>
        My work involves integrating tools and programming languages such as Python, SQL, and VBA to structure, process, and analyze large volumes of data, transforming raw information into clear, reliable, and actionable insights. I have experience using Power BI to develop dashboards and analytical reports, focusing not only on visualization but also on building data-driven narratives that support strategic and operational decision-making.
        <p style='text-align: justify;'>
        Throughout my experience, I have also worked on organizing and consolidating data from multiple sources — including internal data, open data, and consultancy reports — ensuring consistency, traceability, and quality in analyses. In addition, I have been incorporating the use of artificial intelligence into my daily work to optimize analytical processes, accelerate solution development, and enhance insight generation.
        </p>
        """, unsafe_allow_html=True)



    with tab2:
        st.markdown("""
            <style>
            /* Caixa do expander */
            div[data-testid="stExpander"] {
                border-radius: 10px;
                border: 1px solid rgba(0,194,255,0.2);
                background-color: rgba(0,194,255,0.03);
                transition: all 0.3s ease;
                margin-bottom: 10px;
                overflow: hidden;
            }

            /* Hover */
            div[data-testid="stExpander"]:hover {
                background-color: rgba(0,194,255,0.06);
                transform: translateY(-2px);
            }

            /* Quando aberto (ajuste correto) */
            div[data-testid="stExpander"] details[open] {
                border: 1px solid #00C2FF;
                background-color: rgba(0,194,255,0.02);
            }

            div[data-testid="stExpander"] summary * {
                font-weight: 700 !important;
                font-size: 16px !important;
            }
            </style>
        """, unsafe_allow_html=True)
        st.header("Professional Experience")

        with st.expander("Grupo BC Energia (2024-2026)"):
            
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_bc}" style="
                        width:100px;
                        height:100px;
                        border-radius:50%;
                        object-fit:cover;
                        object-position: 00% 20%;
                        border:1px solid #ddd;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    ">
                </div>
                """, unsafe_allow_html=True)
            st.markdown("""
            <p style='text-align: justify;'>
            <br>
            I worked in the Middle Office area with a strong focus on data analysis applied to the energy market, providing direct support for price formation and strategic decision-making. My role involved collecting, processing, and consolidating data from multiple sources — including energy, electrical, hydrological, open data, and consulting firm information — ensuring consistency, traceability, and quality of the datasets used in analyses.

            <p style='text-align: justify;'>
            I was responsible for structuring and maintaining historical databases used in PLD forecasting studies, organizing relevant variables and enabling comparative analyses between current scenarios and past periods with similar characteristics. This work required not only technical data processing but also critical analysis to identify patterns, outliers, and potential inconsistencies that could impact the projections.

            <p style='text-align: justify;'>
            I developed diagnostic and forecasting reports focused on interpreting electro-energetic and hydrometeorological conditions, assessing their impact on price behavior, and directly supporting areas such as trading, pricing, and market intelligence. These analyses were used both internally and as support in interactions with clients and stakeholders.
            
            <p style='text-align: justify;'>
            I also worked on creating interactive dashboards in Power BI, designing visualizations focused on monitoring key indicators and price scenarios. The dashboards were built with an emphasis on clarity, usability, and decision support, enabling quick analyses and comparisons across different variables and time horizons.
            
            <p style='text-align: justify;'>
            In addition, I developed automations in Python for data collection, processing, and storage, including API integration and the execution of SQL queries (via SQLite) within the code itself. This significantly reduced manual effort, increased the frequency of database updates, and improved the reliability of the analyses.

            <p style='text-align: justify;'>
            I actively participated in technical meetings with institutions in the electricity sector and in internal discussions, acting as a bridge between data and business by translating complex information into clear and actionable insights. I also contributed to organizing model execution routines, standardizing analytical processes, and promoting best practices in data usage.                        
            </p>
            
                        
            """, unsafe_allow_html=True)

            if "img_index" not in st.session_state:
                st.session_state.img_index = 0

            imagens = [
            "BIs/Carga1H.png",
            "BIs/Carga2H.png",
            "BIs/Carga1F.png",
            "BIs/Carga2F.png",
            "BIs/Carga3F.png",
            "BIs/Carga4F.png",
            "BIs/EARM1H.png",
            "BIs/EARM2H.png",
            "BIs/EARM3H.png",
            "BIs/EARM4H.png",
            "BIs/ENA1H.png",
            "BIs/ENA2H.png",
            "BIs/ENA3H.png",
            "BIs/ENA1F.png",
            "BIs/ENA2F.png",
            "BIs/ENA3F.png",
            "BIs/Hidrologia1.png",
            "BIs/PLD1H.png",
            "BIs/PLD2H.png",
            "BIs/Precip1F.png",
            "BIs/Precip1H.png",
            "BIs/Precip2H.png",
            "BIs/RodadaPreco1.png",
            ]
            

            st.markdown("<p style='text-align: center;'> <u><b>Developed dashboards</b></u>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1,18,1])

            with col1:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                if st.button("◀"):
                    st.session_state.img_index = (st.session_state.img_index - 1) % len(imagens)

            with col2:
                st.image(imagens[st.session_state.img_index], use_container_width=True)

            with col3:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                if st.button("▶"):
                    st.session_state.img_index = (st.session_state.img_index + 1) % len(imagens)

        with st.expander("Fundação Vanzolini (2024-2026)"):
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_vanzolini}" style="
                        width:100px;
                        height:100px;
                        border-radius:50%;
                        object-fit:cover;
                        object-position: 50% 20%;
                        border:1px solid #ddd;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    ">
                </div>
                """, unsafe_allow_html=True)
            st.markdown("""
            <p style='text-align: justify;'>
        
            <p style='text-align: justify;'>          
            I worked as an analyst and, at certain periods, as a coordinator on projects focused on the public sector and strategic institutions, such as SABESP, PRODESP, municipal governments, and port operations (CODEBA), with a focus on applying data analysis to support management and decision-making. My role involved both technical execution and team coordination, assigning tasks, monitoring deliverables, and ensuring the quality and alignment of results with project objectives.

            <p style='text-align: justify;'>
            From a technical standpoint, I used Python for data collection, processing, organization, and analysis from various sources, structuring consistent datasets for studies and reports. In specific projects, I also worked with geolocation and spatial analysis, using Python libraries and tools such as QGIS for handling geographic data, generating maps, and supporting territorial analyses, contributing to studies with a relevant spatial dimension.

            <p style='text-align: justify;'>
            In addition, I participated in the development of solutions that incorporated artificial intelligence to support analysis and automate operational steps, with the goal of increasing process efficiency, reducing execution time, and standardizing analytical deliverables. These initiatives contributed to improving team productivity and the consistency of delivered results.
            
            <p style='text-align: justify;'>
            I also played an active role in the preparation of technical documents, specialized reports, and institutional materials, translating complex analyses into clear and well-structured content for different audiences. In parallel, I worked on the development of courses and educational materials, contributing to the technical training of professionals and the dissemination of knowledge in public and organizational contexts.
            
            <p style='text-align: justify;'>
            This experience combined analytical work, team coordination, and the production of technical content, always with a focus on generating value through the structured use of data, process standardization, and the continuous improvement of deliverables.                        
            </p>
            
                        
            """, unsafe_allow_html=True)

        with st.expander("Comerc Energia (2021-2022)"):
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_comerc}" style="
                        width:100px;
                        height:100px;
                        border-radius:50%;
                        object-fit:cover;
                        object-position: 00% 20%;
                        border:1px solid #ddd;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    ">
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
            <br>       
            <p style='text-align: justify;'>          
            I worked in the Generator Management area, focusing on the analysis and interpretation of operational and regulatory data from power generation assets. My responsibilities included monitoring asset performance, organizing and consolidating technical information, and preparing specialized reports aimed at both internal support and client service, as well as supporting regulatory advisory activities.

            <p style='text-align: justify;'>
            On a daily basis, I worked with data related to asset operation and performance, structuring analyses that enabled the evaluation of efficiency indicators, regulatory compliance, and operational conditions. These analyses were used as a basis for decision-making support, contributing to greater clarity regarding asset performance and the identification of improvement opportunities.

            <p style='text-align: justify;'>
            I actively participated in cross-functional interactions, promoting integration between technical, regulatory, and commercial teams, especially in discussions related to energy commercialization strategies. In this context, the use of data was essential to support decisions and align expectations across teams, ensuring greater consistency in the strategies adopted.
            
            <p style='text-align: justify;'>
            I also worked on optimizing internal processes through the implementation of automations using VBA and Python, reducing manual activities, standardizing operational routines, and increasing the reliability of deliverables. These automations contributed to significant efficiency gains, allowing greater focus on strategic analysis and less effort on repetitive tasks.
            
            <p style='text-align: justify;'>
            Overall, my role combined data analysis, regulatory support, process automation, and business interface, always focusing on information quality, operational efficiency, and decision-making support.                        
            </p>
            
                        
            """, unsafe_allow_html=True)
        
        with st.expander("Renova Consultoria (2021)"):
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_renova}" style="
                        width:100px;
                        height:100px;
                        border-radius:50%;
                        object-fit:cover;
                        object-position: 00% 20%;
                        border:1px solid #ddd;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    ">
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
        
            <p style='text-align: justify;'>          
            Temporary work focused on automating processes and calculations within a biomass power plant system, with an emphasis on standardization and agility in handling operational spreadsheets. I worked on developing solutions in VBA (Visual Basic for Applications) to automate repetitive routines, structure calculations, and reduce manual intervention, contributing to greater consistency and reliability of the information used in analyses and internal controls.
            </p>
            
                        
            """, unsafe_allow_html=True)

        with st.expander("PIBIC - CNPQ (2018-2021)"):
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_pibic}" style="
                        width:100px;
                        height:100px;
                        border-radius:50%;
                        object-fit:cover;
                        object-position: 50% 20%;
                        border:1px solid #ddd;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    ">
                </div>
                """, unsafe_allow_html=True)
            st.markdown("""
            <p style='text-align: justify;'>
    
            <p style='text-align: justify;'>          
            Research project focused on applying data analysis and Machine Learning techniques to model environmental variables, with an emphasis on solar irradiation prediction. In the initial phase, I participated in the development of Artificial Neural Networks, working from data collection and organization to preprocessing, variable selection, model training, and performance evaluation. This phase involved experimenting with different architectures and parameters to understand model behavior and generalization capacity.

            <p style='text-align: justify;'>
            Throughout the project, I used Python as the main tool, building data pipelines for processing, cleaning, and preparing datasets, as well as implementing Machine Learning models. Later, I advanced to using established libraries such as scikit-learn, which enabled more efficient development, greater focus on result validation, and comparison across different modeling approaches, while maintaining attention to data quality and prediction consistency.

            <p style='text-align: justify;'>
            In addition to modeling, I contributed to the critical analysis of results, evaluating performance metrics and identifying model limitations in the face of natural variations in environmental data, such as seasonality and atypical weather conditions. This stage was essential for properly interpreting results within context.
            
            <p style='text-align: justify;'>
            In a complementary project, I used the PVSyst tool to conduct an energy efficiency study and assess the solar power generation potential of buildings at UNIFESP, Santos campus. The work involved simulating photovoltaic generation scenarios, considering variables such as solar irradiation, system characteristics, and local conditions. Based on this, comparative analyses were developed to evaluate energy performance and solar utilization potential, contributing to the understanding of technical feasibility and supporting decision-making in an institutional context.
            
            <p style='text-align: justify;'>
            Overall, the experience integrated concepts from data science, statistical modeling, energy simulation, and scenario analysis, strengthening my ability to work with complex data, structure analyses, and extract relevant insights across different contexts.                        
            </p>
            
                        
            """, unsafe_allow_html=True)

    with tab3:
        with st.expander("Energy Consumption Dashboard"):
            st.markdown("<p style='text-align: center;'> <u><b>Net Load Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for net load forecast analysis, focusing on daily and hourly variations across different models and run dates.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to calculate variations, compare models, and perform temporal analysis. Data processing techniques, dynamic filters, and segmentations were applied, enabling interactive and flexible navigation.
            <p style='text-align: justify;'>
            The objective of the dashboard is to compare forecast scenarios, identify differences between models, and analyze load behavior over time, supporting decision-making and the interpretation of system variations.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/CargaLiquida1.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Gross Load and Temperature Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for gross load analysis with a focus on correlation with temperature, allowing the evaluation of hourly and daily variations across different models and run dates.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to calculate variations, compare scenarios, and integrate climate variables. Data organization techniques, dynamic filters, and segmentations were applied, enabling an interactive and exploratory analysis.
            <p style='text-align: justify;'>
            The objective of the dashboard is to identify patterns and relationships between load and temperature, evaluating possible correlations and supporting the interpretation of the impact of climate factors on energy consumption.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/CargaLiquida2.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Weekly Load Forecast Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for monitoring weekly load forecasts, enabling continuous comparison between forecasted and actual values throughout the operational week.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to calculate variations, consolidate indicators, and analyze adherence between models (DECOMP) and actual data (IPDO). Dynamic updating techniques, historical comparisons, and interactive filters were applied to support data exploration.
            <p style='text-align: justify;'>
            The objective of the dashboard is to monitor the daily evolution of forecasts, evaluate deviations (delta) between forecasted and actual values, and analyze model accuracy over time, supporting decision-making and operational monitoring.           
            </p>                           
            """, unsafe_allow_html=True)
            st.video("BIs/CargaLiquida3.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Structural Load Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for structural load forecast analysis, integrating different temporal views and comparisons between historical data and future projections.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to consolidate indicators, analyze variations, and compare scenarios. Multiple data sources were integrated, including PEN projections, DECOMP revisions, and macroeconomic indicators such as GDP (Focus), along with the application of dynamic filters and segmentations for interactive exploration.
            <p style='text-align: justify;'>
            The objective of the dashboard is to monitor the evolution of load projections, evaluate revisions over time, and analyze consistency across different scenarios, supporting the interpretation of the structural behavior of energy demand.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/CargaLiquida4.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Load Historical Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for analyzing energy load behavior, focusing on the distribution across subsystems and the temporal evolution of consumption.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to consolidate daily and monthly indicators, as well as enabling comparisons across periods and different regions of the system. Data structuring techniques, dynamic filters, and interactivity through tooltips were applied, allowing for intuitive and exploratory navigation.
            <p style='text-align: justify;'>
            The objective of the dashboard is to provide a clear and accessible view of energy consumption, enabling the identification of patterns, trends, and the representativeness of each subsystem, supporting comparative analysis and the interpretation of the behavior of the National Interconnected System over time.
            </p>          
                 
            """, unsafe_allow_html=True)
            st.video("BIs/CargaLiquida5.mp4")



        with st.expander("EARM Dashboards (Energy Storage)"):
            st.markdown("<p style='text-align: center;'> <u><b>EARM Historical Dashboard</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed to monitor energy storage levels (EARM), enabling daily and monthly historical analysis by subsystem.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to consolidate indicators, perform temporal comparisons, and analyze seasonality. Dynamic filters for period, subsystem, and type of metric (percentage or MWm) were applied, enabling interactive and flexible navigation.
            <p style='text-align: justify;'>
            The objective of the dashboard is to monitor reservoir behavior over time, compare levels across different periods, and support the analysis of the system’s energy availability.
            </p>                     
                 
            """, unsafe_allow_html=True)
            st.video("BIs/EARM1.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Daily EARM Monitoring Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed to monitor variations in reservoir levels (EARM) by subsystem, focusing on quick and objective comparisons.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to calculate daily variations in MWm and percentage. Visual organization techniques and graphical indicators were applied to facilitate data interpretation.
            <p style='text-align: justify;'>
            The objective of the dashboard is to enable agile analysis of increases or decreases in reservoir levels, supporting operational monitoring and decision-making.
                        
            </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/EARM2H.png")

            st.markdown("<p style='text-align: center;'> <u><b>EARM Monitoring by Reservoir Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for detailed analysis of EARM by reservoir, enabling exploration by basin, subsystem, and different time granularities.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to consolidate indicators, perform temporal comparisons, and calculate the representativeness of reservoirs within each subsystem. Chained dynamic filters (basin, reservoir, and subsystem) were applied, along with visualization options in MWm and percentage.
            <p style='text-align: justify;'>
            The objective of the dashboard is to deepen the analysis of reservoir behavior, allowing the identification of patterns, comparison across periods, and evaluation of each asset’s contribution to the total system storage.           

            </p>         
                            
            """, unsafe_allow_html=True)
            st.video("BIs/EARM2.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>EARM Monitoring by Basin Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for EARM analysis by basin within the National Interconnected System, enabling daily, monthly, and period-over-period comparisons.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to consolidate indicators and perform temporal comparisons. Dynamic filters for period and metric type (MWm and percentage) were applied, enabling interactive and flexible navigation.
            <p style='text-align: justify;'>
            The objective of the dashboard is to analyze basin behavior over time, identify patterns, and support the interpretation of the evolution of energy storage within the system.
            </p>        
                 
            """, unsafe_allow_html=True)
            st.video("BIs/EARM3.mp4")



        with st.expander("ENA Dashboards (Natural Inflow Energy)"):
            st.markdown("<p style='text-align: center;'> <u><b>ENA Historical Dashboard</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for ENA analysis of the National Interconnected System, focusing on comparisons across periods and its relationship with the Long-Term Average (LTA).
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to consolidate indicators, perform calculations relative to the LTA, and compare subsystems. Dynamic filters for period and metric type (MWm and percentage of LTA) were applied, along with complementary visualizations to analyze each subsystem’s contribution to the SIN.
            <p style='text-align: justify;'>
            The objective of the dashboard is to monitor ENA behavior over time, identify deviations from the LTA, and analyze the contribution of each subsystem within the context of the electrical system.
            </p>      
                 
            """, unsafe_allow_html=True)
            st.video("BIs/ENA1.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Daily ENA Monitoring Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed to monitor the daily variation of ENA by subsystem, focusing on comparison with the previous day.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to calculate daily variations. Period filters and complementary visual resources, such as bar charts, were applied to facilitate interpretation.
            <p style='text-align: justify;'>
            The objective of the dashboard is to enable quick analysis of ENA fluctuations, supporting operational monitoring and the identification of relevant variations in the system.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/ENA2H.png")


            st.markdown("<p style='text-align: center;'> <u><b>ENA by Basin Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed to monitor ENA by basin, enabling daily and monthly analysis over time.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to consolidate indicators and perform temporal comparisons. Dynamic filters for period and metric type (MWm and percentage) were applied, along with integration of geographic visualization for basin location.
            <p style='text-align: justify;'>
            The objective of the dashboard is to analyze ENA behavior by region, compare periods, and support the interpretation of hydrological evolution in the system. The objective of the dashboard is to monitor ENA behavior over time, identify deviations from the LTA, and analyze the contribution of each subsystem within the context of the electrical system.
            </p>           
                 
            """, unsafe_allow_html=True)
            st.video("BIs/ENA2.mp4")


            st.markdown("<p style='text-align: center;'> <u><b>Daily ENA Forecast Monitoring Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for analyzing future ENA expectations, based on different models and weekly revisions.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to consolidate indicators and compare scenarios. Dynamic filters by model and period were applied, allowing the analysis of forecast evolution over recent days.
            <p style='text-align: justify;'>
            The objective of the dashboard is to compare ENA projections across models and revisions, enabling the evaluation of trends and recent variations in the system’s hydrological expectations.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/ENA1F.png")


            st.markdown("<p style='text-align: center;'> <u><b>Comparative ENA Forecast Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for analyzing the future behavior of ENA by subsystem, on both daily and monthly bases.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to compare forecast models and different publication periods. Dynamic filters were applied, allowing switching between granularities and scenarios.
            <p style='text-align: justify;'>
            The objective of the dashboard is to compare ENA projections, evaluate variations between models, and analyze the evolution of hydrological expectations over time.
            </p>             
                 
            """, unsafe_allow_html=True)
            st.image("BIs/ENA2F.png")


            st.markdown("<p style='text-align: center;'> <u><b>Comparative ENA Forecast Dashboard by Model and Period</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for comparative analysis of ENA forecasts across models, focusing on daily and monthly values by subsystem.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to calculate variations between models, compare with the LTA, and consolidate monthly indicators. Dynamic filters by run date and subsystem were applied, enabling interactive and detailed analysis.
            <p style='text-align: justify;'>
            The objective of the dashboard is to compare forecasts across models, evaluate daily and monthly differences, and analyze ENA positioning relative to the historical average, supporting the interpretation of hydrological expectations.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/ENA3F.png")
        

        with st.expander("PLD Dashboards"):
            st.markdown("<p style='text-align: center;'> <u><b>PLD Historical Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for energy price analysis (PLD and CMO), focusing on daily monitoring and monthly comparisons by subsystem.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to consolidate indicators and compare variables across periods. Dynamic filters for period and subsystem were applied, enabling interactive and flexible navigation.
            <p style='text-align: justify;'>
            The objective of the dashboard is to monitor the difference between PLD and CMO, analyze their evolution over time, and support the interpretation of price behavior in the electrical system.
            </p>           
                 
            """, unsafe_allow_html=True)
            st.video("BIs/PLD1.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>PLD Monitoring Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed to monitor PLD and CMO, focusing on daily and monthly analysis by subsystem.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to consolidate averages, compare variables, and analyze different granularities. Dynamic period filters were applied, allowing switching between monthly views and detailed daily breakdowns.
            <p style='text-align: justify;'>
            The objective of the dashboard is to monitor PLD behavior throughout the month, compare it with CMO on a monthly basis, and support more detailed analyses in specific periods.
            </p>           
                 
            """, unsafe_allow_html=True)
            st.video("BIs/PLD2.mp4")
        

        with st.expander("Precipitation Dashboards"):
            st.markdown("<p style='text-align: center;'> <u><b>Precipitation Forecast Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for precipitation analysis, focusing on comparisons between models and variations across periods and regions.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to calculate differences between models and consolidate indicators. Dynamic filters by subsystem, period, models, and run dates were applied, along with the integration of geospatial data to associate basins and regions.
            <p style='text-align: justify;'>
            The objective of the dashboard is to compare precipitation forecasts across models, analyze variations over time, and support the interpretation of hydrological scenarios.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/Precip1F.png")

            st.markdown("<p style='text-align: center;'> <u><b>Precipitation Monitoring Dashboard</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard developed for analyzing observed rainfall, focusing on accumulated values by basin and comparison with forecasts from different models.
            <p style='text-align: justify;'>
            The solution was built in Power BI, using data modeling and DAX measures to calculate accumulations and compare observed versus forecasted values. Period filters and data organization by basin were applied, enabling a clear and objective analysis.
            <p style='text-align: justify;'>
            The objective of the dashboard is to compare observed precipitation with forecasts, evaluate model adherence, and support the interpretation of hydrological scenarios.
            </p>           
                 
            """, unsafe_allow_html=True)
            st.image("BIs/Precip1H.png")        

    with tab4:
        #st.header("Habilidades")
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            html_code = """
            <div style="
                display: flex;
                justify-content: center;
                align-items: center;
                height: 300px;
                width: 100%;
            ">
            <div id="tagcloud" style="width: 100%; height: 300px;"></div>

            <style>
            #tagcloud span {
                color: #00C2FF !important; /* cor gelo */
                font-weight: bold;
                font-size: 14px;
            }
            </style>

            <script src="https://cdn.jsdelivr.net/npm/TagCloud@2.2.0/dist/TagCloud.min.js"></script>

            <script>
            const container = '#tagcloud';
            const texts = [
                'Python','SQL','Power BI','VBA','ETL','Modeling','APIs','Microsoft Office','Automation',
                'Data','Storytelling', 'AI',
                'Comunication','Team Work','Problem Solving'
            ];

            TagCloud(container, texts, {
                radius: 110,
                maxSpeed: 'fast',
                initSpeed: 'normal',
                direction: 135,
                keep: true
            });
            </script>
            """

            components.html(html_code, height=200)

        st.subheader("Languages")
            
        st.write("- Portuguese")
        st.progress(1.0)
        st.write("- English")
        st.progress(0.8)
        st.markdown("""
        <p style='text-align: justify;'>
    
        <br>
        </p>
        """, unsafe_allow_html=True)

        
        st.subheader("Programming Languages & Tools")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("- Python")
            st.write("- SQL")

        with col2:
            st.write("- VBA")
            st.write("- Pacote Office")
        
        with col3:
            st.write("- Power BI")
            st.write("- Tableau")


        st.subheader("AI Applied to Data")

        col1, col2 = st.columns(2)

        with col1:
            st.write("- AI Agents")
        with col2:
            st.write("- Process Automation")

        st.subheader("BI & Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.write("- Data Analysis")
            st.write("- Data Visualization")
            st.write("- Definition of Metrics and KPIs")

        with col2:
            st.write("- Data Storytelling")
            st.write("- KPI Monitoring & Tracking")
            st.write("- Identification of Business Insights")

        st.subheader("Data Engineering & Processing")

        col1, col2 = st.columns(2)

        with col1:
            st.write("- ETL")
            st.write("- Data Modeling")
            

        with col2:
            st.write("- APIs")
            st.write("- Process Automation")
            


        st.subheader("Soft Skills")

        col1, col2 = st.columns(2)

        with col1:
            st.write("- Teamwork")   
            st.write("- Critical Thinking")
            st.write("- Clear Communication")
            st.write("- Proactivity")
            st.write("- Autonomy")

        with col2:
            st.write("- Business-Oriented Thinking")
            st.write("- Problem Solving")
            st.write("- Analytical Thinking")
            st.write("- Attention to Detail")
            st.write("- Adaptability")
        

            
            


        

        
    with tab5:
        st.header("Contact")
        st.markdown("""
        <p style='text-align: justify;'>
        Available for opportunities in the areas of data analysis, business intelligence, and data engineering, with a focus on transforming data into strategic decisions. Feel free to get in touch for opportunities, collaborations, or discussions about data and technology. I am currently seeking remote work opportunities, but I am also available to travel when necessary for meetings or in-person engagements.
        </p>
        """, unsafe_allow_html=True)
        st.subheader("Direct Contact")
        st.write("📧 Email: leandro_menali@hotmail.com")
        st.write("🔗 LinkedIn: https://www.linkedin.com/in/leandro-menali-ferreira-463355165/")
        st.write("📱 Phone: (35) 99124-3069")
        st.write("📍 Location: Passos, Minas Gerais, Brazil")
else:
    st.markdown("""
    <style>
    div[data-baseweb="tab"] {
        padding: 6px 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "👤 Sobre mim", 
        "💼 Experiências Profissionais", 
        "📊 Projetos",
        "🧠 Habilidades", 
        "📫 Contato"
    ])

    with tab1:
        st.header("Sobre mim  \n")
        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            st.markdown(f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{img_base64}" style="
                    width:200px;
                    height:200px;
                    border-radius:50%;
                    object-fit:cover;
                    object-position: 00% 20%;
                    border:1px solid #00C2FF;
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                ">
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
        <p style='text-align: justify;'>
        <br>
        Me chamo Leandro, tenho 28 anos, sou formado em Ciência e Tecnologia (2016-2018) e Engenharia de Petróleo (2019-2022) pela UNIFESP, com uma base quantitativa sólida que sustenta minha atuação em dados, desde a coleta e tratamento até a geração de insights estratégicos. Ao longo de mais de cinco anos de experiência profissional, construí uma trajetória voltada à análise de dados e suporte à tomada de decisão, atuando em diferentes contextos organizacionais e lidando com problemas complexos e multifatoriais.

        <br>
        <p style='text-align: justify;'>
        Minha atuação envolve a integração de ferramentas e linguagens como Python, SQL e VBA para estruturar, tratar e analisar grandes volumes de dados, transformando informações brutas em análises claras, confiáveis e acionáveis. Tenho experiência na utilização do Power BI para desenvolvimento de dashboards e relatórios analíticos, com foco não apenas na visualização, mas na construção de narrativas que apoiem decisões estratégicas e operacionais.

        <p style='text-align: justify;'>
        Ao longo da minha experiência, também atuei na organização e consolidação de dados provenientes de múltiplas fontes — incluindo dados internos, dados abertos e informações de consultorias — garantindo consistência, rastreabilidade e qualidade das análises. Além disso, venho incorporando o uso de inteligência artificial no meu dia a dia para otimizar processos analíticos, acelerar o desenvolvimento de soluções e ampliar a geração de insights.
        <p style='text-align: justify;'>
        Trabalho de forma colaborativa com equipes multidisciplinares, conectando áreas técnicas e de negócio, sempre com foco em traduzir dados complexos em informações acessíveis. Tenho como pilares o comprometimento, a curiosidade e o aprendizado contínuo, buscando constantemente evoluir tecnicamente e gerar impacto real por meio de soluções orientadas por dados.
        </p>
        """, unsafe_allow_html=True)



    with tab2:
        st.markdown("""
            <style>
            /* Caixa do expander */
            div[data-testid="stExpander"] {
                border-radius: 10px;
                border: 1px solid rgba(0,194,255,0.2);
                background-color: rgba(0,194,255,0.03);
                transition: all 0.3s ease;
                margin-bottom: 10px;
                overflow: hidden;
            }

            /* Hover */
            div[data-testid="stExpander"]:hover {
                background-color: rgba(0,194,255,0.06);
                transform: translateY(-2px);
            }

            /* Quando aberto (ajuste correto) */
            div[data-testid="stExpander"] details[open] {
                border: 1px solid #00C2FF;
                background-color: rgba(0,194,255,0.02);
            }

            div[data-testid="stExpander"] summary * {
                font-weight: 700 !important;
                font-size: 16px !important;
            }
            </style>
        """, unsafe_allow_html=True)
        st.header("Experiências Profissionais")


        with st.expander("Grupo BC Energia (2024-2026)"):
            
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_bc}" style="
                        width:100px;
                        height:100px;
                        border-radius:50%;
                        object-fit:cover;
                        object-position: 00% 20%;
                        border:1px solid #ddd;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    ">
                </div>
                """, unsafe_allow_html=True)
            st.markdown("""
            <p style='text-align: justify;'>
            <br>
            Atuei na área de Middle Office com forte foco em análise de dados aplicada ao mercado de energia, dando suporte direto à formação de preços e à tomada de decisão estratégica. Minha atuação envolvia a coleta, tratamento e consolidação de dados provenientes de múltiplas fontes — incluindo dados energéticos, elétricos, hidrológicos, dados abertos e informações de consultorias — garantindo consistência, rastreabilidade e qualidade das bases utilizadas nas análises.

            <p style='text-align: justify;'>
            Fui responsável por estruturar e manter bases históricas utilizadas em estudos de projeção do PLD, organizando variáveis relevantes e permitindo análises comparativas entre cenários atuais e períodos passados com características semelhantes. Esse trabalho exigia não apenas o tratamento técnico dos dados, mas também uma análise crítica para identificar padrões, outliers e possíveis inconsistências que pudessem impactar as projeções.

            <p style='text-align: justify;'>
            Desenvolvi relatórios diagnósticos e prognósticos com foco na interpretação das condições eletroenergéticas e hidrometeorológicas, avaliando impactos no comportamento dos preços e apoiando diretamente áreas como trading, precificação e inteligência de mercado. Essas análises eram utilizadas tanto internamente quanto como suporte em interações com clientes e stakeholders.
            
            <p style='text-align: justify;'>
            Também atuei na criação de dashboards interativos em Power BI, estruturando visualizações voltadas ao acompanhamento de indicadores-chave e cenários de preço. Os dashboards eram construídos com foco em clareza, usabilidade e apoio à decisão, permitindo análises rápidas e comparações entre diferentes variáveis e horizontes de tempo.
            
            <p style='text-align: justify;'>
            Além disso, desenvolvi automações em Python para coleta, tratamento e armazenamento de dados, incluindo integração com APIs e execução de queries SQL (via SQLite) dentro do próprio código. Isso reduziu significativamente o esforço manual, aumentou a frequência de atualização das bases e melhorou a confiabilidade das análises.

            <p style='text-align: justify;'>
            Participei ativamente de reuniões técnicas com instituições do setor elétrico e de discussões internas, atuando como ponte entre dados e negócio, traduzindo informações complexas em insights claros e acionáveis. Também contribuí na organização de rotinas de execução de modelos, padronização de processos analíticos e disseminação de boas práticas no uso de dados.                        
            </p>
            
                        
            """, unsafe_allow_html=True)

            if "img_index" not in st.session_state:
                st.session_state.img_index = 0

            imagens = [
            "BIs/Carga1H.png",
            "BIs/Carga2H.png",
            "BIs/Carga1F.png",
            "BIs/Carga2F.png",
            "BIs/Carga3F.png",
            "BIs/Carga4F.png",
            "BIs/EARM1H.png",
            "BIs/EARM2H.png",
            "BIs/EARM3H.png",
            "BIs/EARM4H.png",
            "BIs/ENA1H.png",
            "BIs/ENA2H.png",
            "BIs/ENA3H.png",
            "BIs/ENA1F.png",
            "BIs/ENA2F.png",
            "BIs/ENA3F.png",
            "BIs/Hidrologia1.png",
            "BIs/PLD1H.png",
            "BIs/PLD2H.png",
            "BIs/Precip1F.png",
            "BIs/Precip1H.png",
            "BIs/Precip2H.png",
            "BIs/RodadaPreco1.png",
            ]
            

            st.markdown("<p style='text-align: center;'> <u><b>Dashboards desenvolvidos</b></u>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1,18,1])

            with col1:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                if st.button("◀"):
                    st.session_state.img_index = (st.session_state.img_index - 1) % len(imagens)

            with col2:
                st.image(imagens[st.session_state.img_index], use_container_width=True)

            with col3:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                if st.button("▶"):
                    st.session_state.img_index = (st.session_state.img_index + 1) % len(imagens)

        with st.expander("Fundação Vanzolini (2024-2026)"):
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_vanzolini}" style="
                        width:100px;
                        height:100px;
                        border-radius:50%;
                        object-fit:cover;
                        object-position: 50% 20%;
                        border:1px solid #ddd;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    ">
                </div>
                """, unsafe_allow_html=True)
            st.markdown("""
            <p style='text-align: justify;'>
        
            <p style='text-align: justify;'>          
            Atuei como analista e, em determinados períodos, como coordenador em projetos voltados ao setor público e a instituições estratégicas, como SABESP, PRODESP, prefeituras municipais e operações portuárias (CODEBA), com foco na aplicação de análise de dados para suporte à gestão e à tomada de decisão. Minha atuação envolvia tanto a execução técnica quanto a coordenação de equipes, distribuindo atividades, acompanhando entregas e garantindo a qualidade e aderência dos resultados aos objetivos dos projetos.

            <p style='text-align: justify;'>
            No aspecto técnico, utilizei Python para coleta, tratamento, organização e análise de dados provenientes de diferentes fontes, estruturando bases consistentes para estudos e relatórios. Em projetos específicos, também trabalhei com geolocalização e análise espacial, utilizando bibliotecas de Python e ferramentas como QGIS para manipulação de dados geográficos, geração de mapas e suporte a análises territoriais, contribuindo para estudos com dimensão espacial relevante.

            <p style='text-align: justify;'>
            Além disso, participei da construção de soluções que incorporavam inteligência artificial como apoio à análise e à automação de etapas operacionais, com o objetivo de aumentar a eficiência dos processos, reduzir o tempo de execução e padronizar entregas analíticas. Essas iniciativas contribuíram para melhorar a produtividade das equipes e a consistência dos resultados entregues.
            
            <p style='text-align: justify;'>
            Também tive participação ativa na elaboração de documentos técnicos, relatórios especializados e materiais institucionais, traduzindo análises complexas em conteúdos claros e estruturados para diferentes públicos. Paralelamente, atuei no desenvolvimento de cursos e materiais didáticos, contribuindo para a capacitação técnica de profissionais e para a disseminação de conhecimento em contextos públicos e organizacionais.
            
            <p style='text-align: justify;'>
            Essa experiência combinou atuação analítica, coordenação de equipes e produção de conteúdo técnico, sempre com foco em gerar valor por meio do uso estruturado de dados, da padronização de processos e da melhoria contínua das entregas.                        
            </p>
            
                        
            """, unsafe_allow_html=True)

        with st.expander("Comerc Energia (2021-2022)"):
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_comerc}" style="
                        width:100px;
                        height:100px;
                        border-radius:50%;
                        object-fit:cover;
                        object-position: 00% 20%;
                        border:1px solid #ddd;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    ">
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
            <br>       
            <p style='text-align: justify;'>          
            Atuei na área de Gestão de Geradores, com foco na análise e interpretação de dados operacionais e regulatórios de ativos de geração de energia. Minha responsabilidade envolvia o acompanhamento do desempenho dos ativos, organização e consolidação de informações técnicas, além da elaboração de relatórios especializados voltados tanto para suporte interno quanto para atendimento a clientes e apoio à assessoria regulatória.

            <p style='text-align: justify;'>
            No dia a dia, trabalhei com dados relacionados à operação e à performance dos ativos, estruturando análises que permitiam avaliar indicadores de eficiência, conformidade regulatória e condições operacionais. Essas análises eram utilizadas como base para suporte à tomada de decisão, contribuindo para maior clareza sobre o desempenho dos ativos e identificação de oportunidades de melhoria.

            <p style='text-align: justify;'>
            Participei ativamente da interface com diferentes áreas, promovendo a integração entre times técnicos, regulatórios e comerciais, especialmente em discussões relacionadas à estratégia de comercialização de energia. Nesse contexto, o uso de dados foi essencial para embasar decisões e alinhar expectativas entre áreas, garantindo maior consistência nas estratégias adotadas.
            
            <p style='text-align: justify;'>
            Também atuei na otimização de processos internos por meio da implementação de automações utilizando VBA e Python, reduzindo atividades manuais, padronizando rotinas operacionais e aumentando a confiabilidade das entregas. Essas automações contribuíram para ganhos relevantes de eficiência, permitindo maior foco em análises estratégicas e menos esforço em tarefas repetitivas.
            
            <p style='text-align: justify;'>
            De forma geral, minha atuação combinou análise de dados, suporte regulatório, automação de processos e interface com áreas de negócio, sempre com foco na qualidade da informação, eficiência operacional e apoio à tomada de decisão.                        
            </p>
            
                        
            """, unsafe_allow_html=True)
        
        with st.expander("Renova Consultoria (2021)"):
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_renova}" style="
                        width:100px;
                        height:100px;
                        border-radius:50%;
                        object-fit:cover;
                        object-position: 00% 20%;
                        border:1px solid #ddd;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    ">
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
        
            <p style='text-align: justify;'>          
            Trabalho temporário voltado à automatização de processos e cálculos em um sistema de usinas de biomassa, com foco na padronização e agilidade no tratamento de planilhas operacionais. Atuei no desenvolvimento de soluções em VBA (Visual Basic for Applications) para automatizar rotinas repetitivas, estruturar cálculos e reduzir intervenções manuais, contribuindo para maior consistência e confiabilidade das informações utilizadas nas análises e controles internos.
            </p>
            
                        
            """, unsafe_allow_html=True)

        with st.expander("PIBIC - CNPQ (2018-2021)"):
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st.markdown(f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{img_pibic}" style="
                        width:100px;
                        height:100px;
                        border-radius:50%;
                        object-fit:cover;
                        object-position: 50% 20%;
                        border:1px solid #ddd;
                        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                    ">
                </div>
                """, unsafe_allow_html=True)
            st.markdown("""
            <p style='text-align: justify;'>
    
            <p style='text-align: justify;'>          
            Projeto de pesquisa com foco na aplicação de técnicas de análise de dados e Machine Learning voltadas à modelagem de variáveis ambientais, com ênfase na predição de irradiação solar. Em uma primeira etapa, participei do desenvolvimento de Redes Neurais Artificiais, realizando desde a coleta e organização dos dados até o pré-processamento, definição de variáveis, treinamento dos modelos e avaliação de desempenho. Essa fase envolveu experimentação com diferentes arquiteturas e parâmetros, buscando compreender o comportamento dos modelos e sua capacidade de generalização.

            <p style='text-align: justify;'>
            Ao longo do projeto, utilizei Python como principal ferramenta, estruturando pipelines de dados para tratamento, limpeza e preparação das bases, além da implementação dos modelos de Machine Learning. Posteriormente, evoluí para a utilização de bibliotecas prontas, como scikit-learn, o que permitiu maior eficiência no desenvolvimento, foco na validação dos resultados e comparação entre diferentes abordagens de modelagem, mantendo atenção à qualidade dos dados e à consistência das previsões geradas.

            <p style='text-align: justify;'>
            Além da parte de modelagem, participei da análise crítica dos resultados, avaliando métricas de desempenho e identificando limitações dos modelos frente a variações naturais dos dados ambientais, como sazonalidade e condições climáticas atípicas. Essa etapa foi essencial para interpretar os resultados de forma adequada e contextualizada.
            
            <p style='text-align: justify;'>
            Em um projeto complementar, utilizei a ferramenta PVSyst para realizar um estudo de eficiência energética e análise do potencial de geração de energia solar nos edifícios da UNIFESP, campus Santos. O trabalho envolveu a simulação de cenários de geração fotovoltaica, considerando variáveis como irradiação solar, características dos sistemas e condições locais. A partir disso, foram elaboradas análises comparativas que permitiram avaliar o desempenho energético e o potencial de aproveitamento da energia solar, contribuindo para a compreensão de viabilidade técnica e apoio à tomada de decisão no contexto institucional.
            
            <p style='text-align: justify;'>
            De forma geral, a experiência integrou conceitos de ciência de dados, modelagem estatística, simulação energética e análise de cenários, reforçando minha capacidade de trabalhar com dados complexos, estruturar análises e extrair insights relevantes para diferentes contextos.                        
            </p>
            
                        
            """, unsafe_allow_html=True)
        
    with tab3:
        with st.expander("Dashboards de Carga"):
            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Carga Líquida</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise da previsão de carga líquida, com foco nas variações diárias e horárias entre diferentes modelos e datas de rodada.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para cálculo de variações, comparações entre modelos e análise temporal. Foram aplicadas técnicas de tratamento de dados, filtros dinâmicos e segmentações, permitindo uma navegação interativa e flexível.
            <p style='text-align: justify;'>
            O objetivo do dashboard é comparar cenários de previsão, identificar diferenças entre modelos e analisar o comportamento da carga ao longo do tempo, apoiando a tomada de decisão e a interpretação das variações do sistema.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/CargaLiquida1.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Carga Bruta e Temperatura</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise da carga bruta com foco na correlação com a temperatura, permitindo avaliar variações horárias e diárias entre diferentes modelos e datas de rodada.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para cálculo de variações, comparações entre cenários e integração de variáveis climáticas. Foram aplicadas técnicas de organização de dados, filtros dinâmicos e segmentações, possibilitando uma análise interativa e exploratória.
            <p style='text-align: justify;'>
            O objetivo do dashboard é identificar padrões e relações entre carga e temperatura, avaliando possíveis correlações e apoiando a interpretação do impacto de fatores climáticos no consumo de energia.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/CargaLiquida2.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Carga Semanal Prevista</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para acompanhamento da previsão de carga semanal, permitindo a comparação contínua entre valores previstos e realizados ao longo da semana operativa.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para cálculo de variações, consolidação de indicadores e análise de aderência entre modelos (DECOMP) e dados realizados (IPDO). Foram aplicadas técnicas de atualização dinâmica, comparações históricas e uso de filtros interativos para exploração dos dados.
            <p style='text-align: justify;'>
            O objetivo do dashboard é monitorar a evolução diária das previsões, avaliar desvios (delta) entre previsto e realizado e analisar a acurácia dos modelos ao longo do tempo, apoiando a tomada de decisão e o acompanhamento operacional.           
            </p>                           
            """, unsafe_allow_html=True)
            st.video("BIs/CargaLiquida3.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Carga Estrutural</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise da previsão da carga estrutural, integrando diferentes visões temporais e comparativas entre dados históricos e projeções futuras.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para consolidação de indicadores, análise de variações e comparação entre cenários. Foram integradas múltiplas fontes de dados, incluindo projeções do PEN, revisões do DECOMP e indicadores macroeconômicos como o PIB (Focus), além da aplicação de filtros dinâmicos e segmentações para exploração interativa.
            <p style='text-align: justify;'>
            O objetivo do dashboard é permitir o acompanhamento da evolução das projeções de carga, avaliar revisões ao longo do tempo e analisar a consistência entre diferentes cenários, apoiando a interpretação do comportamento estrutural da demanda de energia.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/CargaLiquida4.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Histórico de Carga</b></u>", unsafe_allow_html=True)

            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise do comportamento da carga de energia, com foco na visualização da distribuição entre subsistemas e na evolução temporal do consumo.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para consolidação de indicadores diários e mensais, além de permitir comparações entre períodos e entre diferentes regiões do sistema. Foram aplicadas técnicas de estruturação de dados, filtros dinâmicos e interatividade por meio de tooltips, possibilitando uma navegação intuitiva e exploratória.
            <p style='text-align: justify;'>
            O objetivo do dashboard é fornecer uma visão clara e acessível do consumo de energia, permitindo identificar padrões, tendências e a representatividade de cada subsistema, apoiando análises comparativas e a interpretação do comportamento do Sistema Interligado Nacional ao longo do tempo.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/CargaLiquida5.mp4")



        with st.expander("Dashboards de EARM (Energia de Armazenamento)"):
            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Histórico de EARM</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para acompanhamento do nível de energia de armazenamento (EARM), permitindo a análise histórica diária e mensal por subsistema.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para consolidação de indicadores, comparações temporais e análise de sazonalidade. Foram aplicados filtros dinâmicos de período, subsistema e tipo de grandeza (percentual ou MWm), possibilitando uma navegação interativa e flexível.
            <p style='text-align: justify;'>
            O objetivo do dashboard é monitorar o comportamento dos reservatórios ao longo do tempo, comparar níveis entre diferentes períodos e apoiar a análise da disponibilidade energética do sistema.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/EARM1.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Acompanhamento Diário de EARM</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para acompanhamento das variações do nível dos reservatórios (EARM) por subsistema, com foco em comparações rápidas e objetivas.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para cálculo das variações diárias em MWm e percentual. Foram aplicadas técnicas de organização visual e indicadores gráficos para facilitar a interpretação dos dados.
            <p style='text-align: justify;'>
            O objetivo do dashboard é permitir a análise ágil do aumento ou redução dos níveis dos reservatórios, apoiando o monitoramento operacional e a tomada de decisão.
                        
            </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/EARM2H.png")

            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Acompanhamento EARM por Reservatório</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise detalhada do EARM por reservatório, permitindo a exploração por bacia, subsistema e diferentes granularidades temporais.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para consolidação de indicadores, comparações temporais e cálculo de representatividade dos reservatórios dentro do subsistema. Foram aplicados filtros dinâmicos encadeados (bacia, reservatório e subsistema), além de opções de visualização em MWm e percentual.
            <p style='text-align: justify;'>
            O objetivo do dashboard é aprofundar a análise do comportamento dos reservatórios, permitindo identificar padrões, comparar períodos e avaliar a participação de cada ativo no armazenamento total do sistema.           
            
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/EARM2.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Acompanhamento EARM por Bacia</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise do EARM por bacia do Sistema Interligado Nacional, permitindo o acompanhamento diário, mensal e comparativo entre períodos.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para consolidação de indicadores e comparações temporais. Foram aplicados filtros dinâmicos de período e de grandeza (MWm e percentual), possibilitando uma navegação interativa e flexível.
            <p style='text-align: justify;'>
            O objetivo do dashboard é analisar o comportamento das bacias ao longo do tempo, identificar padrões e apoiar a interpretação da evolução do armazenamento de energia no sistema.
           
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/EARM3.mp4")



        with st.expander("Dashboards de ENA (Energia Natural Afluente)"):
            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Histórico de ENA</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise da ENA do Sistema Interligado Nacional, com foco na comparação entre períodos e na relação com a Média de Longo Termo (MLT).
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para consolidação de indicadores, cálculos em relação à MLT e comparações entre subsistemas. Foram aplicados filtros dinâmicos de período e de grandeza (MWm e percentual da MLT), além de visualizações complementares para análise da participação de cada subsistema no SIN.
            <p style='text-align: justify;'>
            O objetivo do dashboard é acompanhar o comportamento da ENA ao longo do tempo, identificar desvios em relação à MLT e analisar a contribuição de cada subsistema no contexto do sistema elétrico.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/ENA1.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Acompanhamento Diário de ENA</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para acompanhamento da variação diária da ENA por subsistema, com foco na comparação em relação ao dia anterior.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para cálculo das variações diárias. Foram aplicados filtros de período e recursos visuais complementares, como gráficos de barras, para facilitar a interpretação.
            <p style='text-align: justify;'>
            O objetivo do dashboard é permitir uma análise rápida das oscilações da ENA, apoiando o monitoramento operacional e a identificação de variações relevantes no sistema.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/ENA2H.png")


            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de ENA por Bacia</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para acompanhamento da ENA por bacia, permitindo a análise diária e mensal ao longo do tempo.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para consolidação de indicadores e comparações temporais. Foram aplicados filtros dinâmicos de período e de grandeza (MWm e percentual), além da integração com visualização geográfica para localização das bacias.
            <p style='text-align: justify;'>
            O objetivo do dashboard é analisar o comportamento da ENA por região, comparar períodos e apoiar a interpretação da evolução hidrológica no sistema.O objetivo do dashboard é acompanhar o comportamento da ENA ao longo do tempo, identificar desvios em relação à MLT e analisar a contribuição de cada subsistema no contexto do sistema elétrico.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/ENA2.mp4")


            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Acompanhamento Diário de Previsão de ENA</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise das expectativas futuras de ENA, com base em diferentes modelos e revisões semanais.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para consolidação de indicadores e comparação entre cenários. Foram aplicados filtros dinâmicos por modelo e período, permitindo a análise da evolução das previsões nos últimos dias.
            <p style='text-align: justify;'>
            O objetivo do dashboard é comparar projeções de ENA entre modelos e revisões, permitindo avaliar tendências e variações recentes nas expectativas hidrológicas do sistema.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/ENA1F.png")


            st.markdown("<p style='text-align: center;'> <u><b>Dashboard Comparativo de Previsão de ENA</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise do comportamento futuro da ENA por subsistema, em bases diária e mensal.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para comparação entre modelos de previsão e entre diferentes períodos de publicação. Foram aplicados filtros dinâmicos que permitem alternar entre granularidades e cenários.
            <p style='text-align: justify;'>
            O objetivo do dashboard é comparar projeções de ENA, avaliar variações entre modelos e analisar a evolução das expectativas hidrológicas ao longo do tempo.
            </p>             
                 
            """, unsafe_allow_html=True)
            st.image("BIs/ENA2F.png")


            st.markdown("<p style='text-align: center;'> <u><b>Dashboard Comparativo de Previsão de ENA por Modelo e Período</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise comparativa das previsões de ENA entre modelos, com foco em valores diários e mensais por subsistema.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para cálculo de variações entre modelos, comparação com a MLT e consolidação de indicadores mensais. Foram aplicados filtros dinâmicos por data de rodada e subsistema, permitindo uma análise interativa e detalhada.
            <p style='text-align: justify;'>
            O objetivo do dashboard é comparar previsões entre modelos, avaliar diferenças diárias e mensais e analisar o posicionamento da ENA em relação à média histórica, apoiando a interpretação das expectativas hidrológicas.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/ENA3F.png")
        

        with st.expander("Dashboards de PLD"):
            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Histório de PLD</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise dos preços de energia (PLD e CMO), com foco no acompanhamento diário e comparações mensais por subsistema.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para consolidação de indicadores e comparação entre variáveis e períodos. Foram aplicados filtros dinâmicos de período e subsistema, permitindo uma navegação interativa e flexível.
            <p style='text-align: justify;'>
            O objetivo do dashboard é monitorar a diferença entre PLD e CMO, analisar sua evolução ao longo do tempo e apoiar a interpretação do comportamento dos preços no sistema elétrico.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/PLD1.mp4")

            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Acompanhamento de PLD</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para acompanhamento do PLD e CMO, com foco na análise diária e mensal por subsistema.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para consolidação de médias, comparação entre variáveis e análise por diferentes granularidades. Foram aplicados filtros dinâmicos de período, permitindo alternar entre visões mensais e detalhamentos diários.
            <p style='text-align: justify;'>
            O objetivo do dashboard é monitorar o comportamento do PLD ao longo do mês, comparar com o CMO em bases mensais e apoiar análises mais detalhadas em períodos específicos.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.video("BIs/PLD2.mp4")
        

        with st.expander("Dashboards de Precipitação"):
            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Previsão de Precipitação</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise de precipitação, com foco na comparação entre modelos e variações por período e região.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para cálculo de diferenças entre modelos e consolidação de indicadores. Foram aplicados filtros dinâmicos por subsistema, período, modelos e datas de rodada, além da integração de dados geoespaciais para associação entre bacias e regiões.
            <p style='text-align: justify;'>
            O objetivo do dashboard é comparar previsões de precipitação entre modelos, analisar variações ao longo do tempo e apoiar a interpretação de cenários hidrológicos.
            </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/Precip1F.png")

            st.markdown("<p style='text-align: center;'> <u><b>Dashboard de Acompanhamento de Precipitação</b></u>", unsafe_allow_html=True)
            
            st.markdown("""
            <p style='text-align: justify;'>
            Dashboard desenvolvido para análise da chuva realizada, com foco no acumulado por bacia e comparação com previsões de diferentes modelos.
            <p style='text-align: justify;'>
            A solução foi construída no Power BI, utilizando modelagem de dados e medidas em DAX para cálculo de acumulados e comparações entre realizado e previsto. Foram aplicados filtros de período e organização dos dados por bacia, permitindo uma análise clara e objetiva.
            <p style='text-align: justify;'>
            O objetivo do dashboard é comparar a precipitação observada com as previsões, avaliando a aderência dos modelos e apoiando a interpretação dos cenários hidrológicos.
                        </p>            
                 
            """, unsafe_allow_html=True)
            st.image("BIs/Precip1H.png")


    with tab4:
        #st.header("Habilidades")
        col1, col2, col3 = st.columns([1,1,1])
        with col2:
            html_code = """
            <div style="
                display: flex;
                justify-content: center;
                align-items: center;
                height: 300px;
                width: 100%;
            ">
            <div id="tagcloud" style="width: 100%; height: 300px;"></div>

            <style>
            #tagcloud span {
                color: #00C2FF !important; /* cor gelo */
                font-weight: bold;
                font-size: 14px;
            }
            </style>

            <script src="https://cdn.jsdelivr.net/npm/TagCloud@2.2.0/dist/TagCloud.min.js"></script>

            <script>
            const container = '#tagcloud';
            const texts = [
                'Python','SQL','Power BI','VBA','ETL','Modelagem','APIs','Office','Automação',
                'Dados','Storytelling',
                'Comunicação','Trabalho em Equipe','Resolução de Problemas'
            ];

            TagCloud(container, texts, {
                radius: 110,
                maxSpeed: 'fast',
                initSpeed: 'normal',
                direction: 135,
                keep: true
            });
            </script>
            """

            components.html(html_code, height=200)

        st.subheader("Idiomas")
            
        st.write("- Portugês")
        st.progress(1.0)
        st.write("- Inglês")
        st.progress(0.8)
        st.markdown("""
        <p style='text-align: justify;'>
    
        <br>
        </p>
        """, unsafe_allow_html=True)

        
        st.subheader("Linguagens & Ferramentas")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write("- Python")
            st.write("- SQL")

        with col2:
            st.write("- VBA")
            st.write("- Pacote Office")
        
        with col3:
            st.write("- Power BI")
            st.write("- Tableau")


        st.subheader("IA aplicada a Dados")

        col1, col2 = st.columns(2)

        with col1:
            st.write("- Agentes de IA")
        with col2:
            st.write("- Automação de Processos")

        st.subheader("BI & Análise")

        col1, col2 = st.columns(2)

        with col1:
            st.write("- Análise de Dados")
            st.write("- Visualização de Dados")
            st.write("- Monitoramento e Acompanhamento de KPIs")

        with col2:
            st.write("- Storytelling com Dados")
            st.write("- Definição de Métricas e KPIs")
            st.write("- Identificação de Insights para Negócio")

        st.subheader("Engenharia & Tratamento de Dados")

        col1, col2 = st.columns(2)

        with col1:
            st.write("- ETL")
            st.write("- Modelagem de Dados")
            

        with col2:
            st.write("- APIs")
            st.write("- Automação de Processos")
            


        st.subheader("Soft Skills")

        col1, col2 = st.columns(2)

        with col1:
            st.write("- Trabalho em Equipe")   
            st.write("- Pensamento Crítico")
            st.write("- Comunicação Clara")
            st.write("- Proatividade")
            st.write("- Autonomia")

        with col2:
            st.write("- Pensamento Orientado a Negócio")
            st.write("- Resolução de Problemas")
            st.write("- Pensamento Analítico")
            st.write("- Atenção a Detalhes")
            st.write("- Adaptabilidade")
        

            
            


            

        
    with tab5:
        st.header("Contato")
        st.markdown("""
        <p style='text-align: justify;'>
        Disponível para oportunidades nas áreas de análise de dados, business intelligence e engenharia de dados, com foco em transformar dados em decisões estratégicas. Fique à vontade para entrar em contato para oportunidades, colaborações ou conversas sobre dados e tecnologia. Atualmente, busco oportunidades de trabalho remoto, porém também tenho disponibilidade para locomoção em caso de reuniões ou encontros presenciais.
        </p>
        """, unsafe_allow_html=True)
        st.subheader("Contato direto")
        st.write("📧 Email: leandro_menali@hotmail.com")
        st.write("🔗 LinkedIn: https://www.linkedin.com/in/leandro-menali-ferreira-463355165/")
        st.write("📱 Telefone: (35) 99124-3069")
        st.write("📍 Local: Passos, Minas Gerais, Brasil")
        
        

