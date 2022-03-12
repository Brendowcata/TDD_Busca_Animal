from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:/Users/brendow/Documents/Django/tdd_busca_animal/chromedriver.exe') #pega o driver do google

    def tearDown(self):
        self.browser.quit() #fecha janela do navegador
    
    def test_buscando_um_novo_animal(self):
        """Teste se um usuário encontra um animal pesquisando"""
        home_page = self.browser.get(self.live_server_url + '/')  #abre a pagina do navegador
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)



