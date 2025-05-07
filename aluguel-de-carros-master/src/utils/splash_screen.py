from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):


        # Nome(s) do(s) criador(es)
        self.created_by = "KAYO VINICIUS SILVA BRAGA"
        

    def get_documents_count(self, collection_name):
        # Retorna o total de registros computado pela query
        df = config.query_count(collection_name=collection_name)
        return df[f"total_{collection_name}"].values[0]
   

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE ALUGUEL DE CARROS                   
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - CATEGORIAS:  {str(self.get_documents_count(collection_name="categoria")).rjust(5)}
        #      2 - CLIENTES     {str(self.get_documents_count(collection_name="clientes")).rjust(5)}
        #      3 - CARROS:      {str(self.get_documents_count(collection_name="carro")).rjust(5)}
        #      4 - ALOCAÇÕES:   {str(self.get_documents_count(collection_name="alocacao")).rjust(5)}
        #
        #  CRIADO POR:    {self.created_by}
        #                                  
        #               Banco de dados          
        #              
        ########################################################
        """