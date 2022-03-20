from django.test import LiveServerTestCase
from selenium import webdriver
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:/Users/brendow/Documents/Django/tdd_busca_animal/chromedriver.exe') #pega o driver do google
        self.animal = Animal.objects.create(
            nome_animal = "leão",
            predador = "Sim",
            venenoso = "Não",
            domestico = "Não"
        )

    def tearDown(self):
        self.browser.quit() #fecha janela do navegador
    
    def test_buscando_um_novo_animal(self):
        """Teste se um usuário encontra um animal pesquisando"""
        home_page = self.browser.get(self.live_server_url + '/')  #abre a pagina do navegador
        brand_element = self.browser.find_element_by_css_selector('.navbar') #pesquisa elemento navbar no html
        self.assertEqual('Busca Animal', brand_element.text) #procura se tem um navbar com nome Busca Animal no html

        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal') #pesquisa um input com id buscar-animal no html
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso...') #procura no atributo o placeholder = exemplo: leão

        buscar_animal_input.send_keys('leão') #digitar no campo input
        self.browser.find_element_by_css_selector('form button').click() #clica em um botão dentro de um form

        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)


