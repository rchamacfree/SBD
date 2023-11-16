#!/usr/bin/env python
# coding: utf-8

# # Cálculo de emisiones

# A partir del cálculo de km totales que le indiquemos, y con los datos de emisiones de los medios de transporte, calcula el total de emisiones del transporte usado.

# In[7]:


KMS_DIARIOS = 40
DIAS_LABORAIS_SEMANAIS = 5
SEMANAS = 24

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM_coche = 121
EMISION_X_KM_moto = 53

cantidade_de_emisions_coche = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_coche
print('O teu consumo en coche:', cantidade_de_emisions_coche, 'gC02')
cantidade_de_emisions_moto = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM_moto
print('O teu consumo en moto:', cantidade_de_emisions_moto, 'gC02')
print('Al utilizar la moto ahorras al planeta',cantidade_de_emisions_coche - cantidade_de_emisions_moto,' gC02')

