import pygame
import os

#break down recursively beginning geographically

# wscreen = 800
# hscreen = 600

religion = ['christian', 'muslim', 'jewish', 'hindu', 'buddhist', 'atheist', 'agnostic', 'bahai', 'chinese_folk', 'confucianist', 'daoist', 'ethnoreligionist', 'jain', 'new_religionist', 'shintoist', 'sikh', 'spiritist', 'zoroastrian']

american_politics = ['republican', 'democrat', 'liberal', 'conservative', 'left', 'right', 'center', 'far_left', 'center_left', 'radical_center', 'center_right', 'far_right', 'communist', 'socialist', 'social_democratic', 'syncretic', 'populist', 'third_way', 'nationalist', 'none(intelligent)']

race = ['american_indian/alaska_native', 'asian', 'black', 'hispanic', 'hawaiian/islander', 'white']

gender = ['male', 'female', 'hermaphrodite']

pseudo_gender = ['agender', 'androgyne', 'androgynous', 'bigender', 'cis', 'cisgender', 'cis_female', 'cis_male', 'cis_man','cis_woman', 'cisgender_female', 'cisgender_male', 'cisgender_man', 'cisgender_woman', 'ftm', 'gender_fluid', 'gender_nonconforming', 'gender_questioning', 'gender_variant', 'genderqueer', 'intersex', 'mtf', 'neither', 'neutrois', 'non_binary', 'other', 'pangender', 'trans*', 'trans* female', 'trans* male', 'trans* woman', 'trans* man', 'trans* person', 'transgender', 'transgender_female', 'transgender_male', 'transgender_woman', 'transgender_man', 'transgender_person', 'transsexual' 'transfeminine', 'transmasculine', 'transsexual_female', 'transsexual_male', 'transsexual_person', 'transsexual_woman', 'transsexual_man', 'two_spirit', 'none']

dys_employment = ['home_stager', 'customer_service', 'trucker', 'psychiatrist', 'drug_dealer', 'janitor', 'taxi', 'server', 'actor', 'agent']

cause = ['blm', 'glm', 'lgbt+','anti-vax', 'anti-cpunishment','anti-circumcision', 'dv', 'ms', 'lyme', 'tenant_rights', 'autism', 'mgtow', 'feminism', 'pro-choice', 'anti-abortion', 'anti-cps', 'none' ]


#you = human(random select from each category)
#me = human('jain', 'none(intelligent)', 'white', 'tech', 'none', 'none')

class human:
	def __init__(self, religion, politics, race, gender, pseudo_gender, employment, cause):
		self.religion = religion
		self.politics = politics
		self.race = race
		self.gender = gender
		self.pseudo_gender = pseudo_gender
		self.employment = employment
		self.cause = cause
#h = human()
#h_attrs = [h.religion, h.politics, h.race, h.gender, h.pseudo_gender, h.employment, h.cause]

class avatar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        
        for i in range(0, 4):
            img = pygame.image.load(os.path.join('/home/pi/Documents/citizen_chain/img', 'protag' + str(i) + '.png')).convert()
            # transColor = img.get_at((0,0))
            # img.set_colorkey(transColor) 
            self.images.append(img)
            self.img = self.images[0]
            self.rect = self.img.get_rect()	    
